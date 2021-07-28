# class a:
#     def sayhello(self):
#         print("hello")

# class b(a):
#     def sayhello(self):
#         print("hai")

# obja=a()
# objb=b()
# obja.sayhello()
# objb.sayhello()

def add(a,b,c=0):
    return a+b+c

print(add(2,3))
print(add(2,3,4))