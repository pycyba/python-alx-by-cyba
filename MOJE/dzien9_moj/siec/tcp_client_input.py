# Klient TCP, który wysyła na serwer polecenia podane przez użytkownika.
# ChatGPT

import socket

HOST = '127.0.0.1'  # adres serwera
PORT = 5000         # port, na którym działa serwer

def main():
    # Utworzenie gniazda
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        # Połączenie z serwerem
        client.connect((HOST, PORT))
        print(f"Połączono z serwerem {HOST}:{PORT}")
        print("Wpisz komendę (echo, time, date, random) lub 'exit' aby zakończyć.")

        while True:
            message = input("> ")
            if message.lower() in ("exit", "quit"):
                print("Zakończono połączenie.")
                break

            # Wysyłanie danych (zawsze z końcem linii)
            client.sendall((message + "\n").encode())

            # Odbieranie odpowiedzi (blokujące)
            data = client.recv(1024)
            if not data:
                print("Serwer zakończył połączenie.")
                break

            print("Odpowiedź:", data.decode().strip())

if __name__ == "__main__":
    main()
