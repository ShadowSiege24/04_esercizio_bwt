import socket
from bwt import bwt

def start_server(host="127.0.0.1", port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host,port))
        server.listen()

        print("Server in ascolto...")
        print("Socket in ascolto: ", server.getsockname())

        connection, address = server.accept()

        with connection:
            print("Client connesso:", address)

            print("Socket di connessione", connection.getsockname())

            messaggio = connection.recv(1024)
            print("Messaggio ricevuto: ", messaggio.decode())


            connection.sendall(messaggio)


print(start_server)

