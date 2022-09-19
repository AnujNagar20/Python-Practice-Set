class Employee():
      name="anuj"
      roll=35

      @classmethod
      def show(cls,v):
            cls.roll=v
e=Employee()            
print(e.roll)
print(Employee.roll)
e.show(10000)
print(e.roll)
print(Employee.roll)