def hollow_square(n):
    for i in range(1,n+1):
        k=1
        while k<=n:
            print("*",end="")
            k+=1

# hollow_square(5)

# To print first n prime numbers
def is_prime(k):
    p=True
    for i in range(2,k//2+1):
        if k%i==0:
            p=False
            break
    if p:
        return True
    else:
        return False
        
def no_prime(n):
    x=0
    num=2
    while x<n:
        
        if is_prime(num):
            print(num,end=" ")
            
            x+=1
        num+=1
           
# no_prime(10)

# Calculate Factorial
def factorial(n):
    x=1
    for i in range(1,n+1):
        x=x*i
    print(x)

    # if n==1:
    #     return n
    # else:
    #     return n*(factorial(n-1))


# factorial(6)

# Character Frequency Coumter
def counter(s):
    d={}
    sn=s.strip().lower()
    for i in sn:
        if i not in d:
            d[i]=sn.count(i)
    print(d)
    for i in d:
        print(f"{i} : {d[i]}")
    
# counter("  PrograMming")

def is_anagram(s,t):
    x,y=list(s.lower()),list(t.lower())
    if len(x)==len(y):
        a=True
        for i in x:
            if  i in y:
                y.remove(i)
            else:
                a=False
        if a:
            print("Anagram")
        else:
            print("Not Angram")
    else:
            print("Not Angram")
        
    
# is_anagram("cat","AcT")

#to print the perfect numbers 
def perfect(n):
    l=[]
    x=0
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    for j in l:
            x=x+int(j)
    if x==n:
        return True
    
    # if x==n:
    #         print(n,"Perfect Number")
    # else:
    #     print("Not Perfect Number")

# perfect(828)
def print_perfect(t): 
    first=1
    while first !=t:
        if perfect(first):
            print(first)
        first+=1


# t=int(input("Enter the number till you want to print:")) 
# print_perfect(t)

stock = {"Laptop": 23,"Mouse": 12,"Monitor": 3,"Keyboard": 15,"Printer": 5}


def name_sort(stock):
    s=sorted(stock,key=lambda j:j)
    for i in s:
        print(f"{i} : {stock[i]}")

def qty_sort(stock):
    s=sorted(stock,key=lambda j:stock[j])
    for i in s:
        print(f"{i} : {stock[i]}")

def qty_sortreverse(stock):
    s=sorted(stock,key=lambda j:stock[j],reverse=True)
    for i in s:
        print(f"{i} : {stock[i]}")
def less(stock):
    for i in stock:
        if stock[i]<10:
            print(i)

# name_sort(stock)
# qty_sort(stock)
# qty_sortreverse(stock)
# less(stock)

class Product:
    def __init__(self,id,name,price,stock):
        self.id=id
        self.name=name
        self.price=price
        self.stock=stock

    def add_stock(self,newstock):
        self.stock=self.stock+newstock

    def reduce_stock(self,reduce):
        if self.stock>=reduce:
            self.stock=self.stock-reduce
        else:
            print("Stock is less than you entered ")

    def display_product(self):
        print(f"ID={self.id} Name={self.name} Price={self.price} Stock={self.stock}")

# p1=Product(1,"Notebook",10,10)
# p1.add_stock(50)
# p1.reduce_stock(20)
# p1.display_product()

def dup(st):
    l=st.split()
    print(l)
    d=[]
    for i in l:
        if l.count(i)>1 and i not in d:
            print(i)
            d.append(i)

# dup("Python is easy and Python is powerful")

def sec_large():
    c=1
    l=[]
    while c<6:
        n=int(input(f"{c}. Enter the number"))
        l.append(n)
        c+=1

    a=0
    b=0
    for i in l:
        if i>a:
            b=a
            a=i
        elif i>b:
            b=i
    print(f"Second Largest number is {b}")


# sec_large()

def matrx_add():
    n=[]
    m=[]
    new=[]
    print("For the first matrix")
    for i in range (1,4):
        l=[]
        print(f"For row {i}")
        for j in range(1,4):
            s=int(input(f"Enter the {j} element: "))
            l.append(s)
        n.append(l)
    print("for the second matrix")
    for i in range (1,4):
        l=[]
        print(f"For row {i}")
        for j in range(1,4):
            s=int(input(f"Enter the {j} element: "))
            l.append(s)
        m.append(l)
    for w in range(3):
        row=[]
        for x in range(3):
            row.append(n[w][x]+m[w][x])
        new.append(row)

    print("The Final Matrix is :")
    for i in new:
        print(i)
    
# matrx_add()
    

        









        

        
