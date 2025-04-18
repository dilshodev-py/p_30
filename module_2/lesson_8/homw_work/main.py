import datetime
from dataclasses import dataclass

@dataclass
class User:
    id : int = None
    name : str = None
    username : str = None
    password : str = None

    def login_log(self , user_id):
        with open("logs.txt" , "a") as f:
            now = datetime.datetime.now()
            f.write(f"{user_id}|LOGIN|{now}\n")

    def logout_log(self , user_id):
        with open("logs.txt" , "a") as f:
            now = datetime.datetime.now()
            f.write(f"{user_id}|LOGOUT|{now}\n")

    def statistika(self):
        with open("logs.txt" , "r") as f:
            data  =f.readlines()

        login_time = datetime.datetime.fromisoformat(data[0].split("|")[-1].strip())
        logout_time = datetime.datetime.fromisoformat(data[1].split("|")[-1].strip())
        print("Botir : " ,  logout_time - login_time)



    def save(self):
        with open("users.txt") as f:
            users : list[str] = f.readlines()
        for user in users:
            obj = User(*user.split('|'))
            if obj.username == self.username:
                if obj.password == self.password:
                    self.login_log(obj.id)
                    return True , "Login !"

# print(User(username="botir_007" , password="1234").save())


User().statistika()



