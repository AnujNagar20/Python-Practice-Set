mydict={
       "pankha": "fan",
       "dabba": "box",
       "vastu": "item",
}
print("Your options are ",mydict.keys(),"\n")
a=input("Enter the hindi word\n")
print("your english meaning is ",mydict.get(a))