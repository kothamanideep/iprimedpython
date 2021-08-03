import timeit
# x=print("hello")
# print(timeit.timeit(stmt="a=10;b=5;a=a+b"))

# mycode='''
# a=10
# if(a<15):
#     pass'''
# print(timeit.timeit(stmt=mycode))

# def printnumbers():
#     for i in range(1000):
#         pass
# def printwhile():
#         n=0
#         while(n<=1000):
#             n=n+1
#             pass
# print(timeit.timeit(printnumbers,number=100000))
# print(timeit.timeit(printwhile,number=100000))

mylist=[12,34,45,678,654,678,987,567]
def f1():
    filter(12,mylist)
def f2():

    for i in mylist:
        if(i==43):
            pass
print(timeit.timeit(f1,number=100000))
print(timeit.timeit(f2,number=100000))


