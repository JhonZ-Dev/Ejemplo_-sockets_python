# Python Sockets Example

This is a basic example showcasing communication via sockets in Python. The code consists of a client and a server communicating with each other using TCP/IP sockets.

## Requirements

- Python 3.10

## Usage

### Server

1. Run the `server.py` file.
2. The server will be waiting for incoming connections.
3. Once a connection is established with a client, the server will await messages from the client and respond to them.

### Client

1. Run the `client.py` file.
2. The client will connect to the server.
3. Enter messages, which will be sent to the server.
4. The client will receive and display responses from the server.

## Implemented Improvements

- Exception handling to detect and manage potential errors during connection and communication.
- Code structured into separate functions for readability and organization.
- Console status messages indicating established connections and their closure.

## Notes

- The client and server are configured to communicate on `localhost` (127.0.0.1) and port `12345`. You can modify these variables to suit your needs.
- The client can terminate the connection by entering "adiós".

## Contributions

Feel free to contribute to the project by providing enhancements, bug fixes, or suggestions. If you wish to add new features, fork the project and submit a pull request.

## Author

Created by [jhonZambrano1999] - [https://github.com/jhonZambrano1999/Ejemplo_-sockets_python/edit/main/README.md].
