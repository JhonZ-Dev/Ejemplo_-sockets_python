import socket
# Configuración del servidor
server_ip = "127.0.0.1"
server_port = 12345
# Crear un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket a la dirección IP y puerto
server_socket.bind((server_ip, server_port))