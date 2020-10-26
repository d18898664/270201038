print("Discriminant Program")
print("It is like ax2 + bx + c")
a = int(input("enter the first number for a:"))
b = int(input("Enter the second number for b: "))
c = int(input("Enter the third number for c: "))

d = (b ** 2) - (4 * a * c)

r1= ((-1 * b) + (d ** 0.5)) / -2 * a
r2= ((-1 * b) - (d ** 0.5)) / -2 * a
if d > 0:
  print("There are two roots")
  print(r1,r2)
elif d == 0:
  print("There is one real root")
  print(r1)
elif d <0:
  print("These are complex root")
  print(r1,r2)