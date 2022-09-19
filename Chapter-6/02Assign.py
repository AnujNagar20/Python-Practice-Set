marks1=float(input("Enter your marks in first subject : "))
marks2=float(input("Enter your marks in secpnd subject : "))
marks3=float(input("Enter your marks in third subject : "))                   
if(marks1<33 or marks2<33 or marks3<33):
      print("you fail due to less marks from 33")
elif((marks1+marks2+marks3)/3 < 40):   
      print("You fail due to lass percentage below 40")
else:
      print("Congradulation you pass this exam")