import random
while(True):
    choice=input("Enter 'r' to roll dice or press any other key to quit")
    if (choice!='r'):
        break
    n=random.randint(1,6)
    print(n)
    
