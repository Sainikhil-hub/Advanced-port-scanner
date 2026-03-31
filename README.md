# 🔍 Advanced Port Scanner (Python)

A multi-threaded port scanner built using Python that scans a target system for open TCP ports and identifies running services.

---

## 🚀 Features

* ⚡ Multi-threaded scanning for faster performance
* 🎯 User-defined target and port range
* 🧠 Service detection (HTTP, MySQL, etc.)
* 📡 Basic banner grabbing
* 💾 Optional result saving to file
* 🖥️ Supports both CLI mode and interactive input

---

## 🛠️ Tech Stack

* Python 3
* Socket Programming
* Threading

---

## 📌 How It Works

This tool attempts to establish a TCP connection with each port in the given range:

* If connection succeeds → port is **OPEN**
* If connection fails → port is **CLOSED**

It also tries to:

* Identify the service running on the port
* Capture basic banner information (if available)

---

## ⚙️ Usage

### 🔹 CLI Mode (Recommended)

```bash
python3 scanner.py -t 127.0.0.1 -sp 1 -ep 100
```

### 🔹 Save Output to File

```bash
python3 scanner.py -t 127.0.0.1 -sp 1 -ep 100 -o result.txt
```

### 🔹 Interactive Mode

```bash
python3 scanner.py
```

---

## 📊 Example Output

```
[+] Port 80 OPEN (http)
[+] Port 3306 OPEN (mysql)
[+] Port 8080 OPEN (http-alt)

==================================================
Scan Summary:
Total Open Ports: 3
Ports: [80, 3306, 8080]
==================================================
Scan Complete.
```

---

## 🧠 What I Learned

* Fundamentals of TCP/IP and ports
* Socket programming in Python
* Multi-threading for performance optimization
* Basic reconnaissance techniques used in cybersecurity

---

## ⚠️ Disclaimer

This tool is developed for **educational purposes only**.
Do not use it on networks or systems without proper authorization.

---

## 🔮 Future Improvements

* Add IP range scanning (network-wide scanning)
* Add colored terminal output
* Implement thread pool control
* Enhance banner analysis

---


