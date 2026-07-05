# Transpose a matrix
'''
matrix=[]
n=int(input("Enter the no. of rows"))
m=int(input("Enter the no. columns"))

for i in range(n):
    row=[]
    for j in range (m):
        x=int(input("Enter the matrix element:"))
        row.append(x)
    matrix.append(row)

print("Matrix :",matrix)

transpose=[]
for i in range (m):
    row1=[]
    for j in range(n):
        row1.append(matrix[j][i])
    transpose.append(row1)

print("Transpose Matrix :",transpose)

'''


# Print by youngest to oldest
'''
d={"Ravi":24,"Priya":19,"Aman":27,"Neha":22,"Kiran":20}

while len(d)>0:
    n=200
    m=''
    for i in d:
        if d[i]<n:
             n=d[i]
             m=i
             
    print(m,n)
    d.pop(m)
'''
# print prime no. in pattern
'''
def is_prime(x):
    q=0
    for i in range(2,x//2+1):
        if x%i==0:
            q=1
            break
    if q==1:
        return False
    else:
        return True
    
n=int(input("Enter the no. of rows"))
num=2
for i in range (1,n+1):
    m=0
    while m<i:
        if is_prime(num):
            print(num,end=" ")
            m+=1
        num+=1
        
    print()
'''


#BMI calculator 

def calculate_bmi():
   
    try:
        w=int(input("Enter the weight in kg"))
        h=float(input("Enter the height in m"))
        b={18.5:"Underweight",24.9:"Normal Weight",29.9:"Overweight"}

        if w and h >0:
            bmi=w//(h**2)
            for i in b:
                if  bmi<=i:
                    
                    return bmi,b[i]
                else:
                    return bmi,"obese"
        else:
            print("Invalid Input")
    except Exception as e:
        return ("Error occured",e)
    
    

    
        
        
print(calculate_bmi())






        
    






