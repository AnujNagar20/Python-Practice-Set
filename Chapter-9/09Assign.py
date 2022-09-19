with open("this.txt") as f:
      f1=f.read()

with open("copy.txt") as f:
      f2=f.read()

if (f1==f2):
      print("The files are identical")
else:
      print("The files are not identical")
