class V2d():
      def __init__(self,i,j):
            self.i=i
            self.j=j
      def show1(self):
            print(f"{self.i}i+{self.j}j")    
class V3d(V2d):
      def show2(self,k):
            print(f"{self.i}i+{self.j}j+{k}k")
e=V2d(2,5)            
e.show1()
p=V3d(16,4)

p.show2(6)
