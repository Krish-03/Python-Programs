def sumlist(items):
    sum=0
    for i in items:
        sum=sum+i
        return sum
lst=eval(input("Enter list items:"))
print("Sum of list items:",sumlist(lst))
