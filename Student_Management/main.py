from services import StudentService
import sys


def print_menu():
    print("\n" + "=" * 50)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. View Student Details")
    print("5. Update Student")
    print("6. Delete Student")
    print("7. Exit")
    print("=" * 50)


def login():
    USERNAME = "admin"
    PASSWORD = "Admin@123"

    attempts = 3

    while attempts > 0:
        username = input("Username : ")
        password = input("Password : ")

        if username == USERNAME and password == PASSWORD:
            print("\nLogin Successful!\n")
            return True

        attempts -= 1
        print(f"Invalid Credentials! Attempts Left: {attempts}")

    print("\nToo many failed attempts.")
    return False


def main():

    if not login():
        sys.exit()

    service = StudentService()

    while True:

        print_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                service.add_student()

            elif choice == 2:
                service.view_students()

            elif choice == 3:
                service.search_student()

            elif choice == 4:
                service.view_student_details()

            elif choice == 5:
                service.update_student()

            elif choice == 6:
                service.delete_student()

            elif choice == 7:
                service.sort_students()

            elif choice == 8:
                service.filter_students()

            elif choice == 9:
                service.backup_database()

            elif choice == 10:
                service.restore_database()

            elif choice == 11:
                service.export_json()

            elif choice == 12:
                service.import_json()

            elif choice == 13:
                print("\nThank you for using Student Management System.")
                break

            else:
                print("Invalid Menu Choice.")

        except ValueError:
            print("Please enter a valid number.")

        except KeyboardInterrupt:
            print("\nProgram Interrupted.")
            break

        except Exception as e:
            print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()