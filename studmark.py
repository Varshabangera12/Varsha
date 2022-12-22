
Name=input("Enter the name: ")
Age=input("Enter the age: ")
Phno=input("Enter the phone number: ")
Mark1=float(input("Enter marks of first subject: "))
Mark2=float(input("Enter marks of second subject: "))
Mark3=float(input("Enter marks of third subject: "))
Mark4=float(input("Enter marks of fourth subject: "))
Mark5=float(input("Enter marks of fifth subject: "))
if Mark1 > 10 :
 print("Error! Greid point cannot be greater than 10 ")
if Mark2 > 10 :
 print("Error! Greid point cannot be greater than 10 ")
if Mark3 > 10 :
 print("Error! Greid point cannot be greater than 10 ")
if Mark4 > 10 :
 print("Error! Greid point cannot be greater than 10 ")
if Mark5 > 10 :
 print("Error! Greid point cannot be greater than 10 ")
 exit()
 
Total=Mark1+Mark2+Mark3+Mark4+Mark5
Average=Total/5
print("Name="+Name)
print("Age="+Age)
print("Phno="+Phno)
print("Marks1="+str(Mark1))
print("Marks2="+str(Mark2))
print("Marks3="+str(Mark3))
print("Marks4="+str(Mark4))
print("Marks5="+str(Mark5))
print("Total Marks="+str(Total))
print("Average Marks="+str(Average))
