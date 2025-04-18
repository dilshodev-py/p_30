# import json
#
# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get('https://kun.uz/')
# html_code:str = response.text

# soup = BeautifulSoup(html_code , "html.parser")
# carts:list = soup.find_all('div' , {"class" : "small-cards__default-item"})
# news = []
# for cart in carts:
#     new = {
#     "title" : cart.find('a' , {"class" : "small-cards__default-text"}).text,
#     "category" : cart.find('div' , {"class" : "gray-text"}).text.strip(),
#     "photo" : cart.find('img')['src']
#     }
#     news.append(new)
# with open('news.json' , 'w') as f:
#     json.dump(news,f , indent=3)

"""
    Bomdod : 05:47
    Quyosh : 07:05
    Peshin : 12:41
    Asr : 16:24
    Shom : 18:10
    Xufton : 19:24
"""

"""
viloytalardan tanlang:
    1) Toshkent
    2) Samarqand
    .....
>>>

Tumanlardan birini tanlang:
    1) Qorasuv
    2) Boysun
    ....
    0) back
>>>

Nomoz vaqti:
    Bomdod : 05:47
    Quyosh : 07:05
    Peshin : 12:41
    Asr : 16:24
    Shom : 18:10
    Xufton : 19:24
"""

"""
viloytalardan tanlang:
    1) Toshkent
    2) Samarqand
    .....
>>>

kunlar:
    1) bugun
    2) Seshanba
    3) Chorshanba
    ...
    0) back
>>>

ob havo:
    Harorat : +17° +6°  
    Tavsif : 🌧
    Yog'ingarchilik : 100%
"""


