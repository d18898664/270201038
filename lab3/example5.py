January = 1
February = 2
March = 3
April = 4
May = 5 
June = 6
July = 7
August = 8
September = 9
October = 10
November = 11
December = 12


number_of_months = int(input("Enter the number of the month: "))
number_of_days = int(input("Enter the number of the day: "))
number_of_months <= 12 and number_of_months >= 1

if number_of_months == 12 or number_of_months <= 3:
  if number_of_months == 12 and number_of_days < 21:
    print("Fall")
  elif number_of_months == 3 and number_of_days >= 20:
    print("Spring")
  else:
    print("Winter")
elif number_of_months >= 3 and number_of_months <= 6:
  if number_of_months == 3 and number_of_days < 20:
    print("Winter")
  elif number_of_months == 6 and number_of_days <= 21:
    print("Summer")
  else:
    print("Spring")
elif number_of_months >= 6 and number_of_months <= 9:
  if number_of_months == 6 and number_of_days < 21:
    print("Spring")
  elif number_of_months == 9 and number_of_days <= 22:
    print("Fall")
  else:
    print("Summer")
elif number_of_months >= 9 and number_of_months <= 12:
  if number_of_months == 9 and number_of_days < 22:
    print("Spring")
  elif number_of_months == 12 and number_of_days <= 21:
    print("Winter")
  else:
    print("Fall")

