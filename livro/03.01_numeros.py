#!/usr/python3.5

i = 1 # (int) inteiro
f = 3.14 # (float) flutuante
c = 3+4j # (complex) complexo

# convertendo de real para inteiro
print('int(3.14) =', int(3.14))

# convertendo de inteiro para real
print('float(5) = ', float(5))

# calculo entre inteiro e real resulta em real
print('5.0 / 2 + 3 = ', 5.0/2+3)

# inteiros em outras base
print("int('20', 8) = ", int('20', 8))
print("int('20', 16) = ", int('20', 16))

# operacoes com numeros complexos
c = 3+4j
print('c = ', c)
print('Parte real: ', c.real)
print('Parte imaginaria: ', c.imag)
print('conjugado: ', c.conjugate())

# representacao de numero real em notacao cientifica
r = 1.2e22
print("numero real em nocatacao cientifica: ", r)

# operacoes aritmeticas
print('soma: 3 + 12 = ', 3 + 12)
print('diferenca: 43 - 18 = ', 43 - 18)
print('multiplicacao: 31 * 54 = ', 31 * 54)
print('divisao: 11 / 7 = ', 11 / 7) # o resultado sermpre é real, mesmo se a divisao for exata
print('divisao inteira: 11 // 7 =', 11 // 7) # a redonda para o inteiro inferior
print('modulo: 11 % 7 = ', 11 % 7) # resto da divisao
print('potencia: 100 ** 5 = ', 100 ** 5)
print('raiz: 100 ** 0.5 = ', 100 ** 0.5)

# operacoes logicas
print('menor: 5 < 4 = ', 5 < 4)
print('maior: 5 > 4 = ', 5 > 4)
print('menor: ou igual:  5 <= 4 = ', 5 <= 4)
print('maior: ou igual:  5 >= 4 = ', 5 >= 4)
print('igual: 5 == 4 = ', 5 == 4)
print('diferente: 5 != 4 = ', 5 != 4)

# operacoes bit-a-bit
a = 60                                       # 60 0011 1100
b = 13                                       # 13 0000 1101
print('e: ', a & b)                          # 12 0000 1100
print('ou: ', a | b)                         # 61 0011 1101
print('ou exclusivo: ', a ^ b)               # 49 0011 0001
print('inversao: ', ~a)                      #-61 1100 0011
print('deslocamento para esquerda: ', a << 2)#240 1111 0000
print('deslocamento para direita: ', a >> 2) # 15 0000 1111

# outras funcoes (built-in)
print('valor absoluto: abs(16) = ', abs(16))
print('valor octal: oct(16) = ', oct(16))
print('valor hexadecimal: hex(16) = ', hex(16))
print('potencia: pow(2,8) = ', pow(2, 8))
