# Importação da biblioteca socket
import socket

# Função para verificar o vencedor com base nas jogadas dos jogadores
def verifica_vencedor(jogadaJogadorUm, jogadaJogadorDois):
    if jogadaJogadorUm == jogadaJogadorDois:
        return 0 # Empate
    elif (jogadaJogadorUm == "pedra" and jogadaJogadorDois == "tesoura") or (jogadaJogadorUm == "tesoura" and jogadaJogadorDois == "papel") or (jogadaJogadorUm == "papel" and jogadaJogadorDois == "pedra"):
        return 1 # Jogador 1 Vence
    return 2 # Jogador 2 Vence

# Função para interação com o cliente, recebendo a jogada do jogador
def lado_cliente(jogador, jogadorID, jogadas):
    # Após a conexão estabelecida pelo Jogador 2, será exibido para o Jogador 1 e depois para o Jogador 2 (após a jogada do Jogador 1)
    jogador.send(f'Jogador {jogadorID}, escolha a sua jogada!'.encode())
    print('=' * 100)
    # Recebe a jogada de cada Jogador
    jogada = jogador.recv(1024).decode()
    # Associa a jogada de cada jogador no dicionário de jogadas de acordo com o ID do jogador
    jogadas[jogadorID] = jogada
    print(f'Jogador {jogadorID} escolheu: {jogada.upper()}')

# IP do servidor
HOST = '127.0.0.1'
# Porta utilizada pelo servidor
PORT = 50000
# Cria um objeto de socket chamado s que utiliza o protocolo IPv4 e o protocolo de transporte TCP
# socket.AF_INET especifica que o tipo de endereço do socket será IPv4. AF_INET refere-se à família de endereços, e neste caso, é IPv4
# socket.SOCK_STREAM especifica que o tipo do socket será um socket de fluxo TCP, indica que o socket fornecerá um fluxo de dados confiável e bidirecional
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Está associando o socket ao endereço IP local e a uma porta específica
s.bind((HOST, PORT))
# Está colocando o socket no modo de escuta. Limita que até duas conexões simultâneas se conectem ao servidor.
s.listen(2)
print('=' * 100)
print('Aguardando a conexão dos jogadores...'.center(100).upper())
print('=' * 100)

jogadas = {}
conexoes = []
# Laço for para lidar com o aceite das duas conexões dos clientes
for _ in range(2):
    # s.accept() é um objeto de socket que fica bloqueado até que uma conexão seja estabelecida. Quando uma conexão é aceita, ele retorna um novo objeto de socket que representa a conexão com o cliente e o endereço do cliente
    # conexao é um novo objeto de socket que representa a conexão específica com o cliente. Ele é usado para enviar e receber dados da conexão
    # endereco é uma tupla que contém o endereço do cliente. Para conexões TCP/IP (nosso caso), esse endereco é uma tupla no formato (endereco IP, número da porta)
    conexao, endereco = s.accept()
    # Adiciona cada conexao em uma lista de conexoes
    conexoes.append(conexao)
    ip = endereco[0] 
    porta = endereco[1]
    print(f'Jogador {_+1} se conectou pelo IP {ip} na porta {porta}')

# Laço for para lidar com as conexões dos clientes
# Cada conexao na lista de conexoes representa um jogador
# O segundo parâmetro é o ID do jogador
# O terceiro parâmetro é um dicionário vazio que em seguida irá receber a jogada de cada jogador
for _ in range(2):
    lado_cliente(conexoes[_], _+1, jogadas)

jogadorUm = conexoes[0]
jogadorDois = conexoes[1]
jogadaJogadorUm = jogadas[1]
jogadaJogadorDois = jogadas[2]
print('=' * 100)
resultado = verifica_vencedor(jogadaJogadorUm, jogadaJogadorDois)
# Lógica que irá lidar com o resultado exibido para ambos os jogadores
if resultado == 0:
    print(f'RESULTADO: Empate')
    jogadorUm.send(f'O adversário escolheu {jogadaJogadorDois.upper()}\n{"=" * 100}\nVOCÊ EMPATOU COM O ADVERSÁRIO!'.encode())
    jogadorDois.send(f'O adversário escolheu {jogadaJogadorUm.upper()}\n{"=" * 100}\nVOCÊ EMPATOU COM O ADVERSÁRIO!'.encode())
elif resultado == 1:
    print(f'RESULTADO: Jogador 1 Venceu')
    jogadorUm.send(f'O adversário escolheu {jogadaJogadorDois.upper()}\n{"=" * 100}\nPARABÉNS, VOCÊ VENCEU =)'.encode())
    jogadorDois.send(f'O adversário escolheu {jogadaJogadorUm.upper()}\n{"=" * 100}\nQUE PENA, VOCÊ PERDEU =('.encode())
else:
    print(f'RESULTADO: Jogador 2 Venceu')
    jogadorUm.send(f'O adversário escolheu {jogadaJogadorDois.upper()}\n{"=" * 100}\nQUE PENA, VOCÊ PERDEU =('.encode())
    jogadorDois.send(f'O adversário escolheu {jogadaJogadorUm.upper()}\n{"=" * 100}\nPARABÉNS, VOCÊ VENCEU =)'.encode())
