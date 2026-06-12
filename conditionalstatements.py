# to check whther the no. is even
"""
n= int(input("Enter the number"))
if n%2==0:
    print("Number is even")
else:
    print("Number is odd")
"""
a=int(input("Enter the first number:"))
b=int(input("Enter the Second number:"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
choice=int(input("Enter the choice:"))
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    print(a*b)
elif choice==4:
    print(a//b)
else:
    print("invalid input")

