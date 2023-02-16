from threading import Thread
import socket

SOCK_BUFFER = 1024
num_clientes = 0


def client_handler(conn, client_address):
    global num_clientes
    num_clientes += 1
    print(f"Numero de clientes conectados: {num_clientes}")
    try:
        print(f"Conexión desde {client_address}")

        while True:
            data = conn.recv(SOCK_BUFFER)
            print(f"Recibido: {data}")
            if data:
                print(f"Enviando: {data}")
                conn.sendall(data)
            else:
                print("No hay más datos")
                break
    except Exception as e:
        print(f"Excepcion: {e}")
    finally:
        print("Cerrando conexión con el cliente")
        num_clientes -= 1
        conn.close()


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("0.0.0.0", 5000)
    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")
    sock.bind(server_address)

    sock.listen(1)

    while True:
        print("Esperando conexión...")

        conn, client_address = sock.accept()

        client_thread = Thread(target=client_handler, args=(conn, client_address))
        client_thread.start()
