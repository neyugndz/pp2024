import numpy
import os
import zipfile
import pickle
import threading
from datetime import datetime
from domains.student import Student
from domains.course import Course

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
                      
    def set_student(self, student_name_entry, student_id_entry, student_dob_entry):
        student_id = student_id_entry.get()
        name = student_name_entry.get()
        dob = student_dob_entry.get()
    
        if not self.valid_id(student_id):
            print("Invalid name. Please enter a valid name without number or special character.")
            return False
        
        if not self.valid_name(name):
            print("Invalid student ID. Please enter a non-empty string.")
            return False
        
        if not self.valid_dob(dob):
            print("Invalid date of birth. Please enter a valid date in DD/MM/YYYY format.")
            return False
        
        self.__students.append(Student(student_id, name, dob))
        print("Student added successfully!")
        student_name_entry.delete(0, 'end')
        student_id_entry.delete(0, 'end')
        student_dob_entry.delete(0, 'end')
        return True
        
    def set_courses(self, course_name_entry, course_id_entry, course_credit_entry):
        name = course_name_entry.get()
        course_id = course_id_entry.get()
        credit = course_credit_entry.get()
        
        if not self.valid_id(course_id):
            print("Invalid name. Please enter a valid name without number or special character.")
            return False
        
        if not self.valid_name(name):
            print("Invalid course ID. Please enter a non-empty string.")
            return False
        
        if not self.valid_credits(credit):
            print("Invalid credits. Please enter a digit value for credit of the course. ")
            return False
        
        self.__courses.append(Course(name, course_id, credit))
        print("Course added successfully!")
        course_name_entry.delete(0, 'end')
        course_id_entry.delete(0, 'end')
        course_credit_entry.delete(0, 'end')
        return True
    
    def list_students(self, student_list):
        for item in student_list.get_children():
            student_list.delete(item)
            
        students = self
        
        