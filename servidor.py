import socket

def run_client():
    server_ip = "127.0.0.1"
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_ip, server_port))
        while True:
            message = input("Tú: ")
            client_socket.send(message.encode())

            if message.lower() == "adiós":
                print("Conexión terminada.")
                client_socket.close()
                break

            response = client_socket.recv(1024).decode()
            print(f"Servidor: {response}")

    except ConnectionRefusedError:
        print("No se pudo establecer conexión. Asegúrate de que el servidor esté en ejecución.")
    except Exception as e:
        print(f"Error: {e}")
        client_socket.close()

if __name__ == "__main__":
    run_client()
