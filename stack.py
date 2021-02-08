def push():
    a=int(input("Enter the element which you want to push:"))
    stack.append(a)
    return a
def POP():
    if stack==[]:
        print("Stack empty...underflow case...can not deleted the element")
    else:
        print("deleted element is",stack.pop())
def display():
    if stack==[]:
        print("stack is empty...no elements in stack...")
    else:
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])
stack=[]
print("STACK OPERATIONS")
print("*****************")
choice="y"
while choice=="y":
    print("l.PUSH")
    print("2.POP")
    print("3.DISPLAY ELEMENTS OF STACK")
    print("****************************")
    c=int(input("Enter your choice:"))
    if c==1:
        push()
    elif c==2:
        POP()
    elif c==3:
        display()
    else:
        print("Wrong input")
    choice=input("Do you want to continue or not?(y/n):")
