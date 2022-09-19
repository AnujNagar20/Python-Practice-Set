from sre_constants import FAILURE
from sys import set_asyncgen_hooks
from traceback import FrameSummary
from unicodedata import name


class Train():
      def __init__(self,name,fare,seats):
            self.name=name
            self.fare= fare
            self.seats= seats

      def get(self):
            print(f"The name of train is {self.name}")      
            print(f"The no. of seats in train is {self.seats}")  

      def fareInfo(self):      
            print(f"the price of ticket is {self.fare}")

      def book(self):
            if (self.seats>0):
                  print("CONGRADULATION, your seats has been booked")  
                  self.seats=self.seats-1 
                  print(f"The reamining seats is {self.seats}")
            else:
                  print("Sorry the train has been fully booked")     
                  
rajdhani=Train("rajdhani",50,300)            
rajdhani.get()
rajdhani.fareInfo()
rajdhani.book()

