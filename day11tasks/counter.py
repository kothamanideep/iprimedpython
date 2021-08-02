#counter ()
import collections
# x=collections.Counter(["hello","hello","mani"])
# print(x)
li=[]
for i in range(1,11):
    names=input("enter your name")
    li.append(names)
x=collections.Counter(li)
print(x)




