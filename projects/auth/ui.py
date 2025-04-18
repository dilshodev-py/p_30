from projects.auth.db.models import User


class UI:
    session_user : User | None = None

    def account(self):
        print(f"Welcome {self.session_user.first_name}")
    def login(self):
        auth = {
            "username" : input("Username:"),
            "password" : input("Password:")
        }
        user = User(**auth)
        self.session_user = user.is_auth()
        self.account()

    def register(self):
        user = {
            "first_name": input("First name:"),
            "username": input("User name:"),
            "password": input("Password:"),
        }
        user = User(**user)
        user.is_validation()
        user.save()
        self.main()

    def main(self):
        menu = """
            1) Register
            2) Login
            3) exit
            >>>"""
        try:
            match input(menu):
                case "1":
                    self.register()
                case "2":
                    self.login()

        except AssertionError as message:
            print(message)
            self.main()