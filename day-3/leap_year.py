def leap(n):
    if n<0:
        return "enter valid number"
    else:
        if (n%4==0 and n%100!=0) or (n%400==0):
            print(" leap year")
        else:
            print("non_leap year")
n=int(input("enter the year: "))
leap(n)