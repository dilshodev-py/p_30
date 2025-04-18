# strs = ["flower","flow","flight"]
# result = ""
# for i in min(strs , key=len):
#     for item in strs:
#         if not item.startswith(result):
#             print(result[:-1])
#             break
#     result += i


# =========================

# s = "([()]{})"
# d = {
#     ")" : "(",
#     "]" : "[",
#     "}" : "{",
# }
#
# tmp = []
# for i in s:
#     if i in d:
#         if tmp and tmp[-1] == d[i]:
#             tmp.pop()
#         else:
#             tmp.append(i)
#     else:
#         tmp.append(i)
# print(not tmp)


# =============================================

# class User:
#     pass
#
# john = User()
#
# class Shape:
#     pass
#
# circle = Shape()
#
# class Animal:
#     pass
#
# cat = Animal()


# ============================================


# class User:
#     now_year = 2024 # class attribute
#     def __init__(self, fullname ,age , username):
#         self.fullname = fullname # class object attribute
#         self.age = age           # class object attribute
#         self.username = username # class object attribute
#     def __repr__(self) -> str:
#         return f"User(fullname={self.fullname},age={self.age},username={self.username})"
#
#
#
# john = User("John" , 25 , "john_07")
# fayoz = User("Fayoz" , 19 , "fayoz")
#
# print(john , fayoz)
# print([john , fayoz])


# ===================================================

# users = []
# class User:
#     now_year = 2024 # class attribute
#     def __init__(self, fullname ,age , username):
#         self.fullname = fullname # class object attribute
#         self.age = age           # class object attribute
#         self.username = username # class object attribute
#
#     def find_birth_year(self):
#         return self.now_year - self.age
#
#     def hi(self):
#         return f"Hi {self.fullname}"
#
#     def save(self):
#         users.append(self)
#
#     def delete(self):
#         if self in users:
#             users.remove(self)
#         else:
#             print("Bunday user malumotlar omborida mavjud emas !")
#
#     def __repr__(self) -> str:
#         return f"User(fullname={self.fullname},age={self.age},username={self.username})"
#
# fullname = input("Fullname:")
# fayoz = User( fullname, 19 , "fayoz")
#
# print(fayoz.find_birth_year())
# print(fayoz.hi())
# fayoz.save()
# fayoz.save()
# print(users)
# fayoz.delete()
# fayoz.delete()
# fayoz.delete()
# print(users)



# ===========================================



# users: list['User'] = []
#
# class User:
#     def __init__(self , name , company , email , password):
#         self.name = name
#         self.company = company
#         self.email = email
#         self.password = password
#
#     def save(self):
#         users.append(self)
#
#     def signup(self):
#         self.save()
#         print("Success save !")
#
#     def __repr__(self):
#         return self.name
#
# name = input("Name:")
# company = input("Company:")
# email = input("Email:")
# password = input("Password:")
# u = User(password=password , company=company , email=email ,name=name)
# u.signup()
# print(users)


# ===================================================

# orders = []
#
# class Product:
#     def __init__(self , image:str , title : str  , price : float):
#         self.image = image
#         self.title = title
#         self.price = price
#
#     def add_to_cart(self):
#         orders.append(self)


# ------------------- kun.uz -------------------------

categories : list['Category'] = []
class Category:
    def __init__(self ,id = None, name = None):
        self.id = id
        self.name = name

    def save(self):
        self.id = categories[-1].id + 1 if categories else 1
        categories.append(self)

    def delete(self):
        for category in categories:
            if category.id == self.id:
                categories.remove(category)


    def edit(self , new_name):
        for category in categories:
            if category.id == self.id:
                category.name = new_name

    def get(self ):
        for category in categories:
            if category.id == self.id:
                return category

    def __repr__(self):
        return f"Category(id={self.id},name={self.name})"


c1 = Category(name="O'zbekiston")
c1.save()
c2 = Category(name="Jahon")
c2.save()


