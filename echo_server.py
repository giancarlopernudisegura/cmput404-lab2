import socket


def main():
    try:
        host = ''
        port = 8080
        sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen(1)
        conn, addr = sock.accept()
        print(conn)
        print(addr)
    except socket.error as err:
        print('connection error:', err)

if __name__ == "__main__":
    main()

