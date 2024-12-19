k0=int(input("Enter amount: "))
intrest_rate=float(input("Enetr intrest rate: "))
n=int(input("Enter number of years: "))
k1=k0
while n>0:
    k1=k1+(k1*intrest_rate)
    n-=1
print("new captial after ",n,"years is : ",k1)