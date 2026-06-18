def prime(n):
    # n=int(input("Enter the number:"))

    x=0
    if n<=1:
        print(f"{n} is not  prime number")
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                x=1
        if x==1:
            print(f"{n} is not  prime number")
        else:
            print(f"{n} is a prime number")

prime(5)