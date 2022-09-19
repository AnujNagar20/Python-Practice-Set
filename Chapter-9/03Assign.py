for i in range (2,21):
      with open(f"Table/Multiplication of {i}.txt",'w') as f:
            for j in range(1,11):
                  f.write(f"{i}X{j}= {i*j}")
            break  