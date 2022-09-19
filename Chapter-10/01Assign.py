from itertools import product
from unicodedata import name


class Programmer():
      company="microsoft"
      def __init__(self, name, product) :
          self.name = name
          self.product = product
      def getInfo(self):
            print(f"The name of the programmer is {self.name} and product is {self.product}")    
harry = Programmer("harry","skype")            
anuj = Programmer("anuj","GitHub")
harry.getInfo()
anuj.getInfo()


