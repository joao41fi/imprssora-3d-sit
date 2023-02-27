import socket

def comand (comandos):
# Defina o endereço IP e a porta do servidor
 endereco_servidor = '192.168.1.108' # substitua pelo endereço IP do servidor
 porta = 9999

# Crie um socket TCP/IP
 cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecte-se ao servidor
 cliente_socket.connect((endereco_servidor, porta))

# Envie um comando para o servidor
 comando = comandos # substitua pelo comando desejado
 cliente_socket.send(comando.encode())

# Receba o resultado do comando enviado pelo servidor
 resultado = cliente_socket.recv(1024)

# Imprima o resultado na tela
#print(resultado.decode())

# Feche a conexão com o servfidor
 cliente_socket.close()
 return resultado