import time
import pyautogui
import clipboard
import pyscreenshot
from pydoc import classname
from operator import index
from selenium import webdriver
from dados.dewalt.listaProdutosDewalt import listaProdutosDewalt

# instancia o google chrome #
navegador = webdriver.Chrome()
link = 'https://posvenda.telecontrol.com.br/assist/externos/login_posvenda_new.php'
navegador.get(url=link)

# realiza o login #
email = 'carlos@rocfer.com.br'
senha = 'bife4112@'   
campo_email = navegador.find_element('xpath', '//*[@id="login"]')
campo_email.send_keys(email)
campo_senha = navegador.find_element('xpath', '//*[@id="senha"]')
campo_senha.send_keys(senha)
navegador.find_element('xpath', '//*[@id="btnAcao"]').click()

# faz rota sistemica dewalt #
navegador.find_element('xpath', '/html/body/center/div[2]/div/ul/li[1]/a').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="menu_inicial"]/div/div/ul/li[8]/a').click()
time.sleep(1)

# salva PDF #
for item in listaProdutosDewalt.listaProdutosBloco1_200:
    existeVistaExplodida = ''
    # fazer rota sistemica para vista #
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(4)
    navegador.find_element('xpath', '/html/body/center/table[1]/tbody/tr[5]/td[1]/a').click()
    time.sleep(3)
    pyautogui.moveTo(778, 394, 1)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.write(item)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.doubleClick(920, 646)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    existeVistaExplodida = clipboard.paste()
    time.sleep(1)
    if (existeVistaExplodida == 'Vista ' or existeVistaExplodida == 'Informativo '):
        # salva PDF do telecontrol #
        pyautogui.keyDown("pagedown")
        time.sleep(3)
        pyautogui.keyDown("shift")
        time.sleep(1)
        navegador.find_element('xpath', '/html/body/center/table/tbody/tr[2]/td[1]').click()
        time.sleep(1)
        navegador.find_element('xpath', '/html/body/center/table/tbody/tr[6]/td[6]').click()
        time.sleep(1)
        pyautogui.keyUp("pagedown")
        time.sleep(3)
        pyautogui.keyUp("shift")
        time.sleep(1)   
        pyautogui.hotkey('ctrl', 'c')
    else:
        image = pyscreenshot.grab()  
        image.save(f'{item}.png')
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(1)
        pyautogui.hotkey('ctrl', '1')
        time.sleep(1)
        
# ao finalizar o salvar PDF ele fecha o chrome
navegador.quit()