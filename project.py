

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
       
        D=D+[d]
        k=input("To add more press 'y' ")

    return D

def result(D):
    t=0
    result=[]
    for i in D:
        if i["Total Marks"]>t:
            t=i["Total Marks"]
            if result==[]:
                result=[i["Name"]]
            else:
                result[0]=[i["Name"]]
        elif i["Total Marks"]==t:
            result=result+[i["Name"]]
            
    for i in result:
        print(i,"\nSecured First")
    
def search_name():
    name=input("Enter the name :")
    for i in D:
        if i["Name"]==name:
            print(i)

def search_grade():
    grade=input("Enter the grade to search:")
    for i in D:
        if i["Grade"]==grade:
            print(i)





    
D=[]
print('\n== Welcome to the Student Progress Portal ==')
while True:
    print("\n1.Student Entry\n2.View Student Records\n3.View Rank Holder\n4.Search for a particular student\n5.Exit")
    choice=int(input("\nEnter the choice:"))
    match choice:
        case 1:
            D=reg(D)
            print("\nData Stored Successfully!")
        case 2:
            if D==[]:
                print("\nRecords Empty")
            else:
                for i in D:
                    print(i)
        case 3:
            if D==[]:
                print("\nRecords Empty")
            else:
                result(D)
        case 4:
            print("\n1.Search with name\n2.Search with Grade [A+,A,B,C,D,E]")
            k=int(input("Enter your choice:"))
            if D==[]:
                print("\nRecords Empty")
            else:
                if k==1:
                    search_name()
                if k==2:
                    search_grade()

        case 5:
            print("\nThank You!")
            break






