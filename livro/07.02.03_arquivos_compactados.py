#!/usr/python3.5
# o python contem modulos para trabalhar com varios formatos de arquivos compactados
import zipfile

texto = """****************************************
Esse e o texto que sera compactado e...
... guardado dentro de um arquivo zip.
****************************************
"""
# gravacao de um arquivo zip
zip = zipfile.ZipFile('arq.zip', 'w', zipfile.ZIP_DEFLATED) # cria zip
zip.writestr('texto.txt', texto.encode('utf8')) # escreve dentro do zip um arquivo txt e passa seu conteudo 
zip.close() # fecha zip

# leitura de um arquivo zip
zip = zipfile.ZipFile('arq.zip') # abre o zip
arqs = zip.namelist() # gera lista de arquivos dentro do zip
for arq in arqs: # percorre essa lista
    print('arquivo: ', arq) # imprime nome do arquivo
    zipinfo = zip.getinfo(arq) # pega varias informacoes do atual arquivo
    print('tamanho original: ', zipinfo.file_size)
    print('tamanho comprimido: ', zipinfo.compress_size)
    print(zip.read(arq).decode('utf8'))

# tambem prove modulos  para os formatos gzip, bzip2 e tar, bastante usado em unix.
