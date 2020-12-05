counter = 0
total = [[],[],[]]
student = list()
grade = list()
result_list = list()
a = int(input("How many students are:"))

while counter < a:
  m1 = int(input("Enter the first midterm point:"))
  
  m2 = int(input("Enter the second midterm point:"))
  
  f1 = int(input("Enter the final point:"))
 
  result = (m1 * 30) / 100 + (m2 * 30) / 100 + (f1 * 40 / 100)


  if result > 90:

    total[0] = m1
    total[1] = m2
    total[2] = f1
    x = list(total)
    student.append(x)
    result = (m1 * 30) / 100 + (m2 * 30) / 100 + (f1 * 40 / 100)
    result_list.append(result)
    print("Student Notes",student[counter],"Grades",result_list[counter])
  else:
    student.append("None")
    print("The student have not gotten AA point")
    result_list.append("None")
      
  counter = counter + 1
  total.clear

   
  