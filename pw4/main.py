import curses
from output import CursesUI

def main(stdscr):
    ui = CursesUI(stdscr)
    ui.main_loop()

if __name__ == "__main__":
    curses.wrapper(main)
