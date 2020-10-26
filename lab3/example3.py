gpa_user = float(input("Please enter the Gpa:"))
lecture_user = int(input("PLease enter the number of lectures: "))

if lecture_user < 47 and gpa_user < 2.0:
  print("Not enough number of lectures and gpa!")
elif  lecture_user < 47 and gpa_user >= 2.0:
  print("Not enough number of lectuures")
elif lecture_user >= 47 and gpa_user < 2.0:
  print("Not enough GPA!")
else:
  print("GRADUATED!!")