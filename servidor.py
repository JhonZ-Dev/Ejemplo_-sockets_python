import socket
# Configuración del servidor
server_ip = "127.0.0.1"
server_port = 12345
# Crear un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket a la dirección IP y puerto
server_socket.bind((server_ip, server_port))
# Escuchar conexiones entrantes
server_socket.listen(1)
print("Esperando conexiones entrantes...")
# Aceptar una conexión entrante
client_socket, client_address = server_socket.accept()
print(f"Conexión establecida desde {client_address}")
while True:
    # Recibir mensaje del cliente
    message = client_socket.recv(1024).decode()
    print(f"Cliente: {message}")

    # Enviar respuesta al cliente
    response = input("Tú: ")
    client_socket.send(response.encode())

    if response.lower() == "adiós":
        print("Conexión terminada.")
        client_socket.close()
        break