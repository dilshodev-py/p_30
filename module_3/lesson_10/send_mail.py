# email:
#     password

# import smtplib, ssl
#
# port = 465  # For SSL
# smtp_server = "smtp.gmail.com"
# sender_email = "absaitovdev@gmail.com"
# receiver_email = "absaitovdev@gmail.com"
# password = "embpowysidjnhndo"
# message = """Hello World"""
#
# # context = ssl.create_default_context() # MAC UCHUN ISHLAMIDI !
# with smtplib.SMTP_SSL(smtp_server, port) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)



# -------------------- send mail html format ------------------


# import smtplib, ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
# sender_email = "absaitovdev@gmail.com"
# receiver_email = "absaitovdev@gmail.com"
# password = "embpowysidjnhndo"
#
# message = MIMEMultipart("alternative")
# message["Subject"] = "multipart test"
# message["From"] = sender_email
# message["To"] = receiver_email
# html = """\
# <html>
#   <body>
#     <p>Hi,<br>
#        How are you?<br>
#        <a href="http://www.realpython.com">Real Python</a>
#        has many great tutorials.
#     </p>
#   </body>
# </html>
# """
#
# part2 = MIMEText(html, "html")
#
# message.attach(part2)
#
# # context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#     server.login(sender_email, password)
#     server.sendmail(
#         sender_email, receiver_email, message.as_string()
#     )


# --------------------- file yuborish -----------

# import email, smtplib, ssl
#
# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# subject = "An email with attachment from Python"
# body = "This is an email with attachment sent from Python"
# sender_email = "absaitovdev@gmail.com"
# receiver_email = "absaitovdev@gmail.com"
# password = "embpowysidjnhndo"
#
# # Create a multipart message and set headers
# message = MIMEMultipart()
# message["From"] = sender_email
# message["To"] = receiver_email
# message["Subject"] = subject
# message["Bcc"] = receiver_email  # Recommended for mass emails
#
# message.attach(MIMEText(body, "plain"))
#
# filename = "/Users/user/PycharmProjects/p_30/module_3/lesson_10/send_mail.py"
#
# with open(filename, "rb") as attachment:
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload(attachment.read())
#
# encoders.encode_base64(part)
# part.add_header(
#     "Content-Disposition",
#     f"attachment; filename= send_mail_code.py",
# )
# message.attach(part)
# text = message.as_string()
#
# # context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, text)