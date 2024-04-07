import curses
from curses import wrapper

def main(stdscr):

    stdscr.clear()

    

    one = stdscr.addstr(1,4,"Acquisitions")
    two = stdscr.addstr(1,20,"Sales")
    stdscr.addstr(1, 29, "Contracts")
    stdscr.addstr(1, 42, "Data")
    stdscr.addstr(1, 50, "Comms")

    stdscr.refresh()
    stdscr.getch()

wrapper(main)

def alphaMenu():
    indexMenu = 1
    while True:
        key = stdscr.getkey()

        if key == "KEY_LEFT":
            if indexMenu == 1:
                indexMenu = 4
            else:
                indexMenu = indexMenu - 1

        elif key == "KEY_RIGHT":
            if indexMenu == 4:
                indexMenu = 1
            else:
                indexMenu = indexMenu + 1
        
        elif key == "KEY_DOWN":
            pass
        elif key == "KEY_UP":
            pass
        

