l=[234,456,765,243,789]
try:
    print(l[3])
    #print(a[2])
except(IndexError,NameError):
    print("please enter correct index")

else:
    print("execution completed sucessfully")

finally:
    print("ok done of the today")