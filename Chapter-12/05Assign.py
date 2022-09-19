num=int(input("Enter a number: "))
b=[num*i for i in range(1,11)]
print(b)
with open("table.txt","a") as f:
      f.write(str(b))
      f.write("\n")