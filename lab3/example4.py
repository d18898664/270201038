age_user = int(input("Please enter your age: "))
normal_ticket_price = 3
discount_price = 3 * 0.5
if age_user > 60 or age_user < 6:
  print("You can go free!")
elif age_user >= 6 and age_user <= 18:
  print("You can go if you pay: ",(normal_ticket_price * 0.5))
else:
  print("You can go if you pay: ",normal_ticket_price)
