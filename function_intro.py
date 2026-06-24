'''
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
'''
# *args --> stores in a tuple
'''
def add(*args):
    print(args)
    x=0
    for i in args:
        x=x+int(i)
    print(x)

add(24,52,63,69)
'''
# keyword arguments
'''def greet(name,age,place="Kochi",course=None):
    print(f'Hello {name} you are {age} years old')
    print("You are from",place)
'''
# **kwargs --> Stores in a dictionary
'''
def greet(**kwargs):
    print(f"Hello {kwargs["name"]} you are {kwargs["age"]} years old")
    print("you are from",kwargs["place"])

greet(name="Ashwin",age=24,place='Kottayam')
'''

# return and recursion 
'''
def fact(n):
    if n==1:
        
        return n
    else:
        
        return n*fact(n-1)
print(fact(5))
'''
# lambda
add=lambda a,b :a+b
print(add(9,1))

even= lambda n : n%2==0
print(even(93))
