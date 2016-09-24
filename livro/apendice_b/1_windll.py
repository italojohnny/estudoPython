#!/usr/python3.5
# codigo nao testado. So funciona em windows
# exemplo com windll
"""
Evocando a caixa de mensagens do Windows
Os argumentos sao: janela pai, mensagem,
titulo da janela e o tipo da janela.
a funcao retorna um inteiro, que
corresponde a que botao foi pressionado
"""
import ctypes
i = ctypes.windll.user32.MessageBoxA(None, b'Teste de DLL!', b'Mensagem', 0)
# o resultado indica qual botao foi clicado
print(i)
