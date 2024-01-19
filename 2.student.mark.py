class Student:
    def __init__(self):
        self.__student_id = input("Enter the student's id: ")
        self.__name = input("Enter the student's name: ")
        self.__dob = input("Enter the student's dob: ")
        
    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob

class Course:
    def __init__(self):
        self.__id = input("Enter the course's id: ")
        self.__name = input("Enter the course's name: ")
        
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
class Utils:
    def input_something(args):
        return int(input(f"Enter the number of {args}: "))
 
class University:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = []
        self.__num_students = 0
        self.__num_courses = 0
    
    def get_num_students(self):
        return self.__num_students
    
    def get_num_courses(self):
        return self.__courses
    
    def get_student(self):
        return self.__students
    
    def get_courses(self):
        return self.__courses
    
    def set_num_students(self):
        self.__num_students = Utils.input_something("students")
        
    def set_num_courses(self):
        self.__num_courses = Utils.input_something("courses")
    
    def set_student(self):
        self.set_num_students()
        for _ in range (self.__num_students):
            student = Student()
            self.__students.append(student)
    
    def set_courses(self):
        self.set_num_courses()
        for _ in range (self.__num_courses):
            course = Course()
            self.__courses.append(course)
            
    def list_students(self):
        if len(self.__students) == 0:
            print("There aren't any students yet.")
        else:
            print("Here is the student list: ")
            
            for i, student in enumerate(self.__students,start=1):
                print(f"{i}. ID: {student.get_id()} - Name: {student.get_name()} - DoB: {student.get_dob()}")
    
    def list_courses(self):
        if len(self.__courses) == 0:
            print("There aren't any courses yet.")
        else:
            print("Here is the course list")
            
            for i, course in enumerate(self.__courses,start=1):
                print(f"{i}. ID: {course.get_id()} - Name: {course.get_name()}")
    
    def input_marks(self):
        if len(self.__courses) == 0 or len(self.__students) == 0:
            print("There must be courses and students before inputting marks.")
            return
        print("Select a course to input marks: ")
        self.list_courses()
        course_index = int(input("Enter the course number: ")) - 1
        
        if course_index < 0 or course_index >= len(self.__courses):
            print("Invalid course selection. ")
            return
        
        selected_course = self.__courses[course_index]
        
        print(f"Input marks for students in course {selected_course.get_name()}")
        
        for student in self.__students:
            mark = float(input(f"Enter marks for {student.get_name()}: "))
            self.__marks.append({
                'Student ID': student.get_id(),
                'Course ID': selected_course.get_id(),  
                'Marks': mark
            })

    def show_marks(self):
        if len(self.__courses) == 0 or len(self.__students) == 0 or len(self.__marks) == 0:
            print("There must be courses, students, and marks to show the student marks.")
            return
        print("Select a course to show marks: ")
        self.list_courses()
        course_index = int(input("Enter the course number: ")) - 1
        
        if course_index < 0 or course_index >= len(self.__courses):
            print("Invalid course selection. ")
            return
        
        selected_course = self.__courses[course_index]
        print(f"Student marks for course {selected_course.get_name()}")
        
        for mark in self.__marks:
            if mark['Course ID'] == selected_course.get_id():
                student = next((student for student in self.__students if student.get_id() == mark['Student ID']), None)
                if student: 
                    print(f"{student.get_name()} - Marks: {mark['Marks']}")

        
def main():
    univ = University()
    while True:
        print("""
    0. Exit
    1. Add Students
    2. Add Courses
    3. Input marks
    4. List Students
    5. List Courses
    6. Show marks for a course
    """)
        option = int(input("Your choice: "))
        if option == 0:
            break
        elif option == 1:
            univ.set_student()
        elif option == 2:
            univ.set_courses()
        elif option == 3:
            univ.input_marks()
        elif option == 4:
            univ.list_students()
        elif option == 5:
            univ.list_courses()
        elif option == 6:
            univ.show_marks()
        else:
            print("Invalid input. Please try again")

if __name__ == "__main__":
    main()
    