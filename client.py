import socket


def main():
    try:
        host = 'www.google.com'
        port = 80
        req = b'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'
        MAX_PAYLOAD = 4096

        sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.send(req)
        print(sock.recv(MAX_PAYLOAD))
    except socket.error:
        print('connection error')
    except socket.gaierror:
        print('connection error')

if __name__ == "__main__":
    main()

