#!/usr/python3.5

import curses, os, sys, traceback

class gb:
    scrn = None
    cmdoutlines = []
    winrow = None
    startrow = None

def runpsax ():
    p = os.popen('ps aux', 'r')
    gb.cmdoutlines = []
    row = 0
    for ln in p:
        ln = ln[:curses.COLS]
        if ln[-1] == '\n': ln = ln[:-1]
        gb.cmdoutlines.append(ln)
    p.close()

def  showlastpart ():
    gb.scrn.clear()
    gb.winrow = 0
    ncmdlines = len(gb.cmdoutlines)
    if ncmdlines <= curses.LINES:
        gb.startrow = 0
        nwinlines = ncmdlines
    else:
        gb.startrow = ncmdlines - curses.LINES -1
        nwinlines = curses.LINES
    lastrow = gb.startrow + nwinlines -1
    for ln in gb.cmdoutlines[gb.startrow:lastrow]:
        gb.scrn.addstr(gb.winrow,0,ln)
        gb.winrow += 1
    gb.scrn.addstr(gb.winrow, 0, gb.cmdoutlines[lastrow], curses.A_BOLD)
    gb.scrn.refresh()

def updown (inc):
    tmp = gb.winrow +inc
    if tmp >= 0 and  tmp < curses.LINES:
        gb.scrn.addstr(gb.winrow, 0, gb.cmdoutlines[gb.startrow+gb.winrow])
        gb.winrow = tmp
        ln = gb.cmdoutlines[gb.startrow+gb.winrow]
        gb.scrn.addstr(gb.winrow, 0, ln, curses.A_BOLD)
        gb.scrn.refresh()

def kill ():
    ln = gb.cmdoutlines[gb.startrow+gb.winrow]
    pid = int(ln.split()[0])
    os.kill(pid,9)

def rerun ():
    runpsax()
    showlastpart()

def main ():
    gb.scrn = curses.initscr()
    curses.noecho()
    curses.cbreak()
    gb.psax = runpsax()
    showlastpart()
    while True:
        c = gb.scrn.getch()
        c = chr(c)
        if c == 'u': updown(-1)
        elif c == 'd': updown(1)
        elif c == 'r': rerun()
        elif c == 'k': kill()
        else: break
    restorescreen()

def restorescreen ():
    curses.nocbreak()
    curses.echo()
    curses.endwin()

if __name__ == '__main__':
    try:
        main()
    except:
        restorescreen()
        traceback.print_exc()

