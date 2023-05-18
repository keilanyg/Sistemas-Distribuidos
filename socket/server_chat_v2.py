import socket
import sys
import threading

list_clients = []

def new_client(id,conn,address):
    
    list_clients.append({'name':'client_'+str(id),'conn':conn,'address':address})
    
    def thread_function():
        print("Connection from: " + str(address))
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            print("from connected" + str(address) + ": " + str(data))
            #enviando a msg para todos os clientes conectados
            for cli_con in [c['conn'] for c in list_clients]:
                cli_con.send(data.encode())  # send data to the client

        conn.close()  # close the connection
        
    return threading.Thread(target=thread_function, args=())
    
def server_program(num_clients):
    # get the hostname
    #host = socket.gethostname()
    
    port = 8090  # initiate port no above 1024

    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) #SOCK_DGRAM for UDP # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind(('localhost', port))  # bind host address and port together
    
    while num_clients > 0:
        # configure how many client the server can listen simultaneously
        print('Server escutando... Cliente N ' + str(num_clients))
        server_socket.listen(num_clients)
        conn, address = server_socket.accept()  # accept new connection
        #criar nova thread para cada nova conexao
        thread_client = new_client(num_clients,conn,address)
        thread_client.start()
        num_clients = num_clients - 1

if __name__ == '__main__':\
    
    server_program(int(sys.argv[1]))