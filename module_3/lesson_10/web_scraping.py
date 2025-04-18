import json

import requests

# json.dump() # obj -> json file
# json.load() # json file -> obj
# json.loads() # json(str) -> obj
# json.dumps() # obj -> json(str)

# cars = [
#     {
#         "name" : "S5",
#         "model" : "BMW"
#     }
# ]
# t = str(cars)
# t2 = list(t)
# print(t2)


# data = json.dumps(cars , indent=3)
# print(type(data))
# d = json.loads(data)
# print(type(d))
# new_car = {
#     "name" : "Nexia 1",
#     "model" : "Chevrolet"
# }
# with open('cars.json' , 'r') as f:
#     cars_load:list = json.load(f) # list[dict]
# cars_load.append(new_car)
# with open("cars.json" , 'w') as f:
#     json.dump(cars_load, f , indent=3) # noqa


# response = requests.get("https://dummyjson.com/products")
# print(response.json())
# requests.post()
# requests.patch()
# requests.put()
# requests.delete()

# response = requests.get(url="https://kun.uz/")
# print(response.text)

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """

# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.find('p').text)
# soup.find()
# for a in soup.find_all('a'):
#     print(a.text)





