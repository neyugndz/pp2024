class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob           