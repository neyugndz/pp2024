def input_something(args, items):
    num = int(input(f"Enter the number of {args}: "))
    for i in range(num):
        items.append(input_infos(args))
    return items

def input_infos(args):
    item = {}
    if args == "students":
        id, name, dob = input("Enter student ID, name and date of birth(dd/mm/yyyy): ").split()
        item["id"] = id
        item["name"] = name
        item["DoB"] = dob
    elif args == "courses":
        id, name = input("Enter course ID and name: ").split()
        item["id"] = id
        item["name"] = name
    return item

def list_students(students):
    if len(students) == 0:
        print("There aren't any students yet")
    else:
        print("Here is the students list: ")
        
        for i,student in enumerate(students, start=0): #enumerate: to print the list with variables along with their index in the loop
            print(f"{i+1}. {student['id']} - {student['name']} - {student['DoB']}")
            
def list_courses(courses):
    if len(courses) == 0:
        print("There aren't any courses yet")
    else:
        print("Here is the courses list: ")
        
        for i,course in enumerate(courses,start=0):
            print(f"{i+1}. {course['id']} - {course['name']}")           

def input_marks(students, courses, marks):
    if len(courses) == 0 or len(students) == 0:
        print("There must be courses and students before inputting marks.")
        return marks
    print("Select a course to input marks: ")
    list_courses(courses)
    course_index = int(input("Enter the course number: ")) - 1
    
    if course_index < 0 or course_index >= len(courses):
        print("Invalid course selection.")
        return marks
    
    selected_course = courses[course_index]
    
    print(f"Input marks for students in course {selected_course['name']}:")
    for student in students:
        mark = float(input(f"Enter marks for {student['name']}: "))
        marks.append({
            'student_id': student['id'],
            'course_id': selected_course['id'],
            'mark': mark
        })
    return marks
        
def show_student_marks(marks, courses, students):
    if len(courses) == 0 or len(students) == 0 or len(marks) == 0:
        print("There must be courses, students, and marks to show student marks.")
        return
    
    print("Select a course to show student marks: ")
    list_courses(courses)
    course_index = int(input("Enter the course number: ")) - 1
    
    if course_index < 0 or course_index >= len(courses):
        print("Invalid course selection.")
        return 
    
    selected_course = courses[course_index]
    
    print(f"Student marks for course {selected_course['name']}: ")
    for mark in marks:
        if mark['course_id'] == selected_course['id']:
            student = next((student for student in students if student['id'] == mark['student_id']), None)   
            if student:
                print(f"{student['name']} - Marks: {mark['mark']}")


def main():
    students = []
    courses = []
    marks = []
    while(True):
        print("""
    0. Exit
    1. Input students
    2. Input courses
    3. Input marks for a course
    4. List students
    5. List courses
    6. Show student marks for a course
    """)
        options = int(input("Your choice: "))
        
        if options == 0:
            break
        elif options == 1:
            students = input_something("students",students)
        elif options == 2:
            course = input_something("courses",courses)
        elif options == 3:
            marks = input_marks(students, courses, marks)
        elif options == 4:
            list_students(students)
        elif options == 5:
            list_courses(courses)
        elif options == 6:
            show_student_marks(marks, courses, students)
        else:
            print("Invalid input. Please try again")
            
            
if __name__ == "__main__":
    main()