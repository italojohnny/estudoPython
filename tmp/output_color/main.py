
def printc (msg, color="green"):
    from sys import stderr
    if   color == "black":        color = "0;30"
    elif color == "red":          color = "0;31"
    elif color == "green":        color = "0;32"
    elif color == "brown":        color = "0;33"
    elif color == "orange":       color = "0;33"
    elif color == "blue":         color = "0;34"
    elif color == "purple":       color = "0;35"
    elif color == "cyan":         color = "0;36"
    elif color == "ligth gray":   color = "0;37"
    elif color == "dark gray":    color = "1;30"
    elif color == "light red":    color = "1;31"
    elif color == "light green":  color = "1;32"
    elif color == "yellow":       color = "1;33"
    elif color == "light blue":   color = "1;34"
    elif color == "light purple": color = "1;35"
    elif color == "light cyan":   color = "1;36"
    else:                         color = "1;37" # white
    print >> stderr, "\033[%sm%s\033[0m" % (color, msg)

printc("ola mundo", "orange")
