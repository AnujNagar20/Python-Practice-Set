try:
      a=int(input("Enter a number : "))
      print("Hello")
      c=1/a
      print(c)
except ValueError as e:
      print(f"Value Error")   
except ZeroDivisionError as e:
      print(f"Zero division error")   
except Exception as e:
      print(f"Invalid number entered {e}")    
       
print("Anuj") 