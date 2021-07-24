import smtplib
a="INDIA IS MY COUNTRY"
print(a[0:6])
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("manideepkotha324@gmail.com","mani@9324")
message=" INDIA "
connection.sendmail("manideepkotha@gmail.com","kothamanideep123@gmail.com",message)
connection.quit()