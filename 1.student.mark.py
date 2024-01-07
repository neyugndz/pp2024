def input_something(args, items):
    num = int(input(f"Enter the number of {args}: "))
    for i in range(num):
        items.append(input_infos(args))
    return items

def input_infos(args):
    item = {}
    if args == "student":
        id, name, dob = input("Enter student ID, name and date of birth(dd/mm/yyyy): ").split()
        item["id"] = id
        item["name"] = name
        item["DoB"] = dob
    elif args == "course":
        id, name = input("Enter course ID and name: ").split()
        item["id"] = id
        item["name"] = name
    return item

def list_students(student):
    if len(student) == 0:
        print("There aren't any students yet")
    else:
        print("Here is the student list: ")
        
        for i,student in enumerate(student, start=0): #enumerate: to print the list with variables along with their index in the loop
            print(f"{i+1}. {student['id']} - {student['name']} - {student['DoB']}")
def list_courses(course):
    if len(course) == 0:
        print("There aren't any courses yet")
    else:
        print("Here is the course list: ")
        
        for i,course in enumerate(course,start=0):
            print(f"{i+1}. {course['id']} - {course['name']}")            
def main():
    student = []
    course = []
    while(True):
        print("""
    0. Exit
    1. Input students
    2. Input courses
    3. List students
    4. List courses
    """)
        options = int(input("Your choice: "))
        
        if options == 0:
            break
        elif options == 1:
            student = input_something("student",student)
        elif options == 2:
            course = input_something("course",course)
        elif options == 3:
            list_students(student)
        elif options == 4:
            list_courses(course)
        else:
            print("Invalid input. Please try again")
            
if __name__ == "__main__":
    main()