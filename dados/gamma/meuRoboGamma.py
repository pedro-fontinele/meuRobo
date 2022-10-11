from ast import parse
import time
import pyautogui
from pydoc import classname
from operator import index
from selenium import webdriver
from dados.gamma.listaProdutosGamma import listaProdutosGamma

# listaProdutosBloco1 = ok #
# listaProdutosBloco2 = ok #
# listaProdutosBloco3 = ok #
# listaProdutosBloco4 = ok #

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

# faz rota sistemica gamma #
navegador.find_element('xpath', '/html/body/center/div[2]/div/ul/li[3]/a').click()
time.sleep(1)
pyautogui.moveTo(798, 140, 1)
time.sleep(1)
pyautogui.moveTo(773, 409, 1)
time.sleep(1)
pyautogui.click()
time.sleep(10)

# avanca para pagina 2 #      
navegador.find_element('xpath', '/html/body/div[4]/form[2]/div[1]/font[2]/a').click()
time.sleep(5)

# avanca para pagina 3 #      
navegador.find_element('xpath', '/html/body/div[4]/form[2]/div[1]/font[2]/a').click()
time.sleep(5)

# avanca para pagina 4 #      
navegador.find_element('xpath', '/html/body/div[4]/form[2]/div[1]/font[2]/a').click()
time.sleep(5)

# salva PDF bloco 1
itemPDF = 1
linhaItem = 1
while itemPDF <= 100:
    for item in listaProdutosGamma.listaProdutosBloco4:
        pyautogui.hotkey('ctrl', 'r')
        time.sleep(5)
        navegador.find_element('xpath', f'//*[@id="table_frmcomunicado"]/tbody/tr[{linhaItem}]/td[3]/a').click()
        linhaItem = linhaItem+3
        itemPDF = itemPDF+1
        time.sleep(15)
        pyautogui.moveTo(636, 424, 1)
        pyautogui.click()
        time.sleep(5)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(2)
        pyautogui.write(f'{item}') 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('ctrl', '1')

# ao finalizar o salvar PDF ele fecha o chrome
navegador.quit()