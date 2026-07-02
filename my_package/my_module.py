def calulator(a,b):
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
    choice=int(input("Enter the choice:"))
    match choice:
        case 1:
            print(a+b)
        case 2:
            print(a-b)
        case 3:
            print(a*b)
        case 4:
            print(a/b)

