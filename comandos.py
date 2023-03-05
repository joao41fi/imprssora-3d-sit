import subprocess
import time

# Executar um comando simples na console
subprocess.run(["pronsole"])
time.sleep(2)

# Executar um comando mais complexo
subprocess.run(["connect/dev/ttyACM0", "250000"])