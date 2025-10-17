# Też ChatGPT, ale pomysł na program mój :)

import socket
import threading
import datetime
import random

HOST = '127.0.0.1'
PORT = 5000

def handle_client(conn, addr):
    print(f"[NOWE POŁĄCZENIE] {addr}")

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            message = data.decode().strip()
            if not message:
                continue

            print(f"[{addr}] {message}")

            # Podział na komendę i argumenty
            parts = message.split(maxsplit=1)
            command = parts[0].lower()
            arg = parts[1] if len(parts) > 1 else ""

            # Obsługa poleceń
            if command == "echo":
                response = arg

            elif command == "time":
                now = datetime.datetime.now()
                response = now.strftime("%H:%M:%S")

            elif command == "date":
                today = datetime.date.today()
                response = today.strftime("%Y-%m-%d")

            elif command == "random":
                response = str(random.randint(1, 1000))

            else:
                response = f"Nieznane polecenie: {command}"

            # Odesłanie odpowiedzi + nowa linia
            conn.sendall((response + "\n").encode())

    print(f"[ROZŁĄCZONO] {addr}")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[START] Serwer TCP działa na {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        thread.start()
        print(f"[AKTYWNE POŁĄCZENIA] {threading.active_count() - 1}")

if __name__ == "__main__":
    main()
