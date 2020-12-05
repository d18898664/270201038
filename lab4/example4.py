x = int(input("Please enter the base number: "))
y = int(input("Please enter the power number: "))
total = 1

for i in range(y):
  total *= x
print(total)