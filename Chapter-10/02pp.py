class Calculator():
      def __init__(self,n):
            self.num=n
      def square(self):
            print(f"The square of {self.num} is {self.num**2}") 
      def cube(self):
            print(f"The cube of {self.num} is {self.num**3}") 
      def squareroot(self):
            print(f"The squareroot of {self.num} is {self.num**0.5}") 
      @staticmethod
      def greet():
            print("Hello user")      
give=Calculator(int(input("Enter a number")))
give.square() 
give.cube() 
give.squareroot()       
give.greet()      




