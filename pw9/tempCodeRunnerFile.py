self.students_list = ttk.Treeview(self.data_frame, columns=('Student Name', 'ID', 'Date of Birth'))
        self.student_list_scrollbar = ttk.Scrollbar(self.data_frame, orient="horizontal",command=self.students_list.yview)
        self.students_list.configure(yscrollcommand=self.student_list_scrollbar.set)
        self.student_list_scrollbar.grid(row=4, column=2, sticky='ns')
        
        self.courses_list = ttk.Treeview(self.data_frame, columns=('Course Name', 'ID', 'Credits'))
        self.courses_list_scrollbar = ttk.Scrollbar(self.data_frame, orient="vertical", command=self.courses_list.yview)
        self.courses_list.configure(yscrollcommand=self.courses_list_scrollbar.set)
        self.courses_list_scrollbar.grid(row=4, column=5, sticky='ns')
        
        self.marks_list = ttk.Treeview(self.data_frame, columns=('Student ID', 'Course ID', 'Marks'))
        self.marks_list_scrollbar = ttk.Scrollbar(self.data_frame, orient="vertical", command=self.marks_list.yview)
        self.marks_list.configure(yscrollcommand=self.marks_list_scrollbar.set)
        self.marks_list_scrollbar.grid(row=5, column=1, sticky='ns')
        
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
        self.students_list.grid(row=4, column=0, columnspan=3,padx=10,pady=10,sticky='w')
        
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
        self.courses_list.grid(row=4, column=4, columnspan=3,padx=10,pady=10,sticky='e')
        
        #Define column heading for Marks
        self.marks_list.heading('#0', text='')
        self.marks_list.heading('Student ID', text="Student's ID")
        self.marks_list.heading('Course ID', text="Course's ID")
        self.marks_list.heading('Marks', text="Marks")
        
        self.marks_list.column('#0', width=0, stretch=tk.NO)
        self.marks_list.column('Student ID', anchor=tk.W, width=150)
        self.marks_list.column('Course ID', anchor=tk.CENTER, width=110)
        self.marks_list.column('Marks', anchor=tk.CENTER, width=150)
        
        #Location of the Marks List
        self.marks_list.grid(row=5, column=0, columnspan=3,padx=10,pady=10,sticky='nsew')
        