number_counter = 0
even_counter = 0
a = int(input("How many integers?:"))

while number_counter < a:
  sayi = int(input("Enter the number:"))
  if sayi % 2 == 0:
    even_counter = even_counter + 1
  number_counter = number_counter + 1
x = ((100 * even_counter) / number_counter)
print("%",x)
