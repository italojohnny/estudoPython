import socket, select, string, sys

if __name__ == "__main__":
    if (len(sys.argv) < 3):
        print 'use: python main.py <hostname> <port>'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    try:
        s.connect((host, port))
    except:
        print 'nao foi possivel conectar'
        sys.exit()


    print 'conectado'

    while 1:
        socket_list = [sys.stdin, s]
        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
        for sock in read_sockets:
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print 'conexao fechada'
                    sys.exit()
                else:
                    sys.stdout.write(data)
            else:
                msg = sys.stdin.readline()
                s.send(msg)
