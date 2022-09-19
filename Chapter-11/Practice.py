class Employee():
      name="anuj"
      def __init__(self):
            self.roll=35
      def show(self):
            p=55648
            print(self.name, self.roll , p)
e=Employee()  
print(Employee.name)
#print(Employee.roll)
e.show()          
print(e.name)
print(e.roll)
e.name="subodh"
e.roll=10
print(e.name)
print(e.roll)
e.show()
Employee.name="rahul"
print(Employee.name)
e.show()

