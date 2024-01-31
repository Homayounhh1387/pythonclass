x = input("please enter your word: ")
import math
y = math.ceil(len(x)/2 -1)
print(x[y].upper())
print(x[y].lower())
num = int(input("enter your num: "))
sum = 0
for item in range(num +1 ):
    sum = sum + item
print(sum)