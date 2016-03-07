#!/usr/bin/env python

import sys
import os
import signal
import time
import subprocess


host = "127.0.0.1"
port = "5038"
user = "mesa"
keyw = "jkmo1010"
pathpid = '/tmp/ami.pid'

def start():
    if status() == 1:
        print 'start...'
        pid = os.fork()
        if pid:
            filepid = open(pathpid, 'w')
            filepid.write('%s\n' % pid)
            filepid.close()
            sys.exit(0)
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout = open('/dev/null', 'w')
        sys.stderr = open('/dev/null', 'w')
        rotina()
    else:
        print 'ja esta em execusao'

def stop():
    if status() == 0:
        print 'stop...'
        try:
            filepid = open(pathpid, 'r')
            while True:
                os.kill(int(filepid.readline()[:-1]), signal.SIGTERM)#melhorar tratamento aqui 
                time.sleep(1)
            filepid.close()
        except:
            os.remove(pathpid)
    else:
        print 'ja esta parado'

def status():
    try:
        filepid = open(pathpid, 'r')
        filepid.close
        return 0
    except:
        return 1

def make_dict(txt):
    new_dict = {}
    new_list = txt.splitlines()
    for i in new_list:
        if i != '':
            aux = i.split(':')
            if len(aux) > 1:
                new_dict[aux[0]] = aux[1][1:] # esse [1:] e para remover o primeiro caracter, um espaco
            else:
                new_dict[aux[0]] = aux[0]
    return new_dict

def rotina():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    s.connect((host, int(port)))# E NECESSARIO ESSES DOIS PARENTESES

    s.send("action: login\n")
    s.send("username: %s\n" % user)
    s.send("secret: %s\n\n\n" % keyw)

    while 1:
        socket_list = [sys.stdin, s]
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])

        for sock in read_sockets:
            if sock == s:
                data = sock.recv(4096)
                if data :
                    if re.search('Event: PeerStatus', data):
                        temporario = make_dict(data)
                        print 'chama subprocesso para gravar'
                        subprocess.call("xxx", shell=True)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 'start':
            start()

        elif sys.argv[1] == 'stop':
            stop()

        elif sys.argv[1] == 'status':
            if status() == 0:
                print '...rodando'
            else:
                print '...parado'

        elif sys.argv[1] == 'restart':
            stop()
            start()

        else:
            print 'parametro desconhecido'
            sys.exit(2)
    else:
        print 'Use um parametro: {start | stop | restart | status}'
        sys.exit(1)

