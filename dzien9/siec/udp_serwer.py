# Serwer (odbiornik) UDP
# ChatGPT
import socket

HOST = "127.0.0.1"  # lokalny adres
PORT = 6000         # port nasłuchiwania

def main():
    # Tworzymy socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"[START] Serwer UDP nasłuchuje na {HOST}:{PORT}")

        while True:
            data, addr = s.recvfrom(1024)  # odbiór do 1024 bajtów
            message = data.decode()
            print(f"Otrzymano od {addr}: {message}")

if __name__ == "__main__":
    main()
