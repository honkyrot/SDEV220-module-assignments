# gets the name of a student and their GPA and prints it out
# also checks if they are on a list.

student_last_name = input("Enter student's last name: ").title()

# check if student last name is not ZZZ
if student_last_name != "ZZZ":
    student_first_name = input("Enter student's first name: ").title()
    
    while True: # try check for GPA input
        try:
            student_gpa = float(input("Enter student's GPA: "))
            break
        except ValueError:
            print("Invalid GPA, please try again")

    # checks the student if they are on a list
    if student_gpa > 3.5:
        print(f"{student_last_name}, {student_first_name} has a GPA of {student_gpa} and is on the Dean's List")  # I don't know if they should also be on the honor roll too.
        print("They should also be on the Honor Roll")
    elif student_gpa > 3.25:
        print(f"{student_last_name}, {student_first_name} has a GPA of {student_gpa} and is on the Honor Roll")
    else:
        print(f"{student_last_name}, {student_first_name} has a GPA of {student_gpa}")
else:
    print("last name ZZZ, not processing records")
