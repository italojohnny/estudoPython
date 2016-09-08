#!/usr/python3.5
import curses

# Nao esta funcionando (necessita de mais testes)
#curses.filter()

myscreen = curses.initscr()
myscreen.border(0)
linha, coluna = myscreen.getmaxyx()

# retorna inteiro da velocidade do terminal em bits por segundo
#print(curses.baudrate())

# Nao esta funcionando
#curses.beep()

# retorna True ou False, se pode alterar as coisas exibidas pelo terminal
#print(curses.can_change_color())

# Nao esta funcionando 
#curses.cbreak()

# Habilita utilizacao de cores no programa
#curses.start_color()

# Retorna um tupla(3) com a intensidade das cores RGB
#print(curses.color_content(50))

# Retorna o valor da cor do texto
#print(curses.color_pair(50))

# Configura a visibilidade do cursor: 0 - invisivel; 1 - visivel; 2 - Muito visivel
curses.curs_set(0)

# Nao esta funcionando (necessita de mais testes)
curses.def_prog_mode()
# Nao esta funcionando (necessita de mais testes)
curses.def_shell_mode()
# Nao esta funcionando (necessita de mais testes)
curses.delay_output(10000)
# Nao esta funcionando (necessita de mais testes)
curses.doupdate()
# Nao esta funcionando (necessita de mais testes)
curses.echo(1)
# Nao esta funcionando (necessita de mais testes)
curses.erasechar()
# Nao esta funcionando (necessita de mais testes)
curses.flash()
# Nao esta funcionando (necessita de mais testes)
curses.flushinp()
# Nao esta funcionando (necessita de mais testes)
#curses.getmouse()
# Nao esta funcionando (necessita de mais testes)

myscreen.addstr(int(linha/2)-1, 10, "Python curses em ação!")
myscreen.addstr(int(linha/2), 10,   "linha:   %d"%linha)
myscreen.addstr(int(linha/2)+1, 10, "coluna: %d"%coluna)
myscreen.refresh()
myscreen.getch()

# Finaliza a aplicacao curses, retornando ao terminal padrao
curses.endwin()