news:list['NewPost'] = []

class NewPost:
    def __init__(self ,id : int = None, created_at : str = None , title: str = None , description : str = None , category: Category = None):
        self.id = id
        self.created_at = created_at
        self.title = title
        self.description = description
        self.image = []
        self.views = 0
        self.category = category

    def search_name(self):
        result = []
        for new in news:
            if self.title.lower() in new.title.lower():
                result.append(new)
        return result


    def save(self):
        self.id = news[-1].id + 1 if news else 1
        news.append(self)

    def delete(self):
        for new in news:
            if new.id == self.id:
                news.remove(new)


    def edit(self , new_name):
        for new in news:
            if new.id == self.id:
                new.name = new_name

    def get(self ):
        for new in news:
            if new.id == self.id:
                return new

    def filter_by_category(self, category_id):
        result = []
        for new in news:
            if new.category.id == category_id:
                result.append(new)
        return result


new = {
    "created_at" : "2024-12-25",
    "title" : "RFda Ukrainaga qarshi urush qatnashchilari imtiyozli ipotekani ololmaydi",
    "description" : """Rossiya Moliya vazirligi Davlat dumasi deputatlarining Rossiyaning Ukrainaga qarshi urushi qatnashchilari uchun imtiyozli — yillik 2 foizli ipoteka kreditlash dasturini qabul qilish tashabbusini rad etdi. Moliya vaziri o‘rinbosari Ivan Chebeskovning 24 dekabr, seshanba kuni RIA "Novosti" agentligi iqtibos keltirgan javobida aytilishicha, mavjud dasturlar «ipoteka kreditlash bozorida sezilarli nomutanosibliklarga olib kelgan» va shartlar qayta-qayta kengaytirilgan. Fuqarolar va obektlar tobora ortib bormoqda, ammo oxir-oqibat imtiyozli ipoteka maqsadli chora-tadbirlardan ommaviy mahsulotga aylandi.

«Bu... oldimizga qo‘yilgan barcha maqsadlarga erishishga, birinchi navbatda, fuqarolar uchun uy-joy sotib olish imkoniyatini oshirishga imkon bermadi», — deya tushuntirdi vazirlik. U yangi ipoteka mexanizmlarini joriy qilish uchun budjetdan qo‘shimcha mablag‘lar zarurligini tushuntirdi, biroq ularning manbalari aniqlanmagan.

Sberbank asosiy ipoteka dasturlari bo‘yicha stavkalarni oshirdi

15 noyabrdan boshlab Sberbank asosiy ipoteka dasturlari bo‘yicha stavkalarni 3,5 foiz punktga oshirdi. Shunday qilib, qurilayotgan uy-joy uchun kreditlar bo‘yicha minimal stavka 28,4 foizni, tayyor uy-joy uchun — 28,1 foizni tashkil etdi.

15 noyabrdan boshlab Sberbank, shuningdek, davlat tomonidan belgilangan limitdan yuqori oilaviy ipoteka dasturi bo‘yicha kredit olish uchun ariza berishda o‘rtacha stavkalarini 1-2,5 foiz punktiga oshirdi.

Moskva, Moskva oblasti, Sankt-Peterburg va Leningrad oblasti uchun minimal stavka 13,5 million rubl miqdoridagi kredit miqdori uchun 11,8 foizgacha ko‘tarildi. Kredit summasi yetti milliondan ortiq bo‘lgan boshqa hududlar uchun bu ko‘rsatkich 12,9 foizni tashkil etdi.

«IT uchun ipoteka» dasturi doirasida 10,5 million rubl miqdoridagi kredit uchun stavka 13 foizgacha ko‘tarildi.""",
    "category" : c2,

}

#
# nw1 = NewPost(**new)
# nw1.save()


# print(NewPost().filter_by_category(category_id=2))
# print(NewPost(title="ukraina").search_name())














