import smtplib
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("manideepkotha324@gmail.com","mani@9324")
message="hi my name is manideep"
connection.sendmail("manideepkotha@gmail.com","kothamanideep123@gmail.com",message)
connection.quit()