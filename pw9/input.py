from datetime import datetime
from domains.student import Student
from domains.course import Course
from tkinter import messagebox

class Input:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = []

    def valid_name(self, name):
        return all(letter.isalpha() or letter.isspace() for letter in name)
    
    def valid_id(self, student_id):
        return len(student_id) > 0
    
    def valid_dob(self, dob_str):
        try:
            dob = datetime.strptime(dob_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False
    
    def valid_credits(self, credit):
        return credit.isdigit()
    
    def get_students(self):
        return self.__students[:] #Return a copy of the list
    
    def get_courses(self):
        return self.__courses[:]
    
    def get_marks(self, course_id):
        show_marks = [(student_id, marks) for student_id, course_id, marks in self.__marks if course_id == course_id]
        return show_marks
        
    def set_marks(self, student_id, course_id, marks_str):
        #validate student and course existence
        students = any(student.get_id() == student_id for student in self.__students)
        courses = any(course.get_id() == course_id for course in self.__courses)
        
        if not students or not courses:
            return False
        
        try:
            marks = int(marks_str)
            if not(0 <= marks <= 20):
                return False
        except ValueError:
            return False
        
        self.__marks.append((student_id, course_id, marks))
        return True
        
    def set_student(self, student_name_entry, student_id_entry, student_dob_entry):
        student_id = student_id_entry.get()
        name = student_name_entry.get()
        dob = student_dob_entry.get()
    
        if not self.valid_id(student_id):
            messagebox.showerror("Invalid name", "Please enter a valid name without number or special character.")
            return False
        
        if not self.valid_name(name):
            messagebox.showerror("Invalid student ID", "Please enter a non-empty string.")
            return False
        
        if not self.valid_dob(dob):
            messagebox.showerror("Invalid date of birth", "Please enter a valid date in DD/MM/YYYY format.")
            return False
        
        self.__students.append(Student(student_id, name, dob))
        messagebox.showinfo("Success", "Student added successfully!")
        student_name_entry.delete(0, 'end')
        student_id_entry.delete(0, 'end')
        student_dob_entry.delete(0, 'end')
        return True
        
    def set_courses(self, course_name_entry, course_id_entry, course_credit_entry):
        name = course_name_entry.get()
        course_id = course_id_entry.get()
        credit = course_credit_entry.get()
        
        if not self.valid_name(name):
            messagebox.showerror("Invalid course ID", "Please enter a non-empty string.")
            return False
        
        if not self.valid_id(course_id):
            messagebox.showerror("Invalid name", "Please enter a valid name without number or special character.")
            return False
        
        if not self.valid_credits(credit):
            messagebox.showerror("Invalid credits", "Please enter a digit value for credit of the course. ")
            return False
        
        self.__courses.append(Course(name, course_id, credit))
        messagebox.showinfo("Success", "Course added successfully!")
        course_name_entry.delete(0, 'end')
        course_id_entry.delete(0, 'end')
        course_credit_entry.delete(0, 'end')
        return True

        
        