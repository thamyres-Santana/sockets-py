# ANA THAMYRES
# CLIENTE (inicia a conexão)
import socket
import random

HOST = 'localhost'
PORT = 5000

# Cria o socket do produtor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
sock.connect((HOST, PORT))

# Gera os números aleatórios
num = 1
for i in range(1000):
    delta = random.randint(1, 100)
    num += delta
    # Envia o número ao consumidor
    sock.send(str(num).encode())
    # Aguarda a resposta do consumidor
    data = sock.recv(1024)
    # Imprime se o número é primo ou não
    if data == b'1' :
        
        print(f'{num} é primo')
    else:
        print(f'{num} não é primo')
    # Verifica se o número é ímpar ou par
    if num % 2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é ímpar')

# Envia o número zero e fecha a conexão
sock.send(b'0')
sock.close()
