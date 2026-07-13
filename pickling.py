import pickle
l=[1,2,3,4,5,6,7]
d={"Name":"Adwin","Age":18,"Place":"Kochi"}
with open("Binary File.pkl","wb") as f:
    pickle.dump([d,l],f)
    # pickle.dump(l,f)

with open("Binary File.pkl","rb") as f:
    for  i in pickle.load(f):
        print(i)
    


