def prime(n):
    if n <= 1:
        print("Not a prime nor composite number")
        return
    elif n == 2:
        print("Prime number")
        return
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not a prime number")
            return
    print("Prime number")

n = int(input("Enter a number: "))
prime(n)
