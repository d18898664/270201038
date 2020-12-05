counter = 0
total = [[],[],[]]
student = list()
grade = list()
result_list = list()
a = int(input("How many students are:"))

while counter < a:
  m1 = int(input("Enter the first midterm point:"))
  total[0] = m1
  m2 = int(input("Enter the second midterm point:"))
  total[1] = m2
  f1 = int(input("Enter the final point:"))
  total[2] = f1
  x = list(total)
  student.append(x)
  result = (m1 * 30) / 100 + (m2 * 30) / 100 + (f1 * 40 / 100)
  result_list.append(result)
  print("Student Notes",student[counter],"Grades",result_list[counter])
  counter = counter + 1
  total.clear
  #30 min