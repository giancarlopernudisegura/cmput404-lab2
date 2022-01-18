#!/bin/env python
import socket
from multiprocessing import Process

MAX_CONECTIONS = 3
BUFF_SIZE = 4096


def main():
    try:
        with socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM) as sock:
            localhost = ''
            localport = 8080
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((localhost, localport))
            connections = []
            for _ in range(MAX_CONECTIONS):
                sock.listen(2)
                conn, addr = sock.accept()
                p = Process(target=handle_conn, args=(conn, addr))
                p.daemon = True
                p.start()
                connections.append(p)
                print(f'started process {p}')
            for p in connections:
                p.join()
    except socket.error as err:
        print('connection error:', err)

def handle_conn(conn, addr):
    try:
        with socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM) as sock_google:
            host = 'www.google.com'
            port = 80
            sock_google.connect((host, port))
            req = b'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'
            sock_google.send(req)
            google_page = sock_google.recv(BUFF_SIZE)
            # send to proxy client
            conn.sendall(google_page)
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
    except socket.error as err:
        print('connection error:', err)


if __name__ == "__main__":
    main()

