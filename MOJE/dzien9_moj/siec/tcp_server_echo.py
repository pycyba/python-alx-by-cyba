# Na podstawie wzoru od Chat GPT :)
import socket

HOST = '127.0.0.1'  # adres lokalny (localhost)
PORT = 5000         # dowolny, wolny port (>1024)

# Tworzymy gniazdo (socket)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Reuse address (opcjonalnie, przydatne przy częstym restartowaniu)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bindowanie do adresu i portu
server_socket.bind((HOST, PORT))

# Nasłuchiwanie połączeń
server_socket.listen()

print(f"Serwer TCP działa na {HOST}:{PORT}")

# Czekamy na klienta
conn, addr = server_socket.accept()
print(f"Połączono z {addr}")

# Odbieranie i wysyłanie danych
with conn:
    while True:
        data = conn.recv(1024)  # maksymalnie 1024 bajty
        if not data:
            break  # klient się rozłączył
        print(f"Odebrano: {data.decode()}")
        conn.sendall(data)  # odesłanie (echo)

print("Połączenie zakończone.")
