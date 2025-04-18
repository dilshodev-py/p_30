# Backend
# UI
from typing import Optional

users : list['User']=  []
class User:
    def __init__(self ,
                 id = None,
                 first_name = None,
                 last_name = None,
                 email = None,
                 password = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def save(self):
        self.id = users[-1].id + 1 if users else 1
        users.append(self)

    def is_valid(self):
        for user in users:
            if self.email and user.email == self.email:
                return False , "Already exists email !"

        if self.password and len(self.password) < 6:
            return False , "Invalid Password !"

        return True , "Success !"

    def is_login(self):
        for user in users:
            if user.email == self.email:
                if user.password == self.password:
                    return True , user
                else:
                    return False , "Wrong password !"

        return False , "Not Found account !"

    def about(self):
        text = f"""
            Fullname : {self.first_name} {self.last_name}
            email : {self.email}
            password : {len(self.password) * "*"}
            """
        return text

    def delete(self):
        for user in users:
            if user.id == self.id:
                users.remove(user)

    def update(self , field , new_value):
        for user in users:
            if user.id == self.id:
                if field == "email":
                    is_valid , message = User(email=new_value).is_valid()
                    if is_valid:
                        setattr(user, field, new_value)
                    else:
                        return message
                elif field == "password":
                    is_valid, message = User(password=new_value).is_valid()
                    if is_valid:
                        setattr(user, field, new_value)
                    else:
                        return message
                else:
                    setattr(user, field, new_value)
        return  "Success edit !"

# ================================= Front-end =======================

class UI:
    session_user : Optional['User'] = None

    def register(self):
        user = {
            "first_name" : input("First name : "),
            "last_name" : input("Last name : "),
            "email" : input("Email : "),
            "password" : input("Password : ")
        }
        user = User(**user)
        is_valid , message = user.is_valid() # (bool , str)
        if is_valid:
            user.save()
        print(message)
        self.main()

    def main(self):
        menu = """
            1) Register
            2) Login
            3) Exit
            >>>"""
        key = input(menu)
        match key:
            case "1":
                self.register()
            case "2":
                self.login()
            case "3":
                return

    def login(self):
        auth = {
            "email" : input("Email:"),
            "password" : input("Password:")
        }
        auth = User(**auth)
        is_login , response = auth.is_login() # (bool , [obj , str])
        if is_login:
            self.session_user = response
            self.account()
            return
        print(response)
        self.main()

    def account(self):
        print(f"Welcome to account {self.session_user.first_name} {self.session_user.last_name}")
        menu = """
            1) Panel
            2) Settings
            3) logout
            >>>"""
        key = input(menu)
        match key:
            case "1":
                pass

            case "2":
                self.settings()

            case "3":
                self.session_user = None
                self.main()

    def settings(self):
        menu = """
            1) Edit
            2) About
            3) Delete Account
            0) Back
        """
        key = input(menu)
        match key:
            case "1":
                self.edit()

            case "2":
                print(self.session_user.about())
                input("Click Enter Back")
                self.settings()

            case "3":
                key = input("[y/N]")
                if key == "y":
                    self.session_user.delete()
                    self.session_user = None
                    self.main()
                    return
                self.settings()

            case "0":
                self.account()

    def edit(self):
        map = {
            "1" : "first_name",
            "2" : "last_name",
            "3" : "email",
            "4" : "password",
        }
        menu = """
            1) First name
            2) Last name
            3) Email
            4) Password
            0) Back
        """
        key = input(menu)
        if key == "0":
            self.settings()
            return
        field = map.get(key)
        new_value = input("New Value: ")
        print(self.session_user.update(field, new_value))
        self.settings()

UI().main()