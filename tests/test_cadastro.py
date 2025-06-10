import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.cadastro_page import CadastroPage

def test_cadastro_senha_vazia(driver):
    cadastro_page = CadastroPage(driver)
    cadastro_page.abrir()
    cadastro_page.cadastrar("Teste123@gmail.com", "")   
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert alert.text == "Por favor, preencha o Nome de Usuário e a Senha."
        alert.accept()
    except TimeoutException:
        assert False, "Alerta não exibido como esperado."
    time.sleep(2)
