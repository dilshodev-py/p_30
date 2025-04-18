from unittest.mock import sentinel

users : list['User']=  []

class Category:
    def __init__(self ,
                 id : int = None ,
                 name : str = None ,
                 image : str = None):
        self.id = id
        self.name = name
        self.image = image

class Product:
    def __init__(self ,
                 id:int=None ,
                 name : str = None,
                 price : float = None,
                 image : str = None,
                 type : str = None,
                fields : dict = None,
                 description : str = None,
                 discount : int = None,
                 category : Category = None
                 ):
        self.id = id
        self.name = name
        self.price = price
        self.image = image
        self.type = type
        self.fields = fields
        self.description = description
        self.discount = discount
        self.category = category

class User:
    def __init__(self ,
                 id : int = None,
                 phone_number : str = None,
                 first_name : str = None,
                 image : str = None,
                 email : str = None,
                 instagram_username : str = None,
                 telegram_username : str = None,
                 is_premium : bool = False,
                 lang : str = None):
        self.id = id
        self.phone_number = phone_number
        self.first_name = first_name
        self.image = image
        self.email = email
        self.instagram_username = instagram_username
        self.telegram_username = telegram_username
        self.is_premium = is_premium
        self.lang = lang

class Order:
    def __init__(self,
                 id : int = None,
                 owner : User = None,
                 total_amount: float = None,
                 amount : float = None,
                 ordered_at : str = None
                ):
        self.id = id
        self.owner = owner
        self.total_amount = total_amount
        self.amount = amount
        self.ordered_at = ordered_at

class OrderItem:
    def __init__(self,
                 id: int = None,
                 order: Order = None,
                 product: Product = None,
                 quantity : int = 1):
        self.id = id
        self.order = order
        self.product = product
        self.quantity = quantity

class Auth:
    def register(self , user : User):
        users.append(user)

    def login(self , phone_number):
        for user in users:
            if user.phone_number == phone_number:
                code = self.send_sms(phone_number)
                verify_code = input("Code:")
                if code == verify_code:
                    return "Success login!"
                else:
                    return "Invalid code"
        return "Not found Account"

    def send_sms(self , phone_number):
        return "987656"

class Message:
    def __init__(self ,
                 id : int = None ,
                 message : str = None ,
                 owner : User = None):
        self.id = id
        self.message = message
        self.owner = owner

class Language:
    UZBEK = "uz"
    ENGLISH = "en"

class Location:
    def __init__(self ,
                 id : int = None,
                 longitude : float = None,
                 latitude : float = None,
                 owner : User = None,
                 order : Order = None):
        self.id = id
        self.longitude = longitude
        self.latitude = latitude
        self.owner = owner
        self.order = order

class SiteConfig:
    def __init__(self ,
                 id : int = None ,
                 nds : int = None,

                 ):
        self.id = id
        self.nds = nds

class Wishlist:
    def __init__(self ,
                 id : int = None,
                 product : Product = None,
                 owner : User = None):
        self.id = id
        self.product = product
        self.owner = owner



daler = User(
    1 ,
    "+998991231212" ,
    "Daler" ,
    "http://image.png" ,
    "daler@gmail.com",
    lang=Language().UZBEK
)

Auth().register(daler)
print(users)
print(Auth().login("+998991231212"))

category = Category(
    1 , "Meva" , "http://meva.png"
)

product1 = Product(
    1 ,
    "Anor" ,
    40990 ,
    "http://image.png" ,
    "weight" ,
    {"Калории" : "83 ккал" , "Белки" : "1,7г"},
    """Фрукт, известный своим насыщенным вкусом и уникальной текстурой. Он ценится не только за свои вкусовые качества, но и за многочисленные полезные свойства, что делает его популярным выбором среди любителей здорового питания.""",
    50,

)

product2 = Product(
    1 ,
    "Gilos" ,
    40990 ,
    "http://image.png" ,
    "weight" ,
    {"Калории" : "83 ккал" , "Белки" : "1,7г"},
    """Фрукт, известный своим насыщенным вкусом и уникальной текстурой. Он ценится не только за свои вкусовые качества, но и за многочисленные полезные свойства, что делает его популярным выбором среди любителей здорового питания.""",
    50,
    category
)

savat = Order(1 , daler , ordered_at="2024-12-27 09:55:30")

item1 = OrderItem(1 , savat , product1 , 2)
item2 = OrderItem(2 , savat , product2 , 5)



message1 = Message(1 , "salom" , daler)
message2 = Message(2 , "Yordam kerak" , daler)
message3 = Message(3 , "Men mahsulotni qaytarmoqchiman" , daler)
message4 = Message(4 , "Meni balansimda pul kam" , daler)

location = Location(1 , 41.335258, 69.230050 , owner=daler)


SiteConfig(1 , 15)

