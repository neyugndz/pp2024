import curses
from datetime import datetime
import math;
import numpy
class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        
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
    def __init__(self, Id, name, credit):
        self.__id = Id
        self.__name = name
        self.__credits = credit
        
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
    def __init__(self, ui):
        self.__students = []
        self.__courses = []
        self.__marks = []
        self.ui = ui
    
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
        num_students = self.ui.get_input_numeric("Enter the number of students: ", self.ui.input_win)
        for _ in range(num_students):
            student_id = self.ui.get_input_string("Enter student's id: ", self.ui.input_win)
            name = self.ui.get_input_string("Enter student's name: ", self.ui.input_win)
            dob = self.ui.get_input_string("Enter student's dob (DD/MM/YYYY): ", self.ui.input_win)
            self.__students.append(Student(student_id, name, dob))
        self.ui.show_message(f"{num_students} students added successfully.", self.ui.input_win)
                
    def set_courses(self):
        num_courses = self.ui.get_input_numeric("Enter the number of courses: ", self.ui.input_win)
        for _ in range(num_courses):
            course_id = self.ui.get_input_string("Enter the course's id: ", self.ui.input_win)
            name = self.ui.get_input_string("Enter the course's name: ", self.ui.input_win)
            credit = self.ui.get_input_string("Enter the course's credits: ", self.ui.input_win)
            self.__courses.append(Course(course_id, name, credit))
        self.ui.show_message(f"{num_courses} courses added successfully. ", self.ui.input_win)
                
    def list_students(self):
        if len(self.__students) == 0:
            self.ui.show_message("There aren't any students yet.", self.ui.input_win)
        else:
            student_list = "Here is the student list:\n"   
            for i, student in enumerate(self.__students,start=1):
                student_list += f"{i}. ID: {student.get_id()} - Name: {student.get_name()} - DoB: {student.get_dob()}\n"
            self.ui.show_message(student_list, self.ui.input_win)
        
    def list_courses(self):
        if len(self.__courses) == 0:
            self.ui.show_message("There aren't any courses yet.", self.ui.input_win)
        else:
            course_list = "Here is the course list:\n"
            
            for i, course in enumerate(self.__courses,start=1):
                course_list += f"{i}. ID: {course.get_id()} - Name: {course.get_name()}\n"
            self.ui.show_message(course_list, self.ui.input_win)
        
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
            self.ui.show_message("There must be courses and students before inputting marks.", self.ui.input_win)
            return
        self.list_courses()
        course_index = self.ui.get_input_numeric("Select a course to input marks (by number): ", self.ui.input_win) - 1
        
        if course_index < 0 or course_index >= len(self.__courses):
            self.ui.show_message("Invalid course selection. ", self.ui.input_win)
            return
        
        selected_course = self.__courses[course_index]
        
        for student in self.__students:
            mark_input = self.ui.get_input_numeric(f"Enter marks for {student.get_name()}: ", self.ui.input_win)
            self.__marks.append({
                'Student ID' : student.get_id(),
                'Course ID' : selected_course.get_id(),
                'Marks' : mark_input
            })
        self.ui.show_message("Marks entered successfully. ", self.ui.input_win)

    def check_course(self, selected_course_id):
        for mark in self.__marks:
            if mark['Course ID'] == selected_course_id:
                return False
        return True
        
    def show_marks(self):
        if len(self.__courses) == 0 or len(self.__students) == 0 or len(self.__marks) == 0:
            self.ui.show_message("There must be courses, students, and marks to show the student marks.", self.ui.input_win)
            return
        self.list_courses()
        course_index = self.ui.get_input_numeric("Select a course to show marks (by number): ", self.ui.input_win) - 1
        
        if course_index < 0 or course_index >= len(self.__courses):
            self.ui.show_message("Invalid course selection. ", self.ui.input_win)
            return
        
        selected_course = self.__courses[course_index]
        mark_list = f"Student marks for course {selected_course.get_name()}:\n"
        
        for mark in self.__marks:
            if mark['Course ID'] == selected_course.get_id():
                student = next((student for student in self.__students if student.get_id() == mark['Student ID']), None)
                if student: 
                    mark_list += f"{student.get_name()} - Marks: {mark['Marks']}\n"
                    
        if self.check_course(selected_course.get_id()):
            self.ui.show_message("No students being marked yet in the selected course.", self.ui.input_win)
            return
        
        self.ui.show_message(mark_list, self.ui.input_win)
        
    def calGPA(self, student_id):
        student_marks = [mark['Marks'] for mark in self.__marks if mark['Student ID'] == student_id]
        student_credits = [int(course.get_credits()) for course in self.__courses]

        weighted_sum = numpy.dot(student_marks, student_credits)
        total_credits = numpy.sum(student_credits)
        
        if total_credits == 0 :
            return 0.0
        else:
            return weighted_sum / total_credits
        
    def showGPA(self):
        if len(self.__students) == 0 or len(self.__marks) == 0:
            self.ui.show_message("There must be students and marks to calculate GPA.", self.ui.input_win)
            return
        self.list_students()
        student_index = self.ui.get_input_numeric("Select a student to calculate GPA (by number): ", self.ui.input_win) - 1
        
        if student_index < 0 or student_index >= len(self.__students):
            self.ui.show_message("Invalid student selection.", self.ui.input_win)
            return
        
        selected_student = self.__students[student_index]
        student_marks = [mark for mark in self.__marks if mark['Student ID'] == selected_student.get_id()]
        if not student_marks:
            self.ui.show_message(f"No marks recorded for {selected_student.get_name()}.", self.ui.input_win)
            return
        
        total_credits = 0
        total_points = 0
        for mark in student_marks:
            course = next((course for course in self.__courses if course.get_id() == mark['Course ID']), None)
            if course:
                total_credits += int(course.get_credits())
                total_points +=  mark['Marks'] * int(course.get_credits())
            
        if total_credits == 0 :
            gpa = 0
        else:
            gpa = total_points / total_credits
        
        self.ui.show_message(f"GPA for {selected_student.get_name()}: {gpa:.2f}", self.ui.input_win)
        
    def sortGPA(self):
        if len(self.__students) == 0 or len(self.__marks) == 0:
            self.ui.show_message("No students or marks have been added yet.", self.ui.input_win)
            return

        def calculate_gpa(student_id):
            student_marks = [mark for mark in self.__marks if mark['Student ID'] == student_id]
            total_credits = 0
            total_points = 0
            for mark in student_marks:
                course = next((course for course in self.__courses if course.get_id() == mark['Course ID']), None)
                if course:
                    total_credits += int(course.get_credits())
                    total_points += mark['Marks'] * int(course.get_credits())
            return total_points / total_credits if total_credits else 0

        self.__students.sort(key=lambda student: calculate_gpa(student.get_id()), reverse=True)

        sorted_students = "Students sorted by GPA in descending order:\n"
        for student in self.__students:
            gpa = calculate_gpa(student.get_id())
            sorted_students += f"{student.get_name()} - GPA: {gpa:.2f}\n"

        self.ui.show_message(sorted_students, self.ui.input_win)

