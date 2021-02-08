p=float(input("Enter the principal amount:"))
r=float(input("Enter the rate if interest:"))
t=float(input("Enter the time in years:"))
x=(1+r/100)**t
CI=p*x-p
print("Compound Interest is:",round(CI,2))
