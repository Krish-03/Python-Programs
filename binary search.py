def bsearch(ar,item):
    beg=0
    last=len(ar)-1
    while (beg<=last):
        mid=(beg+last)//2
        if(item == ar[mid]):
            return mid
        elif (item > ar[mid]):
            beg=mid+1
        elif (item<ar[mid]):
            last=mid-1
        else:
            return False
n=int(input("Enter desired linear list size:"))
print("Enter elements for linear list in ASCENDING Order:\n")
ar=[0]*n
for i in range(n):
      ar[i]=int(input("element"+str(i)+":"))
item=int(input("\nEnter element to be searched for..."))
index=bsearch(ar,item)
if index:
      print("\nElement fount at index:" ,index, ",position:", (index+1))
else:
    print("\nsorry! Given element could not be found.\n")
