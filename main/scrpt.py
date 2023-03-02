import subprocess
import time

def enviar_comando_pronsole(comando):
    # Abre o Pronsole em um processo separado
    process = subprocess.Popen(['pronsole'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    # Aguarda alguns segundos para o Pronsole inicializar
    time.sleep(2)

    # Envia o comando para o Pronsole
    process.stdin.write(bytes(comando, 'utf-8') + b"\n")

    # Lê a resposta do Pronsole
    output = process.stdout.readline().decode()
    print(output)

    # Fecha o processo do Pronsole
    process.stdin.close()
    process.stdout.close()
    process.wait()