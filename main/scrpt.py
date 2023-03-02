import subprocess
import time

def ligar_impressora(porta='/dev/ttyACM0', velocidade=250000):
    # Abre o Pronsole em um processo separado
    process = subprocess.Popen(['pronsole'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    # Aguarda alguns segundos para o Pronsole inicializar
    time.sleep(2)

    # Envia o comando de conexão para o Pronsole
    connect_cmd = f"connect {porta} {velocidade}\n"
    process.stdin.write(connect_cmd.encode())

    # Lê a resposta do Pronsole
    output = process.stdout.readline().decode()
    print(output)

    # Envia o comando G28 X e aguarda a resposta
    process.stdin.write(b"G28 X\n")
    output = process.stdout.readline().decode()
    print(output)

    # Envia o comando G28 Y e aguarda a resposta
    process.stdin.write(b"G28 Y\n")
    output = process.stdout.readline().decode()
    print(output)

    # Fecha o processo do Pronsole
    process.stdin.close()
    process.stdout.close()
    process.wait()