# from module_2.lesson_1.xolodilnik import *


# class Animal:
#     def __init__(self ,
#                  name : str ,
#                  gender : str ,
#                  habitat: str):
#         self.name = name
#         self.gender = gender
#         self.habitat = habitat
#
#     def about(self):
#         text = f"""
#             nomi : {self.name}
#             jinsi : {self.gender}
#             yashash joyi : {self.habitat}
#         """
#         return text
#
#     def __repr__(self):
#         return self.name
#
#
# class Bird(Animal):
#     def __init__(self , name , gender , habitat , is_fly):
#         super().__init__(name, gender, habitat)
#         self.is_fly = is_fly
#
#     def about(self):
#         return super().about() + f"\tucha oladimi : {self.is_fly}"
#
#
# animals = []
#
# class PlatForm:
#     def add(self , animal : Animal):
#         animals.append(animal)
#
#
#
#
# b1 = Bird("Tuya qush" , "F" , "Afrika" , False)
# print(b1.about())

accounts : list['Account'] = []

class Account:
    def __init__(self,card_number , owner = None , balance= None):
        self.owner = owner
        self.card_number = card_number
        self.balance = balance

    def deposit(self,to_account , transfer_money):
        foiz_amount = transfer_money * 0.01
        to_account.balance -= foiz_amount
        to_account.balance -= transfer_money
        self.balance += transfer_money

    def withdraw(self ,to_account, transfer_money):
        foiz_amount = transfer_money * 0.01
        self.balance -= foiz_amount
        self.balance -= transfer_money
        to_account.balance += transfer_money

    def __repr__(self):

        return f"Account(owner={self.owner},balance={self.balance})"


class SavingSAccount(Account):

    def save(self):
        accounts.append(self)


class CheckingAccount(Account):
    company_balance = 0
    def valid_transfer(self, to_card_number: int , transfer_money:float , type:str):
        to_account = None
        from_account = None
        for account in accounts:
            if account.card_number == to_card_number:
                to_account = account
            elif account.card_number == self.card_number:
                from_account = account
                self = from_account
        if to_account and from_account:
            if type == "withdraw":
                if from_account.balance-transfer_money*0.01 >= transfer_money:
                    self.withdraw(to_account ,transfer_money)
                    return "Success withdraw"
                else:
                    return "Balanse yetarli emas"
            elif type == "deposit":
                if to_account.balance - transfer_money*0.01 >=transfer_money:
                    self.deposit(to_account , transfer_money)
                    return "Success deposit!"
                else:
                    return "Balanse yetarli emas"
        else:
            return "Malumotlar xatto!"

account1 = SavingSAccount(owner="Daler" , balance=1_000_000 , card_number=9860123412341234)
account1.save()
account2 = SavingSAccount(owner="Botir" ,balance= 2_000_000 , card_number=5860123412341234)
account2.save()


transfer = CheckingAccount(9860123412341234)
print(transfer.valid_transfer(5860123412341239, 500_000, type="withdraw"))
transfer = CheckingAccount(5860123412341234)
print(transfer.valid_transfer(98601234123412389, 2_000_000, type="withdraw"))

print(accounts)



