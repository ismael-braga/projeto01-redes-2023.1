# Importação da biblioteca socket
import socket

# IP do servidor
HOST = '127.0.0.1'
# Porta utilizada pelo servidor
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print('=' * 100)
print('Bem-vindo ao pedra, papel e tesoura!'.center(100).upper())
print('=' * 100)
# Exibe a mensagem que está contida na função lado_cliente no código do servidor, é o primeiro print da função
mensagem_jogador = s.recv(1024).decode()
print(mensagem_jogador)
# Lista com valores inteiros que representam as jogadas válidas, pedra é 1, papel é 2 e tesoura é 3
jogadas_validas = [1, 2, 3]
print('1 - Pedra\n2 - Papel\n3 - Tesoura')
print('=' * 100)
jogada = int(input('JOGADA: '))
print('=' * 100)
# Um while que não será encerrado enquanto a jogada não estiver no intervalo INTEIRO de jogadas válidas
while jogada not in jogadas_validas:
    print('Opção inválida, selecione um número entre 1 a 3 para escolher uma jogada correspondente.')
    print('=' * 100)
    print('Faça a sua jogada: \n1 - Pedra\n2 - Papel\n3 - Tesoura')
    print('=' * 100)
    jogada = int(input('JOGADA: '))
    print('=' * 100)
# Depois disso, será atribuido a variável jogada o seu valor real em texto ao invés de valor inteiro
if jogada == 1:
    jogada = 'pedra'
elif jogada == 2:
    jogada = 'papel'
elif jogada == 3:
    jogada = 'tesoura'
# Envia para o servidor a jogada que cada jogador escolheu. Isso é inserido no dicionário jogadas na função lado_cliente
print(f'Você escolheu {jogada.upper()}')
print('=' * 100)
s.send(jogada.encode())
print(s.recv(1024).decode())
