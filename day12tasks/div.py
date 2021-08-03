import logging
a=int(input("enter number:"))
b=int(input("enter second number"))
x=a/b
logging.basicConfig(filename='division.log',level=logging.DEBUG)
logging.info(x)