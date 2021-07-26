class calculator:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print (a-b)
    def mul(self,a,b):
        print( a*b)
    def floordiv(self,a,b):
        print(a//b)

cal=calculator()

a1=int(input("enter first  number: "))
b1=int(input("enter second number: "))
add1=cal.add(a1,b1)
sub1=cal.sub(a1,b1)
mul1=cal.mul(a1,b1)
frdiv=cal.floordiv(a1,b1)




        
