with open('Donkey.txt','r') as f:
      a=f.read()
b=a.replace("Donkey","#####")      
with open('Donkey.txt','w') as f:
      f.write(b)
      