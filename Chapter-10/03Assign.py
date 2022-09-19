class Company():
      a="google"
      print(f"hello {a}")
cal=Company()      
print(cal.a)
print(Company.a)
cal.a="microsoft"
print(cal.a)
print(Company.a)
Company.a="samsung"
print(cal.a)
print(Company.a)
red=Company()

