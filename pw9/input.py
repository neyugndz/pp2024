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
        
    def input_something(self, args):
        while True:
            try:
                num_of_args = int(input(f"Enter the number of {args}: "))
                if num_of_args >= 0:
                    return num_of_args
                else:
                    print(f"Please enter a positive number of {args}")
            except ValueError:
                print("Please enter a valid number.")
    
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
    
    def valid_credits(self):
        while True:
            credits = input("Enter the course's credit: ")
            if credits.isdigit():
                return credits
            else:
                print("Invalid credits. Please enter a numeric value for credits.")
                      
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
        return True
    
    def add_another_student(self, student_name_entry, student_id_entry, student_dob_entry):
        if self.set_student(student_name_entry, student_id_entry, student_dob_entry):
            student_name_entry.delete(0, 'end')
            student_id_entry.delete(0, 'end')
            student_dob_entry.delete(0, 'end')
        else:
            pass
        
    def set_courses(self):
        num_courses = self.input_something("courses")
        for _ in range(num_courses):
            course_id = input("Enter the course's id: ")
            course_name = self.valid_name("course")
            course_credits = self.valid_credits()
            self.__courses.append(Course(course_id, course_name, course_credits)) 