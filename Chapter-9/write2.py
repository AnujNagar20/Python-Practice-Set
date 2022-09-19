from asyncore import write


f=open('another.txt','w')
d=f.write("sachin is a good player")
print(d)
f.close()