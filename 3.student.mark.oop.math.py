from datetime import datetime
import math;
import numpy
class Student:
    def __init__(self):
        self.__student_id = input("Enter the student's id: ")
        self.__name = self.valid_name()
        self.__dob = self.valid_dob()
        
    def valid_dob(self):
        while True:
            dob_str = input("Enter the student's dob (DD/MM/YYYY): ")
            try:
                dob = datetime.strptime(dob_str,"%d/%m/%Y").date()
                return dob.strftime("%d/%m/%Y")
            except ValueError:
                print("Invalid date format. Please enter a valid date format (DD/MM/YYYY): ")
                
    def valid_name(self):
        while True:
            name = input("Enter the student's name: ")
            
            if all(letter.isalpha() or letter.isspace() for letter in name):
                return name
            else:
                print("Invalid name. Please enter a valid name without number or special characters")
 
    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob

class Course:
    def __init__(self):
        self.__id = input("Enter the course's id: ")
        self.__name = self.valid_name()
        self.__credits = self.valid_credits()
        
    def valid_name(self):
        while True:
            name = input("Enter the course's name: ")
            
            if all(letter.isalpha() or letter.isspace() for letter in name):
                return name
            else:
                print("Invalid name. Please enter a valid name without number or special characters")
    
    def valid_credits(self):
        while True:
            credits_s = input("Enter the course's credits: ")
            try:
                credits = float(credits_s)
                if credits > 0:
                    return credits
                else:
                    print("Please enter a positive number of credits .")
            except ValueError:
                print("Please enter a valid numerical value for credits of the course.")
                 
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def get_credits(self):
        return self.__credits
    
class Utils:
    @staticmethod
    def input_something(args):
        while True:
            try:
                num_of_args = int(input(f"Enter the number of {args}: "))
                if num_of_args >= 0:
                    return num_of_args
                else:
                    print(f"Please enter a positive number of {args}")
            except ValueError:
                print("Please enter a valid number. ")
 
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
    
    def valid_mark(self, mark):
        try:
            mark = float(mark)
            if 0.0 <= mark <= 20.0:
                return True
            else:
                print("Invalid mark. Please enter a value between 0.0 and 20.0")
        except ValueError:
            print("Invalid mark. Please enter a valid numerical mark")
        return False
    
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
            while True:
                mark_input = input(f"Enter marks for {student.get_name()}: ")
                if self.valid_mark(mark_input):
                    mark = float(mark_input)
                    rounded_mark = math.floor(mark * 10) / 10
                    self.__marks.append({
                        'Student ID': student.get_id(),
                        'Course ID': selected_course.get_id(),  
                        'Marks': rounded_mark
                    })
                    break

    def check_course(self, selected_course_id):
        for mark in self.__marks:
            if mark['Course ID'] == selected_course_id:
                return False
        return True
        
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
        print(f"Student marks for course {selected_course.get_name()}: ")
        
        if self.check_course(selected_course.get_id()):
            print("No students being marked yet in the selected course.")
            return
        
        for mark in self.__marks:
            if mark['Course ID'] == selected_course.get_id():
                student = next((student for student in self.__students if student.get_id() == mark['Student ID']), None)
                if student: 
                    print(f"{student.get_name()} - Marks: {mark['Marks']}")
                    
                    
    def calGPA(self, student_id):
        student_marks = [mark['Marks'] for mark in self.__marks if mark['Student ID'] == student_id]
        student_credits = [course.get_credits() for course in self.__courses]

        weighted_sum = numpy.dot(student_marks, student_credits)
        total_credits = numpy.sum(student_credits)
        
        if total_credits == 0 :
            return 0.0
        else:
            return weighted_sum / total_credits
        
    def showGPA(self):
        if len(self.__students) == 0 or len(self.__marks) == 0:
            print("There must be students and marks to calculate GPA.")
            return
        
        print("Select a student to calculate GPA.")
        self.list_students()
        index = int(input("Enter the student number: ")) - 1
        
        if index < 0 or index >= len(self.__students):
            print("Invalid student selection.")
            return
        
        selected_student = self.__students[index]
        student_id = selected_student.get_id()
        gpa = self.calGPA(student_id)
        
        print(f"GPA for {selected_student.get_name()} is: {gpa: .2f}")
        
    def sortGPA(self):
        if len(self.__students) == 0 or len(self.__marks) == 0:
            print("There must be students and marks to calculate GPA.")
            return
        
        self.__students.sort(key= lambda student: self.calGPA(student.get_id()), reverse=True)
        
        print("List of students after sorting by GPA in descending order: ")    
        
        for student in self.__students:
            gpa = self.calGPA(student.get_id())
            print(f"{student.get_name()} - GPA: {gpa: .2f}")
        
        
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
    7. Calculate GPA for a student
    8. Sort student by GPA
    """)
        options = input("Your choice: ")
        try:
            option = int(options)
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
            elif option == 7:
                univ.showGPA()
            elif option == 8:
                univ.sortGPA()
            else:
                print("Invalid input. Please try again")
        except ValueError:
            print("Please enter a valid numerical value to process the program")
            
if __name__ == "__main__":
    main()
    