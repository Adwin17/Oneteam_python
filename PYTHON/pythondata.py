'''
List=["oneteam",96,72,1.3]


num=963

Float=7.45

Complex=7j

D={"Oneteam":"Kochi","Ernakulam":783}
print(D.items())

Tuple=("Oneteam",963,7)

Set={"Oneteam",785,"Kochi"}
'''
String="Oneteam is at Kochi , Edappaly"
s="*",'9'
print(String.split("K"))
print(String)

def show_profile(**kwargs):
    # kwargs behaves like a dictionary inside the function
    for i,j in kwargs.items():
        print(kwargs)
        print(f"{i}: {j}")

show_profile(Name="Adwin",Age=18,Place="Kochi")
