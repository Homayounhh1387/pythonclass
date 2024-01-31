first = False
while not first:
    try:
        first = int(input("Enter your number: "))
        we = input("enter your we: ")
    except ValueError:
        print("you have to enter a number")
second = False
while not second:
   try:
    second = int(input("Enter your another number: "))
   except ValueError:
       print(" you have to enter a number")
       
if we == "+":
    print(first + second)
elif we == "-":
    print(first - second)
elif we == "/":
    print(first / second)
elif we == "*":
    print(first * second)
elif we == "**":
    print(first ** second)