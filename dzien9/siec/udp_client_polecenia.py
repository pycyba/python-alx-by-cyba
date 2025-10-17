import socket

HOST = "127.0.0.1"
PORT = 6000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(2.0)  # maksymalnie 2 sekundy oczekiwania na odpowiedź
        print(f"Połączono z {HOST}:{PORT} (UDP)")
        print("Wpisz polecenie (echo, time, date, random) lub 'exit' aby zakończyć.")

        while True:
            message = input("> ")
            if message.lower() in ("exit", "quit"):
                print("Zakończono.")
                break

            # Wyślij wiadomość
            s.sendto(message.encode(), (HOST, PORT))

            # Spróbuj odebrać odpowiedź
            try:
                data, _ = s.recvfrom(1024)
                print("Odpowiedź:", data.decode())
            except socket.timeout:
                print("Brak odpowiedzi od serwera (timeout).")

if __name__ == "__main__":
    main()
