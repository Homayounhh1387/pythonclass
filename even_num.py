# evens = [num for num in range(101) if num % 2 == 0]
# print(evens)
#___________________________________________________

# x = int(input(("please enter your num: ")))

# if x % 2 == 0:
#     print(x)
#     print("your num is even.")
# else:
#     print(x)

#     print("your num is odd")

try:
    x = int(input("Please enter your first num: "))
except:
    print("You gotta enter a num.")
sum1 = 0
for z in range(x+1):
    sum1 = z + sum1   
# x = input("plese enter a num: ")
# print(x)
print(str(sum1) + " this is your first num")
y = int(input("please enter your second num: "))
sum2 = 0
for s in range(y+1):
    sum2 = s + sum2
print(str(sum2) + " this is your second num" )
f = int(input("Please enter your thirst num: "))
sum3 = 0
for c in range(f+1):
    sum3 = c + sum3

fd = (sum1 + sum2 + sum3) / 3
print(str(sum3) + " this is your thirst num")
print(fd)
