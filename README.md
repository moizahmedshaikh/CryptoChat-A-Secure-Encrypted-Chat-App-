# 🔐 CryptoChat – A Secure Encrypted Chat App

CryptoChat is a terminal-based, end-to-end encrypted real-time chat application built with Python. It allows multiple clients to connect securely and communicate via encrypted messages over sockets.

---

## 🚀 Features

- 🔒 End-to-End Encryption using Fernet (AES)
- 💬 Real-time chat with multiple clients
- 🔁 Threaded message handling
- 📡 Encrypted broadcasting (server never sees plain text)
- 🖥️ Lightweight terminal interface

---

## 🧰 Tech Stack

- Python 3
- `socket`, `threading`
- `cryptography.fernet` for AES encryption

---

## 🛠 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/CryptoChat.git
cd CryptoChat
```

### 2️⃣ Install required library

```bash
pip install cryptography
```

### 3️⃣ Generate your encryption key (only once)

You can run this in a separate Python script or in the Python shell:

```python
from cryptography.fernet import Fernet
with open("key.key", "wb") as f:
    f.write(Fernet.generate_key())
```

### 4️⃣ Start the Server

```bash
python server.py
```

### 5️⃣ Start one or more Clients (in separate terminals)

```bash
python client.py
```

---

## 🔐 How It Works

- All messages are AES encrypted using **Fernet** before being sent.
- The **server** does not see any decrypted messages – it just forwards encrypted content.
- Clients decrypt the message locally using the shared `key.key`.
- **Threading** is used to handle multiple clients simultaneously.

---

## 📸 Screenshots

> _Coming soon!_  
(You can include terminal screenshots of the encrypted chat in action here.)

---

## 🤝 Contributing

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you'd like to change.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Author

Made with 💙 by **Moiz Ahmed**  
[LinkedIn Profile](https://www.linkedin.com/in/moiz-ahmed-6516b728a/) *(optional)*
