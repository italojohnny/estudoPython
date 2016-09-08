#!/usr/python3.5
import string
# string em python sao imutaveis, nao e possivel adicionar, remover ou mesmo modificar
# string padrao segue o padrao unicode, suportando acentos e caracteres especiais

# inicializacao de string
a = 'Ne Obliviscaris - Forget Not'
b = "be'lakor - Abeyance"
c = '''
I swallow forgotten words
To gain what was lost
And lost what was gained
Until neither is real
Behind my head, her hands hold no weight
'''
d = r'\n'

print(a)
print(b)
print(c)
print(d)

# operacoes com strings
r = 'cachorro'
print('concatenacao: O '+ r +' roeu a roupa do rei')
print('interpolacao: tamanho de %s = %d' % (r, len(r)))
for ch in r: print('carcter por caracter: ' +ch)
if r.startswith('c'): print(r.upper()) # strings sao objetos e possuem metodos
print(3 * r) #imprime 3 vezes a string

# simbolos usados na interpolacao
print('%s interpolacao com string' % 'isso e')
print('%d interpolacao com inteiro' % 20)
print('%o interpolacao com octal' % 20)
print('%x interpolacao com hexadeciaml' % 20)
print('%f interpolacao com real' % 20)
print('%d%% imprimir caracter %%' % 20)
print('contorlar quantidade de casas %02d:%02d' % (8,2))
print('%.1f%% controlar casas depois do ponto' % 3.1415)

# interpolacao com format()
lt = [('Page', 'guitarrista', 'Led Zeppelin'), ('Fripp', 'guitarrista', 'King Crimson')]
msg = '{0} e {1} do {2}'
for nome, funcao, banda in lt:
    print(msg.format(nome, funcao, banda))

# indice
print('Python'[::-1])
a = string.ascii_letters
print(a)
b = a[1:] + a[0]
print(b)

tab = str.maketrans(a,b)
msg = '''Esse texto será traduzido...
vai ficar bem estranho.'''
print(msg.translate(tab))

st = string.Template('$aviso aconteceu em $quando')
s = st.substitute({'aviso':'Falta de eletricidade', 'quando':'03 de Abril de 2016'})
print(s)

s = bytearray(b'Python')
s[0] = ord('p')
print(s.decode())

# string unicode
u = 'Hüsker Dü'
s = u.encode('latin1')
print(s, '=>', type(s))

# bytes para unicode
s = bytes('Hüsker Dü', 'latin1')
u = s.decode('latin1')
print(u, '=>', type(u))


