# * pattern 
'''
for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print('')
'''
'''
for i in range(1,6):
    print('* '*i)
'''
'''
for i in range(4,-1,-1):
    print(' '*i,'*'*(5-i))
'''

'''
for i in range(1,5):
    n=1
    for j in range(1,i+1):
        print(i*n,end=' ')
        n+=1
    print()
'''
# to check whether a number is a prime number
'''
n=int(input("Enter the number:"))
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
'''

# list comprehension
"""
l=[x for x in range(10) if x%2==0]
print(l)
"""

# pyramid with star at odd and # at even postion
'''
for i in range(1,6):
    print(" "*(5-i),end="")
    for j in range(1,i*2):
        if j%2!=0:
            print("*",end="")
            
        if j%2==0:
            print("#",end="")
    print()
'''


        


