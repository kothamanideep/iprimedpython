with open('file5.txt','w+') as x:
    x.write("hello")
    x.seek(0)
    print(x.read())