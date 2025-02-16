# Chatroom - Multi-Client Chat Application 🗨️

This is a simple multi-client chatroom built using **Python sockets** and **multithreading**.  
It allows multiple users to connect to a chat server and exchange messages in real-time.

## 🚀 Features
- Supports **multiple clients**.
- Uses **multithreading** for smooth communication.
- Broadcasts messages to all connected users.
- Assigns **aliases** (usernames) to clients.

## 🛠️ Prerequisites
- Python 3.x installed
- Basic knowledge of Python sockets and threading

## ⚙️ How to Run

### 1️⃣ Start the Server
Run the following command:
```sh
python server.py
```

### 2️⃣ Start the Client
Run the following command:
```sh
python client.py
```

## How It Works
- The server listens for connections on `127.0.0.1:59000`.
- Clients connect and provide an alias (username).
- Messages from one client are broadcast to all others.
- When a user disconnects, it notifies everyone in the chat.

## 🛠️ Technologies Used
- **Python**
- **Sockets**
- **Multithreading**