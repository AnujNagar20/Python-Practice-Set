class Person():
      name="anuj"
      roll=35
      def __init__(self):
            self.company="google"
            print("hello")
      def show(self):
            print("hii")      
class Employee(Person):  
      def greek(self):        
            print("subodh")
          #  print(f"{self.roll}")
class Baby(Employee):
      def own(self):
            print(f"{self.roll}")            
b=Baby()
b.own()

