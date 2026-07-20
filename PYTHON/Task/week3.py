
def star_pattern(n):
    for i in range(1,n+1):
        print(" "*(n-i),"*"*(2*i-1))

def inverted(number):
    l=list(number)
    print(number)
    L=len(l)
    while L!=0:
        l.pop()
        for i in range (len(l)):
            print(l[i],end='')
        print()
        L-=1
def sum(n):
    
    if n==1:
        return 1
    return n +sum(n-1)







    

             

def app():
    while True:
        print("1. Print Pyramid Star Pattern\n2. Print Inverted Number Pattern\n3. Calculate Sum of First N Natural Numbers\n4. Calculate Power of a Number\n5. Exit")
    
        choice=int(input("Enter your choice :"))
        match choice:
            case 1:
                n=int(input("Enter the no. of rows"))
                star_pattern(n)
            case 2:
                number=input("Enter the number :")
                inverted(number)
            case 3:
                while True:
                    n=int(input("Enter the number to which the sum is to be calculated :"))
                    if n<=0:
                        print("Please Enter a natural number")
                    else:
                        print(f"The sum of first {n} numbers is {sum(n)}")
                        break
            case 4:
                n=int(input("Enter the number to find the power :"))
                x=int(input("Enter the power :"))
                power= lambda n,x:n**x
                print(f"{n} to the power of {x} is {power(n,x)}")
            case 5:
                print("Thank You ,have a good day !")
                break
            case _:
                print("Invalid Input!")




        
app()
