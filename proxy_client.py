import socket


def main():
    try:
        host = 'localhost'
        port = 8080
        req = b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n'
        MAX_PAYLOAD = 4096

        sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM)
        sock.connect((host, port))
        response = sock.recv(MAX_PAYLOAD)
        print(response)
    except socket.error:
        print('connection error')
    except socket.gaierror:
        print('connection error')

if __name__ == "__main__":
    main()

