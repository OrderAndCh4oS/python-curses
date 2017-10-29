import curses
from curses import wrapper


def main(screen):
    d = screen.getmaxyx()
    screen.addstr(0, d[1] / 2 - 3, 'Rummy!')
    screen.addstr(d[0] - 1, d[1] / 2 - 8, "Enter q to quit.")
    screen.refresh()
    getInput(screen, d, "Enter C.")
    curses.endwin()


def getInput(screen, d, text):
    q = 0
    line = 1
    screen.addstr(line, d[1] / 2 - len(text)/2, text)
    while not checkInput(q, [ord('q')]):
        screen.refresh()
        q = screen.getch()
        if q == ord('c'):
            line += 1
            screen.addstr(line, d[1] / 2 - len('Entered C!') / 2, 'Entered C!')
            screen.refresh()


def checkInput(ch, validInputs):
    if ch not in validInputs:
        return False
    return True


wrapper(main)
