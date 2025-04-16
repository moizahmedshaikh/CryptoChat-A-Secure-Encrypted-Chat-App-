import socket
import threading
from cryptography.fernet import Fernet

def load_key():
    return open("key.key", "rb").read()

key = load_key()
cipher = Fernet(key)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5555))
server.listen()

clients = []

def broadcast(message,sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)


def handle_client(conn, addr):
    print(f"✅ New connection from {addr}")
    while True:
        try:
            encrypted_msg = conn.recv(1024)
            if not encrypted_msg:
                break
            decrypted_msg = cipher.decrypt(encrypted_msg).decode()
            print(f"📥 {addr}: {decrypted_msg}")
            broadcast(encrypted_msg, conn)
        except Exception as e:
            print(f"❌ Error with {addr}: {e}")
            break

    conn.close()
    clients.remove(conn)
    print(f"🔌 {addr} disconnected")

def start():
    print("🚀 Server started, waiting for connections...")
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

start()
