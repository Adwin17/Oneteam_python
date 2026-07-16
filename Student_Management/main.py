import services


def print_menu():
    print("\n" + "=" * 50)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Student")
    print("2. View All Student Details")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("=" * 50)





    
def main():
    while True:

        print_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
               services.add_student()

            elif choice == 2:
               services.view_all()

            elif choice == 3:
               services.search_student()

            elif choice == 4:
               services.update_student()

            elif choice == 5:
               services.delete_student()

            elif choice == 6:
                print("\nThank you for using Student Management System.")
                break

            else:
                print("Invalid Menu Choice.")

        except ValueError:
            print("Please enter a valid number.")

        except Exception as e:
            print(f"Unexpected Error: {e}")
main()

