#!/usr/python3.5
"""
DESEMPENHO
o python prove algumas ferramentas para avaliar performance e localizar gargalos
na aplicacao. Entre essas ferramentas estao os modulos cProfile e timeit.
O modulo cprofile faz uma analise detalhada de performance, incluindo as
chamadas de funcao, retornos de funcao e excecoes.

O relatorio do cProfile mostra no inicio as duas informacoes mais importantes: o
tempo de CPU consumido em segundos e a quantidade de chamadas de funcao. As
outras linhas mostram os detalhes por funcao, incluindo o tempo total e por
chamada.
As cinco rotinas do exemplo tem a mesma funcionalidade: geram uma escala de
cores rgb. Porem o tempo de execucao e diferente.
Fatores observados que pesaram no desempelho:
    * a complexidade do algoritmo.
    * geradores apresentam melhores resultados do que as funcoes tradicionais.

A performance do calculo da serie de fibonacci usando um laco que preenche um
dicionario e muito mais eficiente do que a versao usando recursao, que faz
muitas chamadas de funcao.

O modulo timeit serve para fazer benchmark de pequenos trechos de codigo. O
modulo timeit server para fazer benchmark de pequenos trechos de codigo. Foi
projetado para enviar as falhas mais comuns que afetam programas usados para
fazer benchmarks.

A list comprehension e mais eficiente do que o laco tradicional
algumas dicas sobre simples:
    * mantenha o codigo simples
    * otimize apenas o codigo onde a perfromance da aplicacao e realmente critica
    * use ferramentas para identificar os gargalos no codigo
    * evite funcoes recursivas
    * use os recursos nativos da linguagem. As listas e os dicionarios do python sao muito otimizados
    * use list comprehensions em vez de lacos para processar listas usando expressoes simples
    * evite funcoes dentro de lacos. Funcoes podem receber e devolver listas
Use geradores em vez de funcoes para grandes sequencias de dados.
"""
