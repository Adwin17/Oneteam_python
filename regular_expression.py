import re
'''
s="I love  7 Pyth1234on"

m=re.search(r"love",s)
print(m)

k=re.findall("ve",s)
print(k)

# \d for taking digits individually 
p=re.findall(r"\d",s)
print(p)
# \d+ for taking digits together like they exist
q=re.findall(r"\d+",s)
print(q)

# \w for taking letters individually 
m=re.findall(r"[a-zA-Z]+",s)
print(m)

'''
pattern=r'^[a-zA-Z0-9%+-._]+@[a-zA-Z0-9.-]+\.[a-z]{2,}'

email='adwin@gmail.com'

k=re.fullmatch(pattern,email)


