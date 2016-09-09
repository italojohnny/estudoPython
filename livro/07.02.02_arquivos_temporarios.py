#!/usr/python3.5
'''
O modulo tempfile implementa algumas funcoes para facilitar a criacao de
arquivos temporarios, liberando o desenvolvedor de algumas preocupacoes, tais
como:
    Evitar colisoes com nomes de arquivos que estao em uso.
    Identificar a area apropriada do sistema de arquivos para temporario (que 
    varia conforme o sistema operacional)
    Expor a aplicacao a riscos (a area de temporarios e utilizada por outro 
    processos)
'''

import tempfile
temp = tempfile.TemporaryFile() # cria arquivo temporario
temp.write(b'teste') # escreve no arquivo temporario
temp.seek(0) # retorna ponteiro do arquivo para o comeco
print(str(temp.read(), encoding='utf8')) # printa a leitura do arquivo
temp.close() # fecha arquivo

'''
Existe tambem a funcao NamedTemporaryFile(), que retorna um objeto para o
arquivo temporario com nome valido exposto.
'''

