from asyncio.format_helpers import _format_callback_source
import pyrebase
import json

class DBModule:
    def __init__(self):
        with open("./auth/firebaseAuth.json") as f:
            config = json.load(f)
            
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def login(self, uid, pwd):
        users = self.db.child("users").get().val()
        try:
            userinfo = users[uid]
            if userinfo["pwd"] == pwd:
                return True
            else:
                return False
        except:
            return False

    def register_verification(self, uid):
        users = self.db.child("users").get().val()
        for i in users:
            if uid == i:
                return False

        return True

    def register(self, _id_, pwd, name, email):
        information = {
            "pwd" : pwd, 
            "uname" : name, 
            "email" : email
        }
        if self.register_verification(_id_):
            self.db.child("users").child(_id_).set(information)
            return True
        else:
            return False