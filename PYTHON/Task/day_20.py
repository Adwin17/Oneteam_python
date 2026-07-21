import copy

try:
    n = int(input("Enter the number of students: "))

    names = []
    rolls = []
    marks = []

    for i in range(n):
        print(f"\nStudent {i+1}")

        name = input("Enter Name: ")
        roll = int(input("Enter Roll Number: "))

        m = []
        for j in range(1, 4):
            mark = int(input(f"Enter marks for Subject {j}: "))
            m.append(mark)

        names.append(name)
        rolls.append(roll)
        marks.append(m)

    student_dict = dict(zip(rolls, names))

    print(student_dict)

    upper_names = [i.upper() for i in names]
    print(upper_names)

    for name in names:
        if len(name) > 5:
            print(name)

    count = 0
    for name in names:
        if name.upper().startswith("A"):
            count += 1

    print("Number of names starting with 'A':", count)

  
    avg_list = [names[i] for i in range(n) if sum(marks[i])/3>75]

    even_list = [roll for roll in rolls if roll % 2 == 0]

    print("List for avg >75",avg_list)
    print("List for even roll no.s",even_list)

    first_mark= tuple(marks[0])
    print(first_mark)

    
    unique= set()

    for j in marks:
        for k in j:
            unique.add(k)
    print(unique)

    shallow_copy = copy.copy(marks)
    deep_copy = copy.deepcopy(marks)
    marks[0][0] = 77

    print("original",marks)

    print("shallow",shallow_copy)
    print("deep",deep_copy)

except ValueError:
    print("Invalid input! ")

except IndexError:
    print("No student data available.")

except Exception as e:
    print("An error occurred:", e)