x = list(input("Please enter the number: "))
y = int(x[len(x) - 1]) + int(x[len(x) - 2])
if y <= 10:
  y = "0" + str(y)
  print(y)
else:
  print(y)



