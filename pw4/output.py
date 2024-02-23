import curses
from input import Input
class CursesUI:
    def __init__(self,stdscr):
        self.stdscr = stdscr
        self.inp = Input(self)
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        self.stdscr.bkgd(curses.color_pair(1)) 
        self.stdscr.refresh()   
        
    def draw_menu(self, menu):
        self.stdscr.clear()
        self.stdscr.addstr("University Management System\n", curses.A_BOLD)
        self.stdscr.addstr("-" * 30 + "\n", curses.A_BOLD)
        for idx, item in enumerate(menu,start=1):
            menu_item = f"{idx}. {item}\n"
            self.stdscr.addstr(menu_item)
        self.stdscr.addstr("\nSelect an option (0 to exit): ", curses.A_BOLD)
        self.stdscr.refresh()
    
    def main_loop(self):
        menu_options = [
            "Add Students",
            "Add Courses",
            "Input Marks",
            "List Students",
            "List Courses",
            "Show Marks for a Course",
            "Calculate GPA for a Student",
            "Sort Student by GPA"
        ]
        while True:
            self.draw_menu(menu_options)
            option = self.get_input_numeric("Select an option (0 to exit): ")
            if option == 0:
                break
            self.handle_option(option)
            
    def handle_option(self, option):
        options_map = {
            1: self.inp.set_student,
            2: self.inp.set_courses,
            3: self.inp.input_marks,
            4: self.inp.list_students,
            5: self.inp.list_courses,
            6: self.inp.show_marks,
            7: self.inp.showGPA,
            8: self.inp.sortGPA
        }
        action = options_map.get(option)
        if action:
            action()
        else:
            self.show_message("This option is not available yet.")
        
    def get_input_numeric(self, prompt):
        while True:
            num_str = self.get_input_string(prompt)
            if num_str.isdigit():
                return int(num_str)
            else:
                self.show_message("Please enter a valid number.")
    
    def show_message(self, message):
        self.stdscr.clear()
        self.stdscr.addstr(message + "\n Please any key to continue...")
        self.stdscr.refresh()
        self.stdscr.getch()
        
    def get_input_string(self, prompt):
        self.stdscr.clear()
        self.stdscr.addstr(prompt)
        curses.echo()
        input_str = self.stdscr.getstr().decode('utf-8')
        curses.noecho()
        return input_str
    