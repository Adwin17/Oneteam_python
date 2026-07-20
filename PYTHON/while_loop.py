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
# print the fruits starting with vowel
'''
L=['Apple','Orange','Watermelon','Banana']
for i in L:
    if i[0] in 'aeiouAEIOU':
        print(i)
'''
#list slicing
'''
L=[25,45,1,2,3,6]
print(L[1:3])
'''
#character count from string
'''
x=input("Enter the string:")
d={}
for i in x:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

for j in d:
    # print(j,d[j])
    print(f"{j} = {d[j]} ")
'''
#sorting numbers without builtin
'''
numbers=[19,2,1,23,8]
n=len(numbers) #to find the length of given list -->5
for k in range(n-1): #Index position dtarts from 0 so range is 5-1-->4
    for v in range(n-k-1):  
        if numbers[v]>numbers[v+1]:
            numbers[v],numbers[v+1]=numbers[v+1],numbers[v]
print(numbers)   
'''
'''
l=[]
n=int(input("Enter how many numbers to be entered:"))
for i in range(n):
    m=int(input("Enter the number:"))
    l=l+[m]
n=len(l)
for i in range(n-1):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
'''




