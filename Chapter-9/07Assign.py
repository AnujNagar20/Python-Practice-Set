
content=True
i=1

with open("log.txt") as f:
      while content:
            content=f.readline()
            if "python" in content:
                  print(f"yes python present in log file and it is present in {i}")
            i=i+1      