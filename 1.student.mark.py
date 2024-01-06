def num_students():
    global num_of_stu 
    num_of_stu = int(input("Enter the number of the students: "))
    print("The total number of student is: " + str(num_of_stu))   

def student_info():
    id, name, dob = input("Enter student ID, name and date of birth(dd/mm/yyyy): ").split();
    print("Student ID: " + id)
    print("Name: " + name)
    print("Date of birth:(dd/mm/yyyy) "+ dob)

def num_courses():
    global num_of_courses
    num_of_courses = int(input("Enter the number of the courses: "))
    print("The total number of courses is: " + str(num_of_courses))

def course_info():
    id, name = input("Enter course ID and name: ").split()
    print("Course ID: " + id)
    print("Name of the course: " + name)
    
num_students()

for i in range(num_of_stu):
    student_info()
    
num_courses()

for i in range(num_of_courses):
    course_info()