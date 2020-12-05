password = "123456"
user_checker = input("Please enter the password:")
while user_checker != password or user_checker == "Help":
  
  if user_checker == "Help":
    print(password[0])
  else: 
    print("Wrong")
  user_checker = input("Please enter the password:")
    
 
print("Welcome")
