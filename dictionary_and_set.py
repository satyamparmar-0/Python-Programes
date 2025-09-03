# Dictionary Operations
# Both set and dictionary in python are mutable data structures

dict_1= {"michael":89,"lincon":85,"jatin":86,"sumit":65}
dict_1["michael"]=90
print("michael" in dict_1)
print(dict_1.items())
print(dict_1.keys())
print(dict_1.clear())
# Set Operations

set_1={"michael","lincon","sucre"}
print(set_1)
print(set_1.copy())
print(set_1.clear())
print(set_1.add("chanki"))
# set_1.remove("chanki")
print(set_1)
print(set_1.pop())
