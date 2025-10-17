import socket
import datetime
import random

HOST = "127.0.0.1"
PORT = 6000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"[START] Serwer UDP działa na {HOST}:{PORT}")

        while True:
            data, addr = s.recvfrom(1024)
            message = data.decode().strip()
            print(f"[{addr}] -> {message}")

            # Prosty parser poleceń (jak w wersji TCP)
            parts = message.split(maxsplit=1)
            cmd = parts[0].lower()
            arg = parts[1] if len(parts) > 1 else ""

            if cmd == "echo":
                response = arg
            elif cmd == "time":
                response = datetime.datetime.now().strftime("%H:%M:%S")
            elif cmd == "date":
                response = datetime.date.today().strftime("%Y-%m-%d")
            elif cmd == "random":
                response = str(random.randint(1, 1000))
            else:
                response = f"Nieznane polecenie: {cmd}"

            s.sendto(response.encode(), addr)
            print(f"[ODPOWIEDŹ -> {addr}] {response}")

if __name__ == "__main__":
    main()
