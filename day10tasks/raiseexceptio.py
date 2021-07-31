try:
    n1=int(input("enter the number"))
    if n1<0:
        raise ValueError(n1)
    else:
        print(n1)
except ValueError:
    print("n1 is out of range")