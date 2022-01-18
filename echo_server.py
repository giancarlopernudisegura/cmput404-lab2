import socket


def main():
    with socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM) as sock:
        try:
            host = ''
            port = 8080
            payload = 4096
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((host, port))
            sock.listen(1)
            conn, addr = sock.accept()
            print(conn.recv(payload))
        except socket.error as err:
            print('connection error:', err)

if __name__ == "__main__":
    main()

