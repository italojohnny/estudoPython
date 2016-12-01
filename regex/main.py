PYTHON

	Caracteristica | Descricao
	---------------+-------------------------------------------
             Busca | Funcoes re.search, re.findall, re.finditer
      Substituicao | Funcao re.sub
           Divisao | Funcao re.split
           ER crua | r'raw string'
        Ignore M/m | Modificadores (?i), re.I
            Global | E o padrao

Python possui um dos mais completos suportes as expressoes regulares, com objetos e metodos ja prontos para obter diversas informacoes sobre os casamentos. O primeiro passo e carregar o modulo re, responsavel pelo tratamento das expressoes:

	import re

Antes de comecar, uma dica muito importante: sempre coloque suas expressoes dentro de "raw strings" (r'...') para torna-las cruas, evitando assim os infindaveis problemas com escapes. Acostume-se a sempre usar esta notacao, mesmo quando sua expressao for simples e nao possuir nenhuma contrabarra.

Para testar se uma expressao casou ou nao em determinado texto (ou variavel), use a funcao search.

	if re.search(r'^Py', 'Python'):
		print 'Casou'
	else:
		print 'Nao casou'

Alem de somente testar se casou ou nao, esta funcao tambem retorna um objeto com informacoes sobre o casamento. Guarde o resultado em uma variavel para poder acessa-lo depois. E pratica comum na comunidade Python chamar esta variavel de m, uma abreviacao para match.

	m = re.search(r'^Py', 'Python')
	if m:
		print 'Casou'
	else:
		print 'Nao casou'

Com o resultado guardado, agora podemos usar seus metodos para obter informacoes uteis, como o trecho casado e os indices.

	m = re.search(r'^Py', 'Python')
	if m:
		print m.group() # Py
		print m.start() # 0
		print m.end()   # 2
		print m.span()  # (0, 2)

O metodo group traz o trecho de texto casado pela expressao. Com os metodos start e end, voce obtem a posicao de inicio e fim do trecho casado na string original. O metodo span e similar, porem ja traz ambas as posicoes dentro de uma tupla. Lembra-se de que em Python os indices iniciam em zero.

Se sua expressao contem grupos, alem das informacoes do casamento como um todo (considerado grupo zero), voce tambem pode obter informacoes sobre cada um dos grupos, informando seu numero. Ha tambem o metodo groups que retorna uma tupla com o conteudo casado de todos os grupos.

	m = re.search(r'(..)/(..)/(....)', '31/12/1999')
	if m:
		print m.group(0) # 31/12/1999
		print m.group(1) # 31
		print m.group(2) # 12
		print m.group(3) # 1999
		print m.span(0)  # (0, 10)
		print m.span(1)  # (0, 2)
		print m.span(2)  # (3, 5)
		print m.span(3)  # (6, 10)
		print m.groups() # ('31', '12', '1999')

E se a expressao casar mais de uma vez no texto? Para encontrar todas as ocorrencias, use a funcao findall. Ela retorna uma lista com todos os trechos de texto casados pela expressao, ou uma lista vazia, se nao casar.

	texto = "Corri 3km em 15 minutos, ouvindo CPM 22."
	print re.findall(r'\d+', texto) # ['3', '15', '22']
	print re.findll(r'XXX', texto)  # []

Se houver grupos na expressa, o retorno da funcao sera uma lista de tuplas. Cada tupla representa um casamento, trazendo o conteudo de todos os seus grupos.

	texto = "Acordei as 08:00, comi 12:30, dormi as 23:59."
	print re.findall(r'(\d\d):(\d\d', texto)

	# Resultado:
	# [('08', '00'), ('12', '30'), ('23','59')]

Uma maneira mais sofisticada de se lidar com multiplas ocorrencias e fazer um loop nos casamento, usando a funcao finditer. Voce pode inspecionar cada ocorrencia, usando aqueles metodos bacanas que ja vimos anteriormente, como group e span.

	texto = "Acordei as 08:00, comi 12:30, dormi as 23:59."
	for m in re.finditer(r'(\d\d):(\d\d)', texto):
		hora = m.group(1)
		min = m.group(2)
		print "%s horas, %s minutos." % (hora, min)

	# Resultado:
	# 08 horas, 00 minutos.
	# 12 horas, 30 minutos.
	# 23 horas, 59 minutos.

Um metodo util de se utilizar dentro de loops e o expand, que funciona de maneira similar a substituicao, expandindo os retrovisores (\1, \2, ...).

Nao se esqueca de usar "raw string"! Veja como o exemplo anterior fica mais simples:

	texto = "Acordei as 08:00, comi 12:30, dormi as 23:59."
	for m in re.finditer(r'(\d\d):(\d\d)', texto):
		print m.expand(r'\1 horas, \2 minutos')

