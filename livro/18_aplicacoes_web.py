#!/usr/python3.5
"""
APLICACOES WEB
e uma aplicacao cliente-servidor na qual o cliente e o browser (como o mozilla
firefox) e o protocolo utilizado para a comunicacao com o servidor e chamado
hypertext Transfer Protocol (http), tecnologias que servem de base para a workd
wide web (www), as paginas de hipertexto que fazem parte da internet. Tais
paginas seguem as convencoes da linguagem hypertexto markup language (html).
As aplicacoes web geram as paginas html dinamicamente, atendendo as requisicoes
enviadas pelo browser. Se construidas da forma adequada, estas aplicacoes podem
ser acessadas em varios ambientes diferentes, de computadores pessoas ate pdas e
celulares.
A biblioteca-padrao de python contem um servidor e um cliente http que podem ser
incorporados em aplicacoes.
"""
# exemplo de servidor
from http.server import HTTPServer, SimpleHTTPRequestHandler
from cgi import escape
from urllib.parse import unquote_plus
from sys import exc_info

page = '''
<!DOCTYPE html>
<html lang="pt-br">
   <head>
        <meta charset="utf-8"/>
        <title>aplicacao web</title>
    </head>
    <body>
        <form action="/">
            comando:
            <input type="text" name="cmd" value="%s" />
            <input type="submit" />
        </form>
        <p>Resposta: %s</p>
    </body>
</html>
'''

class cachorro (SimpleHTTPRequestHandler):
    def do_GET (self):
        cmd = out = ''
        if '?cmd=' in self.path:
            cmd = self.path.split('?cmd=')[-1]
        print(cmd, end=' ')
        if cmd:
            try:
                out = eval(cmd.encode('utf8'))
            except:
                out = exc_info()[0]
        print('=>', out)
        res = page % (escape(cmd), escape(repr(out)))
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(res))
        self.end_headers()
        self.wfile.write(res.encode('utf8'))
        return

httpd = HTTPServer(('127.0.0.1', 8000), cachorro)
print('Servidor na porta 8000')
httpd.serve_forever()

"""
A saida pode ser acessada por um browser no endereco http://localhost:8000/.
Existem muitos frameworks para facilitar o desenvolvimento de aplicativos web
em python, como pyramid, flask e django.
"""
