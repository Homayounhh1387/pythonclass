
def av(x,y):
   a = (x+y) / 2
   
   if a < x:
      print("x is bigger than average")
   else:
      print("x is not bigger than average")

   if a < y:
      print("y is bigger than average")
   else:
      print("y is not bigger than average")
   print(int(a))
   
av(int(input("entet your number: ")),int(input("entet your number: ")))



# x = 20
# y = 13
# av = (x+y) / 2

# if x > av:
#    print("x is bigger than average")
# else:
#    print("x is not bigger than average")

# if y > av:
#    print("y is bigger than average")
# else:
#    print("y is not bigger than average")