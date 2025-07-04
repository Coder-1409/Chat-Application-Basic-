import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server listening on {HOST}:{PORT}...")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

def receive_messages():
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print(f"\nClient: {data.decode()}\nYou: ", end="")
        except:
            break

def send_messages():
    while True:
        message = input("You: ")
        conn.sendall(message.encode())

receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()

conn.close()
