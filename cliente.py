import socket
# Configuración del cliente
server_ip = "127.0.0.1"
server_port = 12345

# Crear un socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client_socket.connect((server_ip, server_port))

while True:
     # Enviar un mensaje al servidor
    message = input("Tú: ")
    client_socket.send(message.encode())
    # Recibir mensaje del servidor
    response = client_socket.recv(1024).decode()
    print(f"Servidor: {response}")
    if message.lower() == "adiós":
        print("Conexión terminada.")
        client_socket.close()
        break
