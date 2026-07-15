
numbers=[1,2,3,4,5,6]

n=list(map(lambda x:x*2,numbers))
print(n)

m=list(filter(lambda x:x%2==0,numbers))
print(m)

from functools import reduce

total=reduce(lambda a,b:a+b,numbers)
print(total)

k=reduce(lambda a,b:a*b, range(1,6))
print(k) 