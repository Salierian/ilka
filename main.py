import curses
import time

menu = ["Acquisitions", "Sales", "Contracts", "Data", "Comms"]


def print_menu(stdscr, selected_idx):
    x = 2
    for idx, row in enumerate(menu):
        y = 1
        if idx == selected_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
        x+=len(row) + 2
        stdscr.refresh()

def main(stdscr):

    curses.curs_set(0)
    
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    index_menu = 0

    print_menu(stdscr, index_menu)

    while 1:
        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_LEFT:
            if index_menu == 0:
                index_menu = 4
            else:
                index_menu-= 1
        elif key == curses.KEY_RIGHT:
            if index_menu == 4:
                index_menu = 0
            else:
                index_menu+= 1
        elif key == curses.KEY_UP:
            pass
        elif key == curses.KEY_DOWN:
            pass

        print_menu(stdscr, index_menu)

        stdscr.refresh()

curses.wrapper(main)
