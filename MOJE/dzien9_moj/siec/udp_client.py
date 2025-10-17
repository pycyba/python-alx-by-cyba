# Klient (nadawca) UDP
# ChatGPT
import socket

HOST = "127.0.0.1"  # adres serwera UDP
PORT = 6000         # port serwera

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        print(f"Połączono z {HOST}:{PORT} (UDP)")
        print("Wpisz wiadomość i naciśnij Enter. 'exit' kończy działanie.")

        while True:
            message = input("> ")
            if message.lower() in ("exit", "quit"):
                print("Zakończono wysyłanie.")
                break

            s.sendto(message.encode(), (HOST, PORT))

if __name__ == "__main__":
    main()
