def divisible_by_5(num):
    if num%5==0:
        return True
    else:
        return False  
divisible_by_2=lambda x:x%2==0              
l=[1,2,25,625,11,44,45]
print(list(filter(divisible_by_5,l)))
print(list(filter(divisible_by_2,l)))