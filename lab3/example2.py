x1 = int(input("please enter the first number: "))
x2 = int(input("please enter the second number: "))
x3 = int(input("please enter the third number: "))

if x1 < x2 and x1 < x3:
  print(x1)
if x2 < x3 and x2 < x1:
  print(x2)
if x3 < x1 and x3 < x2:
  print(x3)