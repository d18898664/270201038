matching_counter = 0
counter = 0
x = (input("ENTER THE first NUMBER:"))
y = (input("ENTER THE second NUMBER:"))
liste1 = list(x)
liste2 = list(y)
liste1.reverse()
liste2.reverse()

while counter < len(liste1) and counter < len(liste2):
  if(liste1[counter]) == (liste2[counter]):
    matching_counter = matching_counter + 1
  counter = counter + 1
print(matching_counter)

  
