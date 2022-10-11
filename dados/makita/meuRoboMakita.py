from ast import parse
import time
import pyautogui
from pydoc import classname
from operator import index
from selenium import webdriver
from dados.makita.listaProdutosMakita import listaProdutosMakita

# listaProdutoBloco1 = ok #
# listaProdutoBloco2 = ok #
# listaProdutoBloco3 = ok #
# listaProdutoBloco4 = ok #
# listaProdutoBloco5 = ok #
# listaProdutoBloco6 = ok #
# listaProdutoBloco7 = ok #
# listaProdutoBloco8 = ok #
# listaProdutoBloco9 = ok #
# listaProdutoBloco10 = ok #

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

# faz rota sistemica #
navegador.find_element('xpath', '/html/body/center/div[2]/div/ul/li[4]/a').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="menu_inicial"]/div/div/ul/li[7]/a').click()
time.sleep(3)

# avanca para pagina 2 #      
navegador.find_element('xpath', f'/html/body/div[4]/form[2]/div[1]/font[2]/a').click()
time.sleep(5)

# avanca para pagina 3 #      
navegador.find_element('xpath', f'/html/body/div[4]/form[2]/div[1]/font[2]/a').click()
time.sleep(5)

# avanca para pagina 4 #      
navegador.find_element('xpath', f'/html/body/div[4]/form[2]/div[1]/font[2]/a').click()
time.sleep(5)

# avanca para pagina 5 #      
navegador.find_element('xpath', f'/html/body/div[4]/form[2]/div[1]/font[2]/a').click()
time.sleep(5)

# avanca para pagina 6 #      
navegador.find_element('xpath', f'/html/body/div[4]/form[2]/div[1]/font[2]/a').click()
time.sleep(5)

# avanca para pagina 7 #      
navegador.find_element('xpath', f'/html/body/div[4]/form[2]/div[1]/font[2]/a').click()
time.sleep(5)

# avanca para pagina 8 #      
navegador.find_element('xpath', f'/html/body/div[4]/form[2]/div[1]/font[2]/a').click()
time.sleep(5)

# avanca para pagina 9 #      
navegador.find_element('xpath', f'/html/body/div[4]/form[2]/div[1]/font[2]/a').click()
time.sleep(5)

# avanca para pagina 10 #      
navegador.find_element('xpath', f'/html/body/div[4]/form[2]/div[1]/font[2]/a').click()
time.sleep(5)

# salva PDF bloco 1
itemPDF = 1
while itemPDF <= 100:
    for item in listaProdutosMakita.listaProdutoBloco10:
        pyautogui.hotkey('ctrl', 'r')
        time.sleep(5)
        navegador.find_element('xpath', f'//*[@id="table_frmcomunicado"]/tbody/tr[{itemPDF}]/td[4]/a').click()
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