# list=[1,3,45,34,2,4,6,8,9,7]
# new=[i for i in list if i%2==0]
# print(new)

list=['english','email','civic','river','rotor','malayalam','madam','example','running','noon']
# new=[i for i in list if i==i[::-1]]
# print(new)

# list=[i for i in range(2,500)]
# new=[j for j  in list if j%2!=0]
# print(new)

new=[i.replace('noon','morning') for i in list]
print(new)

