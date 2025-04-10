import bluetooth


def start_bluetooth_server():
    # Create a Bluetooth socket
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    # Bind the socket to any Bluetooth adapter and a port (use port 1 by convention)     
    server_socket.bind(("", bluetooth.PORT_ANY))
    server_socket.listen(1)  # Listen for one connection at a time

    print("Waiting for Bluetooth connection...")

    # Accept an incoming connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                break
            print(f"Received: {data}")

            # Optional: Respond to the client
            response = "Command received: " + data
            client_socket.send(response.encode("utf-8"))
    except OSError as e:
        print(f"Connection closed: {e}")
    finally:
        client_socket.close()
        server_socket.close()
        print("Bluetooth server shut down.")

if __name__ == "__main__":
    start_bluetooth_server()
