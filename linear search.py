#linear search function
def lsearch():
    l=eval(input('enter the element:'))
    n=len(l)
    a=eval(input('enter the element that you want to search :'))
    for i in range(n):
        if l[i]==a:
            print('Required element found at index',i+1)
            break
        else:
            print('search not found')
lsearch()
