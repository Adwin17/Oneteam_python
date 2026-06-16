'''
for i in "python":
    print(i)
x=['Oneteam','Kochi',['edapally',96]]
for i in x:
    print(i)
for j in {'name':'adwin','age':18}:
    print(j)
for k in ("oneteam",96,5):
    print(k)
for l in {96,5,6}:
    print(l)
'''

'''
for i in range(10,-2):
    print(i) 
'''
# to print the factorial of a number
'''
num=int(input("Enter the number to find the factorial:"))
x=1
for i in range(1,num+1):
    x=x*i
print(f"The factorial of {num} is {x}")
'''
# to print the even numbers from the list
'''
numbers=[45,12,23,4,8,34]
for i in numbers:
    if i%2==0:
        print(i)
'''
# to add a number to the list using concatenation
'''
x=int(input("Enter how many numbers to be added to the list:"))
l=[]
for i in range(x):
    n=int(input("Enter the number:"))
    l=l+[n]
print(l)
'''

#fibanocci series
'''
x=0
y=1
print(x,y,end=" ")

for i in range(0,8):
    z=x+y
    print(z,end=" ")
    x,y=y,z
''' 


#multiplication table
'''
n= int(input("Enter the number to print the multiplication table : "))
for i in range(1,11):
    m=n*i
    print(f"{n} x {i} = {m} ")
'''


