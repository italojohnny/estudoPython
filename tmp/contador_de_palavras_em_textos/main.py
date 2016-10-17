import re

total = {}
regex = re.compile('[A-Za-zÀ-úç]+')

with open('exemplo2.txt', 'r') as arquivo:
#with open('/home/zak/Documents/leitura/biblia/40_Mateus.txt', 'r') as arquivo:
    linha = arquivo.read()
    palavras = linha.split()
    for palavra in palavras:
        result = regex.search(palavra)
        if result:
            word = result.group(0)

            if word.lower() in total.keys():
                total[word.lower()] += 1
            else:
                total[word.lower()] = 1
    arquivo.close()

lista = [[k, v] for k, v in total.items()]
novalista = sorted(lista, key=lambda x: x[1], reverse=True)
for i in novalista:
    print(i[0], ":", i[1])



