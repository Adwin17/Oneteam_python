
# Write a program to find the sum of digits of a given number until the sum become a single digit number
n=int(input("Enter the number:"))
if n>9:
    while n>9:
        x=0
        for i in list(str(n)):
            x=x+int(i)
            n=x
    print(n)
else:
    print("The number entered is a single digit number:")

# Write a program to print 1st n Fibonacci numbers using a recursive function
def fib():
    n=int(input("Enter how many number of fibanocci numbers to be printed:"))
    a=0
    b=1
    print(a,b,end=' ')
    for i in range(0,n-2):
        c=a+b
        print(c,end=' ')
        a,b=b,c

fib()




