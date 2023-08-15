import socket
import code
import threading

def receive_message(client_socket):
    while True:
        try:
            msg_cifrada = client_socket.recv(1024).decode('utf-8')
            msg = code.decifrar_xor(msg_cifrada, chave)

            if msg == 'tt':
                break
            else:
                print('Mensagem recebida:', msg)

        except:
            break

    client_socket.close()

chave = '#GwkhyRian010107547'

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 8888))

receive_thread = threading.Thread(target=receive_message, args=(cliente,))
receive_thread.start()

terminado = False
print('Digite "tt" para terminar o chat')

while not terminado:
    c = input('Mensagem: ')

    if c == 'tt':
        terminado = True
    else:
        cifrado = code.cifrar_xor(c, chave)
        cliente.send(cifrado.encode('utf-8'))

cliente.close()