class CursesUI:
    def __init__(self,stdscr):
        self.stdscr = stdscr
        self.univ = University(self)
        self.intitialize_ui()
        
    def intitialize_ui(self):
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        self.stdscr.bkgd(curses.color_pair(1))
        self.stdscr.refresh()
        
        max_y, max_x = self.stdscr.getmaxyx()
        self.input_win_height = 10
        self.menu_win = self.stdscr.subwin(max_y - self.input_win_height, max_x, 0, 0)
        self.input_win = self.stdscr.subwin(self.input_win_height, max_x, max_y - self.input_win_height, 0)

        self.menu_win.bkgd(curses.color_pair(1))
        self.input_win.bkgd(curses.color_pair(1))
        self.menu_win.refresh()
        self.input_win.refresh()
    
    def main_loop(self):
        while True:
            self.show_menu()
            option = self.get_input_numeric("Select an option (0 to exit): ",  self.input_win)
            if option == 0:
                break
            self.handle_option(option)
            self.stdscr.refresh()
            
    def show_menu(self):
        self.menu_win.clear()
        self.menu_win.addstr("University Management System\n", curses.A_BOLD)
        self.menu_win.addstr("-" * 30 + "\n", curses.A_BOLD)
        self.menu_win.addstr("1. Add Students \n")
        self.menu_win.addstr("2. Add Courses \n")
        self.menu_win.addstr("3. Input Marks \n")
        self.menu_win.addstr("4. List Students \n")
        self.menu_win.addstr("5. List Courses \n")
        self.menu_win.addstr("6. Show Marks for a Course \n")
        self.menu_win.addstr("7. Calculate GPA for a Student \n")
        self.menu_win.addstr("8. Sort Student by GPA \n")
        self.menu_win.addstr("0. Exit")
        self.menu_win.refresh()
            
    def handle_option(self, option):
        options_map = {
            1: self.univ.set_student,
            2: self.univ.set_courses,
            3: self.univ.input_marks,
            4: self.univ.list_students,
            5: self.univ.list_courses,
            6: self.univ.show_marks,
            7: self.univ.showGPA,
            8: self.univ.sortGPA
        }
        action = options_map.get(option)
        if action:
            action()
        else:
            self.show_message("This option is not implemented yet.")
        
    def get_input_numeric(self, prompt, window):
        while True:
            num_str = self.get_input_string(prompt, window)
            if num_str.isdigit():
                return int(num_str)
            else:
                self.show_message("Please enter a valid number.", window)
    
    def show_message(self, message, window):
        window.clear()
        window.addstr(message + "\n Please any key to continue...")
        window.refresh()
        window.getch()
        
    def get_input_string(self, prompt, window):
        window.clear()
        window.addstr(prompt)
        curses.echo()
        input_str = window.getstr().decode('utf-8')
        curses.noecho()
        window.clear()
        window.refresh()
        return input_str
    
def main(stdscr):
    ui = CursesUI(stdscr)
    ui.main_loop()
            
if __name__ == "__main__":
    curses.wrapper(main)