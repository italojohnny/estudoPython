#!/usr/python3.5
"""
SOBRECARGA DE OPERADORES
o comportamento dos operadores e definido por metodos especiais, porem tais
metodos so podem ser alterados nas classes abertas. Por convencao, os metodos
especiais tem nomes que comecam e terminnam com "__".

Lista de operadores e os metodos correspondentes:
    +  __add__      adicao
    -  __sub__      subtracao
    *  __mul__      multiplicacao
    /  __div__      divisao
    // __floordiv__ divisao inteira
    %  __mod__      modulo
    ** __pow__      potencia
    +  __pos__      positivo
    -  __neg__      negativo
    <  __lt__       menor que
    >  __gt__       maior que
    <= __le__       menor ou igual a
    >= __ge__       maior ou igual a
    == __eq__       igual a
    != __ne__       diferente de
    << __lshift__   deslocamento para a esquerda
    >> __rshift__   deslocamento para a direita
    &  __and__      e bit-a-bit
    |  __or__       ou bit-a-bit
    ^  __xor__      ou exclusivo bit-a-bit
    ~  __inv__      inversao
"""
class String (str):
    def __sub__(self, s):
        return self.replace(s, '')

s1 = String('The Lamb Lies Down On Broadway')
s2 = 'Down'

print('"%s" - "%s" = "%s"' % (s1, s2, s1 - s2))

"""
Observacoes:
    * A subtracao definida no codigo nao e comutativa (da mesma forma que a
    adicao em strings tambem nao e)
    * a classe str nao e aberta, portanto nao e possivel alterar o comportamento
    da string-padrao do python. Porem a classe String e aberta.
    * A redefinicao de operadores conhecidos pode dificultar a leitura do codigo.
"""
