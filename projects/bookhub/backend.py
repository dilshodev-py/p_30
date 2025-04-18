from dataclasses import dataclass
from stringprep import c6_set

users : list['User'] = []
categories : list['Category'] = []
books : list['Book'] = []
orders : list['Order'] = []

@dataclass
class User:

    id : int = 0
    first_name : str = None
    email : str = None
    password : str = None

    def is_valid(self):
        if self.email == "":
            return False , "Email formati xato"
        for user in users:
            if self.email and user.email == self.email:
                return False , "Oldin bu email ishlatilgan"
        if self.email and not self.email.endswith("@gmail.com"):
            return False , "Email formati xato"
        if not len(self.password) >= 4:
            return False , "Password uzunligi kalta ! min: 4 tadan ko'p bo'lsin"
        return True , "Mofaqiyatli o'tdi !"

    def is_login(self):
        for user in users:
            if user.email == self.email:
                if user.password == self.password:
                    return True , user
                else:
                    return False , "Password xato !"
        return False , "Bunday hisob mavjud emas"

    def save(self):
        User.id += 1
        users.append(self)

    def change_password(self , new_value):
        for user in users:
            if user.id == self.id:
                is_valid , message = User(password=new_value).is_valid()
                if is_valid:
                    setattr(user, "password" , new_value)
                    return True , "Mofaqiyatli o'zgartirildi"
                else:
                    return False , message

    def about(self):
        text = (
            f"Ism : {self.first_name}"
            f"Pochta : {self.email}"
            f"Password : {6*"*"}"
        )
        return text



@dataclass
class Category:
    id : int = 0
    name : str = None



@dataclass
class Book:
    id : int = 0
    title : str = None
    description : str = None
    price : float = None
    image : str = None
    author : str = None
    quantity : int = None
    category : Category = None

    def books_by_category(self):
        books = []
        for book in books:
            if book.category == self.category:
                books.append(book)
        return books

    def is_available(self):
        return self.quantity > 0

    def search(self , search_text):
        books = []
        for book in books:
            if search_text in self.author or search_text in self.title:
                books.append(book)
        return books

    def about(self):
        text = (
            f"Nomi : {self.title}"
            f"Tafsifi : {self.description}"
            f"price : {self.price} so'm"
            f"Rasm : {self.image}"
            f"Yozuvchi: {self.author}"
            f"Zahirada : {self.quantity} ta"
            f"Janri : {self.category.name}"
        )
        return text



@dataclass
class Order:
    id : int = 0
    book : Book = None
    user : User = None
    cost : float = None
    count : int = None
    status : str = None
    ordered_at : str = None

    def save(self):
        Order.id += 1
        orders.append(self)

    def checkout(self):
        if self.book.quantity <= 0:
            return False , "Kitob qolmagan"
        if self.book.quantity < self.count:
            return False , f"Siz hohlagan miqdorda kitob mavjud emas ! Bunday kitobdan : {self.book.quantity} ta qolgan"
        self.book.quantity -= self.count
        self.status = "completed"
        return True , "Mofaqiyatli to'lov amalga oshirildi"

    def clear_order(self):
        for order in orders:
            if order.user == self.user:
                if order.status == "new":
                    orders.remove(order)

    def history(self):
        results = []
        for order in orders:
            if order.user == self.user:
                if order.status == "completed":
                    results.append(order)
        return results



















