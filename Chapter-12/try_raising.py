
def show(num):
      try:
            return int(num)+1
      except:
            raise ValueError("PLEASE ENTER A VALID NUMBER")      
a=show(564)            
print(a)
            