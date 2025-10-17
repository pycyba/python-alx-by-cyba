# Wielowątkowy serwer TCP - obsługuje nowych klientów w oddzielnych wątkach,
# pozwala to na wiele połączeń do tego serwera jednocześnie.
# Na podstawie wzoru od Chat GPT.
import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

def handle_client(conn, addr):
    print(f"[NOWE POŁĄCZENIE] {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"[{addr}] {data.decode()}")
            conn.sendall(data)
    print(f"[ROZŁĄCZONO] {addr}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print(f"[START] Serwer TCP działa na {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"[AKTYWNE POŁĄCZENIA] {threading.active_count() - 1}")
