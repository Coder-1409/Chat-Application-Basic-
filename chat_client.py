import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print(f"Connected to server at {HOST}:{PORT}")

def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"\nServer: {data.decode()}\nYou: ", end="")
        except:
            break

def send_messages():
    while True:
        message = input("You: ")
        client_socket.sendall(message.encode())

receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()

client_socket.close()