A substituicao e feita pela funcao sub, que troca toddas as ocorrencias encontradas. Ela aceita um terceiro argumento opcional para limitar o numero de substituicoes a serem feitas:

	print re.sub(r'\w', '.', 'Python')    # ......
	print re.sub(r'\w', '.', 'Python', 2) # ..thon

Os retrovisores sao referenciados normalmente, usando a contrabarra. Por isso, lembres-se de tambem colocar o texto substituto dentro de uma "ram string", para evitar problemas de escape.

	print re.sub(r'(Py).*', r'\1\1', 'Python') #PyPy

Uma sintaxe alternativa para os retrovisores e \g<1>, \g<2>, util quando voce precisa usar um numero literal longo apos o retrovisor.


	print re.sub(r'(Py).*', r'\13', 'Python')    # erro
	print re.sub(r'(Py).*', r'g\<1>3', 'Python') # Py3

Para substituicoes realmente estilosas, voce pode usar uma funcao no lugar do texto substituto. Esta funcao recebera uma instancia de MatchObject para cada ocorrenca e deve retornar uma string.

	def data_por_extenso (m):
		dia = m.group(1)
		mes = m.group(2)
		ano = m.group(3)
		meses = {
			'01':'Jan',	'02':'Fev',	'03':'Mar',	'04':'Abr',	'05':'Mai',	'06':'Jun',
			'07':'Jul',	'08':'Ago',	'09':'Set',	'10':'Out',	'11':'Nov',	'12':'Dez',
		}
		return dia + " de " + meses[mes] + " de " + ano

	texto = "Hoje e dia 31/12/1999"
	regex = r'(\d\d)/(\d\d)/(\d\d\d\d)'
	print re.sub(regex, data_por_extenso, texto)
	# Hoje e dia 31 de Dez de 19999.

Para dividir um texto usando expressoes regulares, use a funcao split, que retorna uma lista de strings. Um terceiro argumento opcional pode ser informado para limitar o numero de vezes que o texto vai ser dividido. Neste caso, o ultimo item da lista trara o texto restante, que ficou sem corte.

	print re.split(r'[/.]', '31/12/99')    # ['31', '12', '99']
	print re.split(r'[/.]', '31/12/99', 1) # ['31', '12/99']

SE voce for ultilizar a mesma expressao mais de uma vez, e possivel compilar-la para garantir uma execucao mais rapida. O objeto retornado da compilacao tem os mesmos metodos do modulo re, entao voce pode casar, substituir e dividir textos usando expressoes regulares compiladas.

	# Primeiro compile as expressoes
	er_hora = re.compile(r'(\d\d):(\d\d)')
	er_separador = re.compile(r'[/.:]')

	# Agora pode usa-las diretamente para pesquisar
	if er_hora.search('23:59'):
		print 'Casou'

	# Para substituir
	print er_hora.sub(r'\1h\2min', '23:59') # 23h59min

	# E para dividir
	print er_separador.split('1.23')     # ['1', 23]
	print er_separador.split('23:59)     # ['23', '59']
	print er_separador.split('31/12/99') # ['31', '12', '99']

Flags
Para ignorar a diferenca entre maiusculas e minusculas, voce precisa adicionar uma flag a expressao. Ha duas maneiras de se fazer isso: usar o grupo modernoso (?i) no inicio da expressao, ou passar as constantes re.I ou re.IGNORECASE as funcoes.

	if re.search(r'(?i)^py', 'Python'):
		print 'Casou'

	if re.search(r'^py', 'Python', re.IGNORECASE):
		print 'Casou'

Nao recomendo o uso de constantes pois ele e especifico do Python e nem todas as funcoes o suportam. Prefira sempre a primeira forma (?i), pois, alem de manter tudo dentro da propria expressao, esse formato e padrao e funciona em outras linguagens.

Sempre coloque este gurpo especial bem no incio da expressao para evitar problemas, e se voce precisar usar mais de uma flag ao mesmo tempo, basta juntar as letras dentro do mesmo grupo:(?iux).

E com flags que resolvemos problemas de acentuacao tambem. O Python nao tem classes POSIX (como [:alpha:] e amigos), mas possui o barra-letra \w, que casara letras acentuadas se os planetas estiverem bem alinhados :)

Tudo depende da configuracao de seu sistema, da versao do Python e da codificacao do texto original. Ha duas flags que voce pode usar: (?L) para levar em conta a localizacao  de seu sistema, e (?u) para levar em conta a tabela Unicode.

Surgiro testar as combinacoes e ver qual funciona para o seu ambiente. Para o futuro, e melhor sempre manipular o texto como Unicode e usar a flag (?u). Estes sao os resultados em meu sistema atual (Python 2.7.1, LANG=pt_BR.UTF-8):

	print re.search(r'\w',     '.',  'Páiton') # .á....
	print re.search(r'(?L)\w', '.',  'Páiton') # .á....
	print re.search(r'(?u)\w', '.',  'Páiton') # ..?...
	print re.search(r'\w',     '.', u'Páiton') # .á....
	print re.search(r'(?L)\w', '.', u'Páiton') # .á....
	print re.search(r'(?u)\w', '.', u'Páiton') # .á.... OK

Ha duas flags especiais para lidar com strings de multiplas linhas. Use (?s) para fazer o metacaractere ponto casar o \n, o que normalmente nao acontece. Assim, o seu curinga .* vai casar a string toda. Use (?m) para fazer as ancoras ^ e $ casarem cada uma das linhas da string.

	# Flag (?s) para o . casar o \n
	re.sub(r'.*',     '.', '1\n2\n3) # .\n.\n.
	re.sub(r'(?s).*', '.', '1\n2\n3) # .

	# Flag (?m) para usar ^ e $ em todas as linhasn
	re.sub(r'^2',     '.', '1\n2\n3) # 1\n2\n3
	re.sub(r'(?m)^2', '.', '1\n2\n3) # 1\n.\n3

E caso sua expressao fique realmente grande e complexa, use a flag (?x), que permite que voce organize sua expressao em varias linhas, com alinhamento e comentarios. Os espacos em branco e Tabs sao ignorados e o caractere # e usado para iniciar um comentario. Para inserir espaco literais, voce deve escapa-los ou usar \s.

	# Numeros de telefone no formato internacional
	texto = '''
		+554798765432
		+55 47 98765432
		+55 47 9876-5432
		+55 11 9876-5432
	'''

	# Expressao para casar numeros de telefone
	# Nota: Sao duas flags no inicio: 'x' e 'm'
	regex = r'''(?xm)
		^        # Inicio da linha
		\s*      # Espacos opcionais
		\+55     # Codigo do Brasil: +55
		\s?      # Espaco opcional
		[0-9]{2} # Codigo de area (DDD)
		\s?      # Espaco opcional
		9?       # Digito 9 adicional para Sao Paulo
		[0-9]{4} # Quatro primeiros digitos
		-?       # Separador opcional
		[0-9]{4} # Ultimos quatro digitos
		$        # Fim da linha

	'''
	print re.sub(regex, 'casou', texto)
	# Resultado:
	# casou
	# casou
	# casou
	# casou

Grupos nomeados
Em Python voce tambem pode dar nomes aos grupos de sua expressao. Assim, alem dos numeros, voce tambem pode referenciar esses grupos usando o seu nome.

O formato usado para dar um nome ao grupo e feio que doi: (?P<nome>...). Por exemplo, a versao splificada da expressao para casar uma data no formato brasileiro (..)/(..)/(....), colocando nomes nos grupos, fica assim:

	(?P<dia>..)/(?P<mes>..)/(?P<ano>....)

Para usar o retrovisor em grupos normais, voce usa \1 tanto dentro da expressao quando na substituicao. Ja para grupos nomeados, voce deve usar (?P=nome) dentro da expressao e \g<nome> na substituicao.

	# Converte datas de DD/MM/AAAA para AAAA-MM-DD
	data = '31/12/1999'

	# Substituicao usando grupos normais
	print re.sub(
		r'(..)/(..)/(....)',
		r'\3-\2-\1',
	data)

	# Substituicao usando grupos nomeados
	print re.sub(
		r'(?P<dia>..)/(?P<mes>..)/(?<ano>....)',
		r'\g<ano>-\g<mes>-\g<dia>',
	data)

	# Resultado:
	# 19990-12-31
	# 19990-12-31

Os metodos de MatchObject aceitam o nome ou numero do grupo, tanto faz. Perceba que, enquanto o metodo groups retorna uma tupla com todos os grupos, o metodo groupdict retorna um dicionario composto unicamente com os grupos nomeados.

	m = re.search(r'(?P<dia>..)/(?P<mes>..)/(....)', '31/12/1999')
	if m:
		print m.group(0)     # 31/12/1999
		print m.group(1)     # 31
		print m.group(2)     # 12
		print m.group(3)     # 1999
		print m.group('dia') # 31
		print m.group('mes') # 12
		print m.groups()     # ('31', '12', '1999')
		print m.groupdict()  # {'dia': '31', 'mes': '12'}


