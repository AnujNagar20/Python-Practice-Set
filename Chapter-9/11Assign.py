import os

with open("sample.txt") as f:
      content=f.read()
with open("removed_by_python.txt",'w') as f:   
        f.write(content)

os.remove("sample.txt")        