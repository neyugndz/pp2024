import tkinter as tk
from tkinter import *
from input import Input

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
        self.button2 = tk.Button(self.process_frame, text= "Add Another Student",font=("Brass Mon", 12, 'bold'), 
                    command=lambda: self.input_instance.add_another_student(self.student_name_ent, self.student_id_ent, self.student_dob_ent))
        self.button2.place(x = 0, y = 61, width=380, height=60)
        
        self.button3 = tk.Button(self.process_frame, text= "Input Marks",font=("Brass Mon", 12, 'bold'))
        self.button3.place(x = 0, y = 121, width=380, height=60)
        
        self.button4 = tk.Button(self.process_frame, text= "List Students",font=("Brass Mon", 12, 'bold'))
        self.button4.place(x = 0, y = 181, width=380, height=60)
        
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
        
        self.student_name_ent = tk.Entry(self.data_frame, bd=3, font=("Brass Mon", 12), width=25)
        self.student_name_ent.grid(row=0, column=2,padx=2,pady=2)
        
        self.student_id = tk.Label(self.data_frame, text= "Student's ID", font=("Brass Mon", 12, 'bold'), bg="lightgrey")
        self.student_id.grid(row=1,column=1,padx=2, pady=2)
        
        self.student_id_ent = tk.Entry(self.data_frame, bd=3, font=("Brass Mon", 12), width=25)
        self.student_id_ent.grid(row=1, column=2,padx=2,pady=2)
        
        self.student_dob = tk.Label(self.data_frame, text= "Student's Date of Birth", font=("Brass Mon", 12, 'bold'), bg="lightgrey")
        self.student_dob.grid(row=2,column=1,padx=2, pady=2)
        
        self.student_dob_ent = tk.Entry(self.data_frame, bd=3, font=("Brass Mon", 12), width=25)
        self.student_dob_ent.grid(row=2, column=2,padx=2,pady=2)
        
        self.course_name = tk.Label(self.data_frame, text= "Course's Name", font=("Brass Mon", 12, 'bold'), bg="lightgrey")
        self.course_name.grid(row=0,column=3,padx=2, pady=2)
        
        self.course_name_ent = tk.Entry(self.data_frame, bd=3, font=("Brass Mon", 12), width=20)
        self.course_name_ent.grid(row=0, column=4,padx=2,pady=2)

        self.course_id = tk.Label(self.data_frame, text= "Course's ID", font=("Brass Mon", 12, 'bold'), bg="lightgrey")
        self.course_id.grid(row=1,column=3,padx=2, pady=2)
        
        self.course_id_ent = tk.Entry(self.data_frame, bd=3, font=("Brass Mon", 12), width=20)
        self.course_id_ent.grid(row=1, column=4,padx=2,pady=2)
        
        self.course_credits = tk.Label(self.data_frame, text= "Course's Credits", font=("Brass Mon", 12, 'bold'), bg="lightgrey")
        self.course_credits.grid(row=2,column=3,padx=2, pady=2)
        
        self.course_credits_ent = tk.Entry(self.data_frame, bd=3, font=("Brass Mon", 12), width=20)
        self.course_credits_ent.grid(row=2, column=4,padx=2,pady=2)
        self.root.mainloop()
        return
    
    

if __name__ == "__main__":
    App()
