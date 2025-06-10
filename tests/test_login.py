import time
import pytest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from selenium.common.exceptions import TimeoutException

@pytest.mark.parametrize("username,password,expected_alert", [
    ("usuarioInexistente@gmail.com", "teste9090", "User does not exist."),
    ("Teste123@gmail.com", "incorreta123", "Wrong password."),
    ("Teste123@gmail.com", "", "Please fill out Username and Password."),
    ("", "teste9090", "Please fill out Username and Password."),
    ("", "", "Please fill out Username and Password."),
    ("NaoCadastrado123", "errada456", "User does not exist."),
])
def test_login_alertas(driver, username, password, expected_alert):
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.login(username, password)
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert alert.text == expected_alert
        alert.accept()
    except TimeoutException:
        pytest.fail("Alerta esperado não foi exibido.")


def test_login_valido(driver):
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.login("Teste123@gmail.com", "teste9090")
    usuario = login_page.obter_usuario_logado()
    assert "Teste123" in usuario
    time.sleep(2)