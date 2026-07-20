---
title: Networking and Web
tags: [networking, sockets, http, requests, urllib, ssl, security]
status: complete
source: Official Python docs, socket/http/urllib modules
last_updated: 2026-07-20
---

# Networking and Web

Python supports low-level socket operations as well as high-level application protocols (like HTTP) out of the box, facilitating robust network client and server development.

## Low-Level Interfaces (`socket`)

Sockets are standard endpoints for sending and receiving data across a network.

### Simple TCP Echo Server
```python
import socket

# Create socket, bind to local address, and listen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8080))
server_socket.listen(1)

print("Server is listening on port 8080...")

try:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)  # Echo back
finally:
    server_socket.close()
```

### Simple TCP Client
```python
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))

client_socket.sendall(b"Hello, Server!")
response = client_socket.recv(1024)
print("Received from server:", response.decode())
client_socket.close()
```

## High-Level HTTP and URL Operations (`urllib`)

The `urllib.request` module allows parsing URLs, fetching web resources, and sending POST/GET requests.

```python
import urllib.request
import urllib.parse

# 1. Basic GET request with explicit timeout
url = "https://api.github.com/users/octocat"
headers = {"User-Agent": "Python-urllib"}

req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode('utf-8')
        print(html[:100])  # Print first 100 characters
except urllib.error.URLError as e:
    print("Failed to reach server:", e.reason)
```

## Security Best Practices

### 1. Always Enforce SSL/TLS Certificate Verification
When fetching remote data, always ensure the server's certificate is verified to prevent Man-in-the-Middle (MitM) attacks.
* `urllib.request.urlopen` verifies certificates by default. Do not disable this by passing custom unverified SSL contexts.
* **Bad**: `ssl._create_unverified_context()`

### 2. Set Explicit Timeouts
By default, standard library functions (like socket connections and `urllib.request.urlopen`) can wait indefinitely if the connection hangs. This can lead to denial of service due to thread/resource exhaustion.
* **Bad**: `urllib.request.urlopen("https://example.com")` (no timeout specified)
* **Good**: `urllib.request.urlopen("https://example.com", timeout=10)` (fails if connection takes > 10 seconds)

### 3. Server-Side Request Forgery (SSRF) Protection
If your application accepts a URL from a user and fetches it, an attacker can supply local IP addresses (e.g. `http://127.0.0.1` or `http://169.254.169.254` for AWS metadata) to read internal data.
* **Best Practice**: Validate user-supplied URLs against an allowlist of domains, or resolve IP addresses and block private/loopback address blocks (e.g., `10.0.0.0/8`, `127.0.0.0/8`, `169.254.0.0/16`, `172.16.0.0/12`, `192.168.0.0/16`).

## External Libraries

- **`requests`**: A widely popular third-party HTTP client that is highly readable, feature-rich, and automatically handles cookie persistence, redirection, and keep-alive. Installable via PyPI.
