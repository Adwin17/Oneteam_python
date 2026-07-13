'''
f=open("Sample.txt","w")
f.write("Welcome to the new file")
f.close()
'''
'''
with open("Sample.txt","a") as f:
    f.write("\nNew line appended")
'''


with open("Sample.txt","r") as f:
    print(f.read())
