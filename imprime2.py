import pyautogui
import time

# Abre o PrusaSlicer
pyautogui.press('winleft')
pyautogui.write('prusa slicer')
pyautogui.press('enter')
time.sleep(5)  # aguarda a abertura do PrusaSlicer

# Importa o modelo 3D
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)
pyautogui.write('caminho/caminho/do/arquivo.gcode
                do/arquivo.stl')
pyautogui.press('enter')
time.sleep(5)  # aguarda a importação do modelo

# Configura as opções de impressão
pyautogui.click(100, 100)  # clica no botão de configurações
time.sleep(2)
pyautogui.click(200, 200)  # clica no botão de perfis de impressora
time.sleep(2)
pyautogui.click(300, 300)  # seleciona o perfil de impressora desejado
time.sleep(2)
pyautogui.click(400, 400)  # clica no botão de fatiamento
time.sleep(2)
pyautogui.click(500, 500)  # seleciona as opções de fatiamento desejadas
time.sleep(2)

# Gera o arquivo G-code
pyautogui.hotkey('ctrl', 'p')
time.sleep(2)
pyautogui.write('caminho/do/arquivo.gcode')
pyautogui.press('enter')
time.sleep(5)  # aguarda a geração do arquivo G-code

# Envia o arquivo G-code para a impressora 3D
pyautogui.hotkey('ctrl', 'shift', 'p')
time.sleep(2)
pyautogui.write('caminho/do/arquivo.gcode')
pyautogui.press('enter')
time.sleep(5)  # aguarda o envio do arquivo G-code para a impressora 3D
