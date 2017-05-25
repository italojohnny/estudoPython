import commands

def get_list_file ():


def exec_command_system (cmd):
    return commands.getstatusoutput(cmd)


diretorio = "/home/italo/Pictures/"
comando = "find %s -name '*' -type f | sort | egrep -i 'JPG$'" % diretorio
print exec_command_system(comando)
        
