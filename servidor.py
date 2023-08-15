import socket
import code
import threading

clientes = []
chave = '#GwkhyRian010107547'

def handle_client(client_socket):
    while True:
        try:
            msg_cifrada = client_socket.recv(1024).decode('utf-8')
            if not msg_cifrada:
                break
            msg = code.decifrar_xor(msg_cifrada, chave)

            if msg == 'tt':
                break
            else:
                print('Mensagem recebida:', msg)
                broadcast(msg_cifrada, client_socket)

        except:
            break

    client_socket.close()

def broadcast(msg_cifrada, client_socket):
    for cliente in clientes:
        if cliente != client_socket:
            try:
                cliente.send(msg_cifrada.encode('utf-8'))
            except:
                clientes.remove(cliente)

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 8888))
servidor.listen()

print('Aguardando conexão...')

while True:
    cliente, _ = servidor.accept()
    clientes.append(cliente)
    client_thread = threading.Thread(target=handle_client, args=(cliente,))
    client_thread.start()