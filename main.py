import curses
from curses import wrapper

def main(stdscr):

    stdscr.clear()

    

    stdscr.addstr(1,4,"Acquisitions")
    stdscr.addstr(1,20,"Sales")
    stdscr.addstr(1, 29, "Contracts")
    stdscr.addstr(1, 42, "Data")
    stdscr.addstr(1, 50, "Comms")

    stdscr.refresh()
    stdscr.getch()

wrapper(main)

def alphaMenu():
    while True:
        key = stdscr.getkey()

        if key == "KEY_LEFT":
            pass
        elif key == "KEY_RIGHT":
            pass
        elif key == "KEY_DOWN":
            pass
        elif key == "KEY_UP":
            pass
