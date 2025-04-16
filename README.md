# 🔐 CryptoChat - A Secure End-to-End Encrypted Chat App

CryptoChat is a terminal-based secure chat application built with Python. It uses **Socket Programming** for real-time communication and **Fernet encryption (from the cryptography library)** for end-to-end message security between multiple clients.

## ✨ Features

- 🔒 End-to-End AES Encryption (Fernet)
- 📡 Real-time Communication with Socket Programming
- 👥 Multi-client support with threading
- 💬 Encrypted Message Broadcasting
- 📁 Simple and lightweight — pure Python!

## 🛠️ Tech Stack

- Python 3
- socket (for server-client communication)
- threading (for handling multiple clients)
- cryptography.fernet (for encryption & decryption)

## 📁 Project Structure

secure-chat/ ├── key.key # Encryption key (auto-generated) ├── server.py # Server code ├── client.py # Client code └── README.md # Project documentation

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/cryptochat.git
cd cryptochat
2️⃣ Install required library
bash
Copy
Edit
pip install cryptography
3️⃣ Generate your encryption key (only once)
bash
Copy
Edit
# Run inside Python shell or create a script
from cryptography.fernet import Fernet
with open("key.key", "wb") as f:
    f.write(Fernet.generate_key())
4️⃣ Start the Server
bash
Copy
Edit
python server.py
5️⃣ Start one or more Clients (in separate terminals)
bash
Copy
Edit
python client.py
🔐 How It Works
All messages are AES encrypted using Fernet before being sent over the network.

The server never sees decrypted messages — it simply forwards encrypted data.

Clients decrypt the messages locally with the shared secret key (key.key).

Threading enables multiple clients to chat simultaneously.

📸 Screenshots
Coming soon! (You can add terminal screenshots of chat)

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

📜 License
This project is licensed under the MIT License.

🙌 Author
Made with 💙 by Moiz Ahmed