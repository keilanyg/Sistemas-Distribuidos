import socket


def client_program():
    #host = socket.gethostname()  # as both code is running on same pc
    port = 8090  # socket server port number

    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)  # instantiate
    client_socket.connect(('localhost', port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()