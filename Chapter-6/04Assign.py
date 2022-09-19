name=input("Enter your name : ")
if(len(name)<10):
      print("Your name contains less than 10 characters")
elif(len(name)==10):
      print("Your name contains exactly 10 characters")   
else:
      print("Your name contains greater than 10 characters")