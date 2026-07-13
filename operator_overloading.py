class Numbers:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def __add__(self,other):
        return (self.num1+other.num1,self.num2+other.num2 )
    
o1=Numbers(10,5)
o2=Numbers(2,5)
print(o1+o2)