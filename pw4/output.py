import curses
from input import Input
class CursesUI:
    def __init__(self,stdscr):
        self.stdscr = stdscr
        self.inp = Input(self)
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
        self.menu_win.addstr("8. Sort Student by GPA ")
        self.menu_win.addstr("0. Exit")
        self.menu_win.refresh()
            
    def handle_option(self, option):
        if option == 1:
            self.switch_to_input_window("ADD STUDENTS")
            self.inp.set_student()
        elif option == 2:
            self.switch_to_input_window("ADD COURSES")
            self.inp.set_courses()
        elif option == 3:
            self.switch_to_input_window("INPUT MARKS")
            self.inp.input_marks()
        elif option == 4:
            self.switch_to_input_window("LIST STUDENTS")
            self.inp.list_students()
        elif option == 5:
            self.switch_to_input_window("LIST COURSES")
            self.inp.list_courses()
        elif option == 6:
            self.switch_to_input_window("SHOW MARKS FOR A SELECTED COURSE")
            self.inp.show_marks()
        elif option == 7:
            self.switch_to_input_window("CALCULATE GPA FOR A STUDENT")
            self.inp.showGPA()
        elif option == 8:
            self.switch_to_input_window("SORT STUDENT BY GPA")
            self.inp.sortGPA()
        else:
            self.show_message("This option is not available yet.", self.input_win)
            
    def switch_to_input_window(self, title):
        self.input_win.clear()
        self.input_win.addstr(f"{title}\n", curses.A_BOLD)
        self.input_win.addstr("-" * 30 + "\n", curses.A_BOLD)
        self.input_win.refresh()
        
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
        
    