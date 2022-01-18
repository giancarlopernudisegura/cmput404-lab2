import socket
from multiprocessing import Process


def main():
    try:
        with socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM) as sock:
            localhost = ''
            localport = 8080
            payload = 4096
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((localhost, localport))
            sock.listen(1)
            conn, addr = sock.accept()
            with socket.socket(
                    socket.AF_INET,
                    socket.SOCK_STREAM) as sock_google:
                host = 'www.google.com'
                port = 80
                payload = 4096
                sock_google.connect((host, port))
                req = b'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'
                sock_google.send(req)
                google_page = sock_google.recv(payload)
                # send to proxy client
                conn.send(google_page)
    except socket.error as err:
        print('connection error:', err)

if __name__ == "__main__":
    main()

