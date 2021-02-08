ch=input("Enter a character:")
if ch.isalpha():
    print(ch,"is an alphabet")
elif ch.isdigit():
    print(ch,"is a digit")
elif ch.isalnum():
    print(ch,"is alphabet and numeric")
else:
    print(ch,"is a special symbol")
