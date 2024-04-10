import tkinter as tk
from tkinter import *
from tkinter import ttk
from input import Input

#Complete the method to announce Any action being done
class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Information System")
        self.root.geometry("1350x700+0+0")
        self.input_instance = Input()
        
        self.title_label = tk.Label(self.root, text="Student Management System", font=("Brass Mono", 30, "bold"), bg="pink",relief=tk.GROOVE)
        self.title_label.pack(side=tk.TOP,fill=tk.X)
        
        self.process_frame = tk.LabelFrame(self.root, text="System Options", font=("Brass Mon", 20), border=10, relief= tk.GROOVE, bg="lightgrey")
        self.process_frame.place(x = 20, y = 90, width=400, height=585)
        
         #----------------------------------------------------OPTIONS FRAME------------------------------------------------
        self.button1 = tk.Button(self.process_frame, text="Add Student", font=("Brass Mon", 12, 'bold'),
                    command=lambda: self.input_instance.set_student(self.student_name_ent, self.student_id_ent, self.student_dob_ent))
        self.button1.place(x = 0, y = -5, width=380, height=65)
        #lambda function call the function which is linked behind it
        self.button2 = tk.Button(self.process_frame, text= "Add Course",font=("Brass Mon", 12, 'bold'), 
                    command=lambda: self.input_instance.set_courses(self.course_name_ent, self.course_id_ent, self.course_credits_ent))
        self.button2.place(x = 0, y = 61, width=380, height=60)
        
        self.button3 = tk.Button(self.process_frame, text= "Input Marks",font=("Brass Mon", 12, 'bold'))
        self.button3.place(x = 0, y = 121, width=380, height=60)
        
        self.button4 = tk.Button(self.process_frame, text= "List Students",font=("Brass Mon", 12, 'bold'))
        self.button4.place(x = 0, y = 181, width=380, height=60)
        self.button4.configure(command=self.list_students)
        
        self.button5 = tk.Button(self.process_frame, text= "List Courses",font=("Brass Mon", 12, 'bold'))
        self.button5.place(x = 0, y = 241, width=380, height=60)
        
        self.button6 = tk.Button(self.process_frame, text= "Show Marks for a course",font=("Brass Mon", 12, 'bold'))
        self.button6.place(x = 0, y = 301, width=380, height=60)
        
        self.button6 = tk.Button(self.process_frame, text= "Calculate GPA for a Student",font=("Brass Mon", 12, 'bold'))
        self.button6.place(x = 0, y = 361, width=380, height=60)
        
        self.button7 = tk.Button(self.process_frame, text= "Sort Student by GPA",font=("Brass Mon", 12, 'bold'))
        self.button7.place(x = 0, y = 421, width=380, height=60)
        
        self.button8 = tk.Button(self.process_frame, text= "Exit",font=("Brass Mon", 12, 'bold'), command=self.root.quit)
        self.button8.place(x = 0, y = 481, width=380, height=60)
        
        self.data_frame = tk.LabelFrame(self.root, text="Details", font=("Brass Mon", 20), border=10, relief=tk.GROOVE, bg="lightgrey" )
        self.data_frame.place(x = 430, y =90, width= 910, height=585)
        
        #--------------------------------------------------------ENTRY----------------------------------------------------------
        self.student_name = tk.Label(self.data_frame, text= "Student's Name", font=("Brass Mon", 12, 'bold'), bg="lightgrey")
        self.student_name.grid(row=0,column=1,padx=2, pady=2)
        
        self.student_name_ent = tk.Entry(self.data_frame, bd=3, font=("Brass Mon", 12), width=30)
        self.student_name_ent.grid(row=0, column=2,padx=2,pady=2)
        
        self.student_id = tk.Label(self.data_frame, text= "Student's ID", font=("Brass Mon", 12, 'bold'), bg="lightgrey")
        self.student_id.grid(row=1,column=1,padx=2, pady=2)
        
        self.student_id_ent = tk.Entry(self.data_frame, bd=3, font=("Brass Mon", 12), width=30)
        self.student_id_ent.grid(row=1, column=2,padx=2,pady=2)
        
        self.student_dob = tk.Label(self.data_frame, text= "Student's Date of Birth", font=("Brass Mon", 12, 'bold'), bg="lightgrey")
        self.student_dob.grid(row=2,column=1,padx=2, pady=2)
        
        self.student_dob_ent = tk.Entry(self.data_frame, bd=3, font=("Brass Mon", 12), width=30)
        self.student_dob_ent.grid(row=2, column=2,padx=2,pady=2)
        
        self.course_name = tk.Label(self.data_frame, text= "Course's Name", font=("Brass Mon", 12, 'bold'), bg="lightgrey")
        self.course_name.grid(row=0,column=3,padx=2, pady=2)
        
        self.course_name_ent = tk.Entry(self.data_frame, bd=3, font=("Brass Mon", 12), width=30)
        self.course_name_ent.grid(row=0, column=4,padx=2,pady=2)

        self.course_id = tk.Label(self.data_frame, text= "Course's ID", font=("Brass Mon", 12, 'bold'), bg="lightgrey")
        self.course_id.grid(row=1,column=3,padx=2, pady=2)
        
        self.course_id_ent = tk.Entry(self.data_frame, bd=3, font=("Brass Mon", 12), width=30)
        self.course_id_ent.grid(row=1, column=4,padx=2,pady=2)
        
        self.course_credits = tk.Label(self.data_frame, text= "Course's Credits", font=("Brass Mon", 12, 'bold'), bg="lightgrey")
        self.course_credits.grid(row=2,column=3,padx=2, pady=2)
        
        self.course_credits_ent = tk.Entry(self.data_frame, bd=3, font=("Brass Mon", 12), width=30)
        self.course_credits_ent.grid(row=2, column=4,padx=2,pady=2)
        
         #--------------------------------------------------------LIST----------------------------------------------------------
        self.students_list = ttk.Treeview(self.data_frame, columns=('Student Name', 'ID', 'Date of Birth'))
        self.courses_list = ttk.Treeview(self.data_frame, columns=('Course Name', 'ID', 'Credits'))
        #Define column headings for Student
        self.students_list.heading('#0', text ='')
        self.students_list.heading('Student Name', text="Student's Name")
        self.students_list.heading('ID', text="Student's ID")
        self.students_list.heading('Date of Birth', text="Student's DoB")
        
        self.students_list.column('#0', width=0, stretch=tk.NO)
        self.students_list.column('Student Name', anchor=tk.W, width=150)
        self.students_list.column('ID', anchor=tk.CENTER, width=110)
        self.students_list.column('Date of Birth', anchor=tk.CENTER, width=150)
        
        #Location of the List
        self.students_list.grid(row=4, column=0, columnspan=6,padx=10,pady=10,sticky='w')
        
        #Define column heading for Course
        self.courses_list.heading('#0', text ='')
        self.courses_list.heading('Course Name', text="Course's Name")
        self.courses_list.heading('ID', text="Course's ID")
        self.courses_list.heading('Credits', text="Credits")
        
        self.courses_list.column('#0', width=0, stretch=tk.NO)
        self.courses_list.column('Course Name', anchor=tk.W, width=150)
        self.courses_list.column('ID', anchor=tk.CENTER, width=110)
        self.courses_list.column('Credits', anchor=tk.CENTER, width=150)
        
        #Location of the List
        self.courses_list.grid(row=4, column=2, columnspan=6,padx=10,pady=10,sticky='e')
        
        self.root.mainloop()
        return
    
    def list_students(self, ):
        #Clear existing entries in Treeview
        for item in self.students_list.get_children():
            self.students_list.delete(item)
            
        #Retrieve the list of students from input instance
        students = self.input_instance.get_students()
        
        #Loop over the list of student and put in Treeview
        for student in students:
            self.students_list.insert('', 'end', values=(student.get_name(), student.get_id(), student.get_dob()))
    

if __name__ == "__main__":
    App()
