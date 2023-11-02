import socket
# Configuración del cliente
server_ip = "127.0.0.1"
server_port = 12345

# Crear un socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client_socket.connect((server_ip, server_port))
