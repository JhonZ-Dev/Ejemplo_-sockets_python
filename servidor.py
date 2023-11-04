import socket

def run_server():
    server_ip = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind((server_ip, server_port))
        server_socket.listen(1)
        print("Esperando conexiones entrantes...")
        client_socket, client_address = server_socket.accept()
        print(f"Conexión establecida desde {client_address}")

        while True:
            message = client_socket.recv(1024).decode()
            print(f"Cliente: {message}")

            if message.lower() == "adiós":
                print("Conexión terminada.")
                client_socket.close()
                break

            response = input("Tú: ")
            client_socket.send(response.encode())

    except Exception as e:
        print(f"Error: {e}")
        server_socket.close()

if __name__ == "__main__":
    run_server()
