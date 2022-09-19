from asyncore import read


with open('twinkle.txt','r') as f:
      a=f.read()
if 'twinkle' in a:
      print("Twinkle is preent in your text")
else:
      print("Twinkle is not preent in your text")
            