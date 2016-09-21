#!/usr/python3.5
"""
OBJETOS DISTRIBUIDOS
A premissa basica da tecnologia de objetos distribuidos e tornar objetos
disponiveis para que seus metodos possam ser evocados remotamente a partir de
outras maquinas ou mesmo por outros processos na mesma maquina, usando a pilha
de protocolos de rece tcp/ip para isso.
Existem diversas solucoes para estes casos, porem utilizar objetos distribuidos
oferece varias vantagens em relacao a outras solucoes que implementam
funcionalidades semelhantes, tal como o protocolo xml-rpc:
    * simplicidade para implementacao
    * oculta as camadas de comunicacao
    * suporte a estruturas de dados nativas (contanto que sejam serializaveis)
    * boa performance
    * maturidade da solucao
PYRO (PYthon Pemote Objects) e um framework para aplicacoes distribuidas que
permite publicar objetos via tcp/ip. Na maquina servidora, o pyro publica o
objeto, cuidando de detalhes como protocolo, controle de sessao, autenticacao,
controle de concorrencia e outros.
"""
# EXEMPLO DE SERVIDOR
import Pyro4

class Dist: # classe para o objeto distribuido
    def calc(self, n):
        return n**n

if __name__ == '__main__':
    daemon = Pyro4.Daemon(port=8888) # define a porta tcp/ip usada pelo pyro
    uri = daemon.register(Dist(), 'dist') # publica  o objeto
    print(uri)
    daemon.requestLoop()

"""
Na maquna cliente, o programa usao PYRO para evocar rotinas do servidore receber
os resultado da mesma forma que um metodo de um objeto local.
"""

# EXEMPLO DE CLIENTE
import Pyro4

uri = 'PYRO:dist@localhost:8888' # url com a porta
proxy = Pyro4.Proxy(uri)

for i in range(10): # testa com ate dez elementos
    print((i +1, '=>', proxy.calc(i +1)))

"""
Os metodos publicados por meio do PYRO nao podem ser identificados por
introspeccao pela aplicacao cliente.
Embora PYRO resolva problemas de concorrencia de comunicacao com os clientes
queestao acessando o mesmo servidor (cada conexao roda em um thread separada),
fica por conta do desenvolvedr (ou de outros frameworks que a aplicacao utilize)
resolver questoes de concorrencia por outros recursos, como arquivos ou conexao
de banco de dados, por exemplo. E possivel autenticar as conexoes atraves da
criacao de objetos da classe validator, que podem verificar credenciais,
endereco IP e outros itens.
"""
