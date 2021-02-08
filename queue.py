Queue=[]
choice="y"
while choice=="y":
    print("l.INSERT")
    print("2.DELETE")
    print("3.DISPLAY ELEMENTS OF QUEUE")
    c=int(input("Enter your choice:"))
    if c==1:
        a=int(input("Enter the element that you want to push:"))
        Queue.append(a)
    elif c==2:
        if Queue==[]:
            print("Queue is empty... Underflow case...cannot delete the element")
        else:
            print("Deleted element is",Queue.pop(0))
    elif c==3:
        for i in range(len(Queue)):
            print(Queue[i])
    else:
        print("Wrong input")
    choice=input("Do you want to continue or not?(y/n):")
 
