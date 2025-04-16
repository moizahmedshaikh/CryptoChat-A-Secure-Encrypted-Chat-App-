import socket
import threading
from cryptography.fernet import Fernet

def load_key():
    return open("key.key", "rb").read()

key = load_key()
cipher = Fernet(key)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5555))

def recieve_message():
    while True:
        try:
            encrypted_msg = client.recv(1024)
            if encrypted_msg:
                decrypted_msg = cipher.decrypt(encrypted_msg).decode()
                print(f"\n📨 Friend: {decrypted_msg}")

        except Exception as e:
            print("❌ Disconnected from server.")
            client.close()
            break


def send_message():
    while True:
        msg = input("You: ")
        encrypted_msg = cipher.encrypt(msg.encode())
        client.send(encrypted_msg)

receive_thread = threading.Thread(target=recieve_message)
receive_thread.start()

send_thread = threading.Thread(target=send_message)
send_thread.start()