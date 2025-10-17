"""
Przykład asynchronicznego serwera TCP w Pythonie, który wykorzystuje moduł asyncio (również wbudowany w standardową bibliotekę).
Taki serwer jest idealny do obsługi wielu jednoczesnych połączeń bez użycia wątków — działa wydajnie i skalowalnie.

- asyncio.start_server() tworzy serwer TCP i uruchamia handle_client() dla każdego klienta.
- reader i writer to asynchroniczne strumienie służące do odbierania i wysyłania danych.
- await pozwala innym klientom działać, gdy np. jeden czeka na dane.

(Chat GPT)
"""

import asyncio

HOST = '127.0.0.1'
PORT = 5000


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info('peername')
    print(f"[NOWE POŁĄCZENIE] {addr}")

    while True:
        data = await reader.read(1024)
        if not data:
            break  # klient się rozłączył
        message = data.decode().strip()
        print(f"[{addr}] {message}")

        # Odesłanie odpowiedzi (echo)
        writer.write(data)
        await writer.drain()

    print(f"[ROZŁĄCZONO] {addr}")
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    addr = server.sockets[0].getsockname()
    print(f"[START] Serwer TCP (asyncio) działa na {addr}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
