'''
l=[12,"Python",7,["Oneteam",12,"Kochi"],34.12]

l.append("Java")
l.insert(3,["Metro",96])
l.pop(-1)
l.remove("Python")
l.clear()
print(l.index(['Oneteam',12,'Kochi']))
l.extend(["Java",85,52])
print(l)

str="Python is a snake in Forest"
st="Pyhton is a language"
print(str.lower())
print(str.upper())
s=str.split()

print("=".join(str))
print(str.strip("o"))
'''

n=input("Enter the 1st string :")
m=input("Enter the 2nd String :")

l1=list(n)
l2=list(m)

if len(l1)==len(l2):
    x=1
    for i in l1:
        if i in l2:
            x=1 
            l2.remove(i)
         
        else:
            x=0
            break
            
               
    if x==0:
        print(" The words are not anagram")
    else:
        print("The words are anagram")
else:
    print("The words are not anagram")