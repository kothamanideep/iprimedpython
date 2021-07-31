try:
    n1=int(input("enter the number:"))
    n2=int(input("enter second number:"))
    div=n1/n2
    print(div)

except ZeroDivisionError:
    print("opps!, something went wrong")

except ValueError:
    print("only number should be entered")