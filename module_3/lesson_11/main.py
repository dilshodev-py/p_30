# import time
# from time import process_time_ns
# import smtplib, ssl
# from threading import Thread
#
# emails = """waht2332@gmail.com
# my.main9860@gmail.com
# ravshansharipov078@gmail.com
# qwertyllionman@gmail.com
# abrorrizayevv@gmail.com
# asadsultonov277@gmail.com
# usmanovj141@gmail.com
# xunuddinovshaxob@gmail.com
# xabibullo.nazrullayev@gmail.com
# salimjon001003@gmail.com
# gulrukhkhalilovna@gmail.com
# azimbekhakimov2@gmail.com
# wfayoz@yahoo.com
# dmukhammadamin@gmail.com
# """.split()
# #
# #
#
# def send_mail(receiver):
#     port = 465
#     smtp_server = "smtp.gmail.com"
#     sender_email = "absaitovdev@gmail.com"
#
#     password = "embpowysidjnhndo"
#     message = """Hello World"""
#     with smtplib.SMTP_SSL(smtp_server, port) as server:
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver, message)
#
# start = time.time()
# threads = []
# for email in emails:
#     thread = Thread(target=send_mail , args=(email,))
#     thread.start()
#     threads.append(thread)
# for t in threads:
#     t.join()
#
# end = time.time()
# print(end-start)
# import time
# from threading import Thread
# # main thread
#
# def task1():
#     print("Start task1")
#     time.sleep(1)
#     print("Finish task1")
#
# def task2():
#     print("Start task2")
#     time.sleep(1)
#     print("Finish task2")
#
# def task3():
#     print("Start task3")
#     time.sleep(1)
#     print("Finish task3")
#
# start = time.time()
# tasks = [task1 , task2 , task3]
# threads = []
# for task in tasks:
#     thread = Thread(target=task)
#     thread.start()
#     threads.append(thread)
# for thread in threads:
#     thread.join()
# end = time.time()
# print(end-start)



"""

"""
import asyncio
import time


# import time
# from threading import Thread
# from multiprocessing import Pool
#
#
# with Pool(10) as p:
#     p.map(targer=func)

# import requests
#
# """
#
# """
#
#
# response = requests.get('https://picsum.photos/id/102/4320/3240')
# with open('random_img.png' , "wb") as f:
#     f.write(response.content)

# async(thread , process)

async def function():
    time.sleep(1)
    print("Hello World")

async def function1():
    await function()


async def function2():
    await function1()

asyncio.run(function2())





# def tmp():
#     time.sleep(1)
#
# l = range(10000)
# start = time.time()
# threads = []
# for i in l:
#     t= Thread(target=tmp)
#     t.start()
#     threads.append(t)
# for t in threads:
#     t.join()
#
# end = time.time()
# print(end-start)



# process -> 1000
# process -> 1000
# process -> 1000
# process -> 1000
# process -> 1000
# process -> 1000
# process -> 1000
# process -> 1000
# process -> 1000
# process -> 1000
# process -> 1000



