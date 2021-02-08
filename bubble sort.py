def bubble():
    a=[]
    number=int(input("Please enter the total number of elements:"))
    for i in range(number):
        value=int(input("Please enter the element of list1:"))
        a.append(value)
        for i in range(number-1):
            for j in range(number-i-1):
                if (a[j]>a[j+1]):
                    temp=a[j]
                    a[j]=a[j+1]
                    print("The sorted list in ascending order:",a)
bubble()
