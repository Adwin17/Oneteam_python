

def reg(D):
    k='y'
    while k=='y':
        d={}
        n=input("Enter the name of the student:")
        cl=input("Enter the Class :")
        p=int(input("Enter the marks for physics:"))
        c=int(input("Enter the marks for chemistry:"))
        m=int(input("Enter the marks for maths:"))
        total=p+c+m
        d["Name"]=n
        d["Class"]=cl
        d["Total Marks"]=total
        d["Percentage"]=total/3
        if total/3>=90:
            d["Grade"]='A+'
        elif total/3>=80:
            d["Grade"]='A'
        elif total/3>=70:
            d["Grade"]='B'
        elif total/3>=60:
            d["Grade"]='C'
        elif total/3>=50:
            d["Grade"]='D'
        else:
            d["Grade"]='E'
       
        # D=D+[d]
        D.append(d)
        k=input("To add more press 'y' ").lower()

    return D

def view(D):
    print("\n======== Student Records ======")
    for i in D:
        print(f"Name : {i["Name"]}        Class:{i["Class"]}")
        print(f"Total Marks: {i["Total Marks"]}      Percentage:{i["Percentage"]}    Grade:{i['Grade']}")

def result(D):
    r1,r2,r3=-1,-1,-1
    rank1,rank2,rank3=[],[],[]
    
    for i in D:
        mark=i["Total Marks"]
        name=i["Name"]
        if mark>r1:
            r3=r2
            rank3=rank2
            r2=r1
            rank2=rank1
            r1=mark
            rank1=[name]
        elif mark==r1:
            rank1.append(name)
        elif mark>r2:
            r3=r2
            rank3=rank2
            r2=mark
            rank2=[name]
        elif mark == r2:
            rank2.append(name)
        elif mark>r3:
            r3 = mark
            rank3=[name]
        elif mark== r3:
            rank3.append(name)
    
            
    print("\n=======Student Leaderboard=======")
    if r1 != -1:
        for j in range(len(rank1)):
            if j>0:
                print(", ",end="")
            print(rank1[j],end=" ")
        print(f"secured 1st rank with {r1} marks")
        
    if r2 != -1:
        for j in range(len(rank2)):
            if j>0:
                print(", ",end="")
            print(rank2[j],end=" ")
        print(f"secured 2nd rank with {r2} marks")
        
    if r3 != -1:
        for j in range(len(rank3)):
            if j>0:
                print(", ",end="")
            print(rank3[j],end=" ")
        print(f"secured 3rd rank with {r3} marks")

    
def search_name(D):
    name=input("Enter the name :")
    x=0
    for i in D:
        if i["Name"].lower()==name.lower():
             print(f"Name : {i["Name"]}      Class:{i["Class"]}")
             print(f"Total Marks: {i["Total Marks"]}    Percentage:{i["Percentage"]}    Grade:{i['Grade']}")
             x=1
             continue
             
        
    if x==0:
        print("Name not found")


def search_grade(D):
    grade=input("Enter the grade to search:")
    y=1
    for i in D:
        if i["Grade"].lower()==grade.lower():
             print(f"Name : {i["Name"]}      Class:{i["Class"]}")
             print(f"Total Marks: {i["Total Marks"]}    Percentage:{i["Percentage"]}    Grade:{i['Grade']}")
             y=0
             
    if y==1:
        print(" Entered Invalid Grade or Grade not found")
            






    
D=[]
print('\n============ Welcome to the Student Progress Portal ============')
while True:
    print("\n1.Student Entry\n2.View Student Records\n3.Leaderboard\n4.Search for a particular student\n5.Exit")
    choice=int(input("\nEnter the choice:"))
    match choice:
        case 1:
            D=reg(D)
            print("\nData Stored Successfully!")
        case 2:
            if D==[]:
                print("\nRecords Empty")
            else:
                view(D)
        case 3:
            if D==[]:
                print("\nRecords Empty")
            else:
                result(D)
        case 4:
            if D==[]:
                print("\nRecords Empty")
            else:
                while True:
                    print("\n1.Search with name\n2.Search with Grade [A+,A,B,C,D,E]\n3.Back to main menu")
                    k=int(input("Enter your choice:"))
                    if k==1:
                        search_name(D)
                    elif k==2:
                        search_grade(D)
                    elif k==3:
                        break
                    else:
                        print("Invalid Input !")
                        

                

        case 5:
            print("\nThank You!")
            break
        case _:
            print("\nInvalid Input !")






