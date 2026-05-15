students = []

def main():
    while True:
        print("\n student record manager")
        print("1 add student")
        print("2 view all students")
        print("3 search student")
        print("4 update marks")
        print("5 delete student")
        print("6 exit")

        choice = input("Enter your choice:")
        if choice == '1':
            roll_no = input("Enter Roll Number:")
            duplicate = False
            for s in students:
                if s["roll_no"] == roll_no:
                    duplicate = True
                    break
            
            if duplicate:
                print("Error: duplicate roll number")
            else:
                name = input("Enter Name:")
                marks = input("Enter Marks:")
                new_student = {
                    "roll_no": roll_no,
                    "name": name,
                    "marks": marks
                }
                students.append(new_student)
                print("student added")

        elif choice == '2':
            if not students:
                print("no record found")
            else:
                print("\n all student records")
                for s in students:
                    print(f"Roll: {s['roll_no']}, Name: {s['name']}, Marks: {s['marks']}")

        elif choice == '3':
            search_roll = input("Enter roll Number to search:")
            found = False
            for s in students:
                if s["roll_no"] == search_roll:
                    print(f"found name: {s['name']}, marks: {s['marks']}")
                    found = True
                    break
            if not found:
                print("student not found")

        elif choice == '4':
            update_roll = input("Enter Roll Number to update marks: ")
            found = False
            for s in students:
                if s["roll_no"] == update_roll:
                    new_marks = input("Enter new marks: ")
                    s["marks"] = new_marks
                    print("marks updated")
                    found = True
                    break
            if not found:
                print("Error: student doesn't exist")

        elif choice == '5':
            delete_roll = input("Enter Roll Number to delete:")
            found = False
            for i in range(len(students)):
                if students[i]["roll_no"] == delete_roll:
                    confirm = input(f"Are you sure you want to delete {students[i]['name']}? (y/n): ")
                    if confirm.lower() == 'y':
                        students.pop(i)
                        print("student deleted")
                    found = True
                    break
            if not found:
                print("student not found")


        elif choice == '6':
            print("task khatam, bye")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
