# ==================== 3.1 ======================

# phone = {
#     "name" : "16 pro max",
#     "model" : "Iphone",
#     "year" : 2024,
#     "color" : "black"
# }
# while phone:
#     print("================")
#     print(phone)
#     print("================")
#     key = input("Kalit:")
#     print(phone.pop(key , "Bunday kalit topilmadi!"))
# print(phone)


# ============================================


# contacts = []
# while True:
#     menu = """
#         *) search 🔎
#         1) contact +
#         2) delete
#         3) contacts
#         4) exit
#         >>>"""
#     key = input(menu)
#     match key:
#         case "*":
#             search = input("🔎:").lower()
#             for contact in contacts:
#                 fullname = contact.get("fullname")
#                 phone_number = contact.get("phone_number")
#                 if search in fullname.lower() or search in phone_number:
#                     print(contact)
#
#         case "1":
#             fullname = input("Fullname:")
#             phone_number = input("Phone number:")
#             new_contact = {
#                 "fullname" : fullname,
#                 "phone_number" : phone_number
#             }
#             contacts.append(new_contact)
#             print("Success save !")
#         case "2":
#             for pos , contact in enumerate(contacts,1):
#                 text = f"{pos}) {contact.get("fullname")}:{contact.get("phone_number")}"
#                 print(text)
#             index = int(input(">>>"))-1
#             is_sure = input("Are you sure [y/N]?")
#             if is_sure == "y":
#                 del_contact = contacts.pop(index)
#                 print(f"Delete ✅: {del_contact} ")
#             else:
#                 print("Abort delete !")
#         case "3":
#             for pos, contact in enumerate(contacts, 1):
#                 text = f"{pos}) {contact.get("fullname")}:{contact.get("phone_number")}"
#                 print("--------------------")
#                 print(text)
#                 print("--------------------")
#
#             input("Click Enter to Back !")
#
#         case "4":
#             break





