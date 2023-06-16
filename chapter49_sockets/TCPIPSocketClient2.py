import socket


def main():
    print('Starting Client')
    print('Create a TCP/IP socket')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Connect the socket to the server port')
    server_address = ('localhost', 8084)
    print('Connecting to: ', server_address)
    try:
        sock.connect(server_address)
        print('Connected to server')
        print('Send data')
        message = 'John'
        print('Sending: ', message)
        sock.send(message.encode())
        data = sock.recv(1024).decode()
        print('Received from server: ', data)
    except ConnectionRefusedError as err:
        print(f'Error connecting to server: {err}')
    except Exception as exp:
        print(f'Something went wrong: {exp}')
    finally:
        print('Closing socket')
        sock.close()


if __name__ == '__main__':
    main()
