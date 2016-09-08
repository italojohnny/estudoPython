#!/usr/python3.5
import curses
s = curses.initscr()

#s.border('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
#s.border(97, 98, 99, 100, 101, 102, 103, 104)
s.border(0)

#s.addstr('hello world!')
s.addstr(1, 1, 'hello world!')


teste1 = s.getch()
teste2 = s.getkey()
teste3 = s.getmaxyx()
teste4 = s.get
curses.endwin()

print(teste3)
