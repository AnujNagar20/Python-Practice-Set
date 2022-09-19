class Programmer():
      company="microsoft"
      def __init__(slf, name, product) :
          slf.name = name
          slf.product = product
      def getInfo(slf):
            print(f"The name of the programmer is {slf.name} and product is {slf.product}")    
harry = Programmer("harry","skype")            
anuj = Programmer("anuj","GitHub")
harry.getInfo()
anuj.getInfo()