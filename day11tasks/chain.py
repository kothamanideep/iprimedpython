#chainmap
import collections
dict1={"name":"mani","age":21}
dict2={"name":"guru","age":21}
comb_dict=collections.ChainMap(dict1,dict2)
print(comb_dict.maps)
print(list(comb_dict.keys()))






