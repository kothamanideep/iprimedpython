#namedtuple
import collections
employees=collections.namedtuple("employees",["name","empid","salary"])
e1=employees("raju","1001","1000")
print(e1[0])



# import collections
# d1=collections.OrderedDict()
# d1['name']='mani'
# d1['rollno']='21'
# d1['admin']='1000'
# for key,value in d1.items():

#  print(key,value)