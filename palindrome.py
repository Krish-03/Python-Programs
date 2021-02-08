num = int(input("Enter a number:"))
n=num
res=0
while num>0:
    rem=num%10
    res=rem+res*10
    num=num//10
if res==n:
    print("Number is a Palindrome")
else:
    print("Number is not a Palindrome")
