# Socket Programming Examples in Python 🚀

This project contains three Python scripts demonstrating **basic socket programming**:
- `main.py` → Connects to **GitHub's web server** (www.github.com) using **TCP**.
- `server.py` → Implements a **simple TCP server** that listens for connections.
- `client.py` → Implements a **TCP client** that connects to the server and receives a message.

---
---

## 🛠️ Prerequisites
- **Python 3.x** installed
- Basic understanding of **networking and sockets**

---

## ⚙️ How to Run

### 1️⃣ Running `main.py`
This script connects to **GitHub's web server** on **port 80**.
```sh
python main.py
```
# TCP Server and Client

## 2️⃣ Running the Server (`server.py`)

This script starts a TCP server on port `56789`.

### Command to Run:

```sh
python server.py

```

## 3️⃣ Running the Client (client.py)

This script connects to the server on `127.0.0.1:56789`.
### Command to Run:

```sh
python client.py

```

## 📜 How It Works

### 🔹 `main.py`
- Creates a TCP socket.
- Resolves GitHub's IP address.
- Establishes a connection to GitHub's web server (port 80).

### 🔹 `server.py`
- Creates a TCP socket and binds it to port `56789`.
- Listens for incoming connections.
- Sends a welcome message to the connected client.

### 🔹 `client.py`
- Creates a TCP socket.
- Connects to the server (`127.0.0.1:56789`).
- Receives and prints the server's message.

