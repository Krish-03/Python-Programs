def insertion_sort(sort_list):
    for i in range(1,len(sort_list)):
        key=sort_list[i]
        j=i-1
        while j>=0 and key<sort_list[j]:
            sort_list[j+1]=sort_list[j]
            j-=1
            sort_list[j+1]=key
            print('\n The sorted list:\t',sort_list)
            print('\n')
lst=[]
size=int(input("\n Enter the size of list: \t"))
for i in range(size):
    element=int(input("Enter the element: \t"))
    lst.append(element)
insertion_sort(lst)
