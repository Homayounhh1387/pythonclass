# dict1 = ["name","lastname","age"]
# dict2 = ["homayoun",'jafari',"15"]

# person = {item:item2 for item,item2 in zip(dict1,dict2)}
# print(person)
# y = []
# n = 0

# evens = [x for x in range(101) if x % 2 == 0]
# print(evens)

x = {1,2,3,4,5,6,7}
y = {3,4,5,6,43,4,5,64,32,33,3,3,3,3,}
z = x.union(y)
print(z)
z1 = y.intersection(x)
print(z1)