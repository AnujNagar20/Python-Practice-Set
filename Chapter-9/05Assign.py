list=["Donkey ","is","animal"]
with open('Donkey.txt','r') as f:
      a=f.read()
for word in list:
      b=a.replace(word,"$$$$")
      with open('Donkey.txt','w') as f:
            f.write(b)
