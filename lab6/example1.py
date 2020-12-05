email = "abc@example.com"
email_replace = email.replace(".","")
while True:
  x = input("PLEASE INSERT A EMAIL:")
  x_split = x.split("@")[1]
  x_replace = x.replace(".","")
  x_lower = x_replace.lower()
  if x_split[7:] == email[11:]:
    if  x_lower == email_replace:
      print("Welcome")
      break
    else:
      print("Wrong")
  else:
    print("Wrong")


  
