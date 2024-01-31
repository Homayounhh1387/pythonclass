# name = "Homaypun"
# import math 
# capital = (math.ceil(len(name)/ 2))
# print(capital)


# print(name[5].upper())
# print(name.replace("p" , "o"))
# x = len(name)

# x = input("enter your word: ")
# print(x.upper())

capmil = input("please enter your word: ")
import math
m=math.ceil(len(capmil)/2 -1)
before = capmil[:m]
mid = capmil[m]
after = capmil[m+1:]
print(before + mid.upper() + after)
print(before + mid.lower() + after)

