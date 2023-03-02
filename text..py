import subprocess
import time

# Abre o Pronsole em um processo separado
process = subprocess.Popen(['pronsole'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# Aguarda alguns segundos para o Pronsole inicializar
time.sleep(2)

# Envia um comando para o Pronsole
process.stdin.write(b"G28\n")

# Lê a resposta do Pronsole
output = process.stdout.readline().decode()
print(output)

# Fecha o processo do Pronsole
process.stdin.close()
process.stdout.close()
process.wait()