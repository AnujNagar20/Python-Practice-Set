class Calculator():
      def __init__(self,num):
            self.number= num
      def square(self):
            print(f"The square of {self.number} is {self.number**2}")      

      def cube(self):
            print(f"The cube of {self.number} is {self.number**3}")  

      def squareroot(self):
            print(f"The squareroot of {self.number} is {self.number**0.5}") 
      @staticmethod
      def greet():
            print("Hello")
cal=Calculator(9)              
cal.square()
cal.cube()
cal.squareroot()
cal.greet()