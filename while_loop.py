# factorial
'''
n=int(input("Enter the number to find the factorial:"))
x=1
num=1
while x<=n:
    num=x*num
    x+=1
print(f"The factorial of {n} is {num}")
'''
# fibanocci
'''
x,y=0,1
z=0
print(x,y,end=' ')
k=1
while k<=9:
    z=x+y
    print(z,end=' ')
    x,y=y,z
    k+=1
'''

# calculator loop
'''
x="yes"
while x=="yes":

    a=int(input("Enter the first number:"))
    b=int(input("Enter the Second number:"))
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
    choice=int(input("Enter the choice:"))
    match choice:
        case 1:
            print(f"{a} + {b} ={a+b}")
        case 2:
            print(f"{a} - {b} ={a-b}")
        case 3:
            print(f"{a} * {b} ={a*b}")
        case 4:
            print(f"{a} / {b} ={a/b}")
    x=input("Do you wish to continue ? (yes/no)")
else:
    print("Exiting...")
'''
L=['Apple','Orange','Watermelon','Banana']
for i in L:
    if i[0] in 'aeiouAEIOU':
        print(i)
