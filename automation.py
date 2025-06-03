from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Dados de login
USERNAME = "Teste123@gmail.com"
PASSWORD = "teste9090"
URL = "https://demoblaze.com/"

def iniciar_driver():
    print("Iniciando o driver...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)
    return driver

def esperar_elemento(driver, by, value, espera=20):
    return WebDriverWait(driver, espera).until(EC.visibility_of_element_located((by, value)))

def clicar_elemento(driver, by, value, espera=20):
    elemento = WebDriverWait(driver, espera).until(EC.element_to_be_clickable((by, value)))
    elemento.click()
    return elemento

def realizar_login(driver, username, password):
    print("Clicando no botão Login...")
    clicar_elemento(driver, By.ID, "login2")
    time.sleep(1)

    print("Preenchendo username e password...")
    esperar_elemento(driver, By.ID, "loginusername").send_keys(username)
    esperar_elemento(driver, By.ID, "loginpassword").send_keys(password)

    print("Clicando para confirmar login...")
    clicar_elemento(driver, By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')

def main():
    try:
        driver = iniciar_driver()
        time.sleep(2)  # esperar carregamento inicial
        realizar_login(driver, USERNAME, PASSWORD)
        print("Login realizado com sucesso! ✅")
    except Exception as e:
        print(f"Erro durante o processo de login: {e}")
    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    main()

# Dados de login
USERNAME = ""  # Campo de e-mail vazio
PASSWORD = "teste9090"
URL = "https://demoblaze.com/"
EXPECTED_ALERT = "Please fill out Username and Password."

def iniciar_driver():
    print("Iniciando o driver...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)
    return driver

def esperar_elemento(driver, by, value, espera=20):
    return WebDriverWait(driver, espera).until(EC.visibility_of_element_located((by, value)))

def clicar_elemento(driver, by, value, espera=20):
    elemento = WebDriverWait(driver, espera).until(EC.element_to_be_clickable((by, value)))
    elemento.click()
    return elemento

def realizar_login(driver, username, password):
    print("Clicando no botão Login...")
    clicar_elemento(driver, By.ID, "login2")
    time.sleep(1)

    print("Preenchendo username...")
    esperar_elemento(driver, By.ID, "loginusername").send_keys(username)

    print("Preenchendo password...")
    esperar_elemento(driver, By.ID, "loginpassword").send_keys(password)

    print("Clicando para confirmar login...")
    clicar_elemento(driver, By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')

def verificar_alerta(driver, esperado):
    print("Esperando alerta de erro...")
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alerta = driver.switch_to.alert
    texto_alerta = alerta.text
    print(f"⚠️ Alerta exibido: '{texto_alerta}'")

    if texto_alerta == esperado:
        print("✅ Alerta CORRETO! Login não realizado, como esperado!")
    else:
        print(f"❌ Alerta incorreto! Esperado: '{esperado}', mas apareceu: '{texto_alerta}'")

    time.sleep(5)
    alerta.accept()

def main():
    driver = None
    try:
        driver = iniciar_driver()
        time.sleep(2)
        realizar_login(driver, USERNAME, PASSWORD)
        verificar_alerta(driver, EXPECTED_ALERT)
    except Exception as e:
        print(f"🚨 Ocorreu um erro: {e}")
    finally:
        if driver:
            driver.quit()
            print("✅ Navegador fechado com sucesso!")
        else:
            print("⚠️ Driver não foi iniciado ou já foi fechado.")

if __name__ == "__main__":
    main()

#Cenário 3: Senha vazia no cadastro

# Dados para cadastro
USERNAME = "Teste123@gmail.com"
PASSWORD = ""  # Senha vazia
URL = "https://demoblaze.com/"
EXPECTED_ALERT = "Please fill out Username and Password."

def iniciar_driver():
    print("Iniciando o driver...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)
    return driver

def esperar_elemento(driver, by, value, espera=20):
    return WebDriverWait(driver, espera).until(EC.visibility_of_element_located((by, value)))

def clicar_elemento(driver, by, value, espera=20):
    elemento = WebDriverWait(driver, espera).until(EC.element_to_be_clickable((by, value)))
    elemento.click()
    return elemento

def realizar_cadastro(driver, username, password):
    print("Clicando no botão Sign up...")
    clicar_elemento(driver, By.ID, "signin2")
    time.sleep(1)

    print("Preenchendo username...")
    esperar_elemento(driver, By.ID, "sign-username").send_keys(username)

    print("Preenchendo password (pode estar vazio)...")
    esperar_elemento(driver, By.ID, "sign-password").send_keys(password)

    print("Clicando para confirmar cadastro...")
    clicar_elemento(driver, By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')

def verificar_alerta(driver, esperado):
    print("Esperando alerta de erro...")
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alerta = driver.switch_to.alert
    texto_alerta = alerta.text
    print(f"⚠️ Alerta exibido: '{texto_alerta}'")

    if texto_alerta == esperado:
        print("✅ Alerta CORRETO! Cadastro não realizado, como esperado!")
    else:
        print(f"❌ Alerta incorreto! Esperado: '{esperado}', mas apareceu: '{texto_alerta}'")

    time.sleep(5)
    alerta.accept()

def main():
    driver = None
    try:
        driver = iniciar_driver()
        time.sleep(2)
        realizar_cadastro(driver, USERNAME, PASSWORD)
        verificar_alerta(driver, EXPECTED_ALERT)
    except Exception as e:
        print(f"🚨 Ocorreu um erro: {e}")
    finally:
        if driver:
            driver.quit()
            print("✅ Navegador fechado com sucesso!")
        else:
            print("⚠️ Driver não foi iniciado ou já foi fechado.")

if __name__ == "__main__":
    main()

#Cenário 4: Login com dados válidos

# Dados de login válidos (pré-cadastrados)
USERNAME = "Teste123@gmail.com"
PASSWORD = "teste9090"
URL = "https://demoblaze.com/"

def iniciar_driver():
    print("Iniciando o driver...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)
    driver.maximize_window()
    return driver

def esperar_elemento(driver, by, value, espera=20):
    return WebDriverWait(driver, espera).until(EC.visibility_of_element_located((by, value)))

def clicar_elemento(driver, by, value, espera=20):
    elemento = WebDriverWait(driver, espera).until(EC.element_to_be_clickable((by, value)))
    elemento.click()
    return elemento

def realizar_login(driver, username, password):
    print("Clicando no botão Login...")
    clicar_elemento(driver, By.ID, "login2")
    time.sleep(1)

    print("Preenchendo username e password...")
    campo_user = esperar_elemento(driver, By.ID, "loginusername")
    campo_user.clear()
    campo_user.send_keys(username)

    campo_pass = esperar_elemento(driver, By.ID, "loginpassword")
    campo_pass.clear()
    campo_pass.send_keys(password)

    print("Confirmando login...")
    clicar_elemento(driver, By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')

def verificar_login_sucesso(driver):
    print("Esperando a confirmação do login...")
    usuario_logado = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "nameofuser"))
    )
    print(f"✅ Login realizado com sucesso! Bem-vindo, {usuario_logado.text}!")

    print("Pausando 5 segundos para visualizar que logou...")
    time.sleep(5)

def main():
    driver = None
    try:
        driver = iniciar_driver()
        time.sleep(2)
        realizar_login(driver, USERNAME, PASSWORD)
        verificar_login_sucesso(driver)
    except Exception as e:
        print(f"🚨 Ocorreu um erro: {e}")
    finally:
        if driver:
            driver.quit()
            print("✅ Navegador fechado com sucesso!")
        else:
            print("⚠️ Driver não foi iniciado ou já foi fechado.")

if __name__ == "__main__":
    main()

#Cenário 5: Email incorreto e senha correta

# Dados de login incorreto
USERNAME = "incorreto123@gmail.com"
PASSWORD = "teste9090"
URL = "https://demoblaze.com/"
EXPECTED_ALERT = "User does not exist."

def iniciar_driver():
    print("Iniciando o driver...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)
    driver.maximize_window()
    return driver

def esperar_elemento(driver, by, value, espera=20):
    return WebDriverWait(driver, espera).until(EC.visibility_of_element_located((by, value)))

def clicar_elemento(driver, by, value, espera=20):
    elemento = WebDriverWait(driver, espera).until(EC.element_to_be_clickable((by, value)))
    elemento.click()
    return elemento

def realizar_login(driver, username, password):
    print("Clicando no botão Login...")
    clicar_elemento(driver, By.ID, "login2")
    time.sleep(1)

    print("Preenchendo username e password...")
    campo_user = esperar_elemento(driver, By.ID, "loginusername")
    campo_user.clear()
    campo_user.send_keys(username)

    campo_pass = esperar_elemento(driver, By.ID, "loginpassword")
    campo_pass.clear()
    campo_pass.send_keys(password)

    print("Confirmando login...")
    clicar_elemento(driver, By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')

def verificar_alerta(driver, esperado):
    print("Esperando alerta de erro...")
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alerta = driver.switch_to.alert
    texto_alerta = alerta.text
    print(f"⚠️ Alerta exibido: '{texto_alerta}'")

    if texto_alerta == esperado:
        print("✅ Teste passou: Alerta correto exibido!")
    else:
        print(f"❌ Teste falhou: Esperado '{esperado}', mas apareceu '{texto_alerta}'")

    print("Pausando 5 segundos para visualização...")
    time.sleep(5)
    alerta.accept()

def main():
    driver = None
    try:
        driver = iniciar_driver()
        time.sleep(2)
        realizar_login(driver, USERNAME, PASSWORD)
        verificar_alerta(driver, EXPECTED_ALERT)
    except Exception as e:
        print(f"🚨 Ocorreu um erro: {e}")
    finally:
        if driver:
            driver.quit()
            print("✅ Navegador fechado com sucesso!")
        else:
            print("⚠️ Driver não foi iniciado ou já foi fechado.")

if __name__ == "__main__":
    main()

#Cenário 6: Senha incorreta

# Dados de login (usuário correto, senha incorreta)
USERNAME = "Teste123@gmail.com"
PASSWORD = "incorreta123"
URL = "https://demoblaze.com/"
EXPECTED_ALERT = "Wrong password."

def iniciar_driver():
    print("Iniciando o driver...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)
    driver.maximize_window()
    return driver

def esperar_elemento(driver, by, value, espera=20):
    return WebDriverWait(driver, espera).until(EC.visibility_of_element_located((by, value)))

def clicar_elemento(driver, by, value, espera=20):
    elemento = WebDriverWait(driver, espera).until(EC.element_to_be_clickable((by, value)))
    elemento.click()
    return elemento

def realizar_login(driver, username, password):
    print("Clicando no botão Login...")
    clicar_elemento(driver, By.ID, "login2")
    time.sleep(1)

    print("Preenchendo username e password...")
    campo_user = esperar_elemento(driver, By.ID, "loginusername")
    campo_user.clear()
    campo_user.send_keys(username)

    campo_pass = esperar_elemento(driver, By.ID, "loginpassword")
    campo_pass.clear()
    campo_pass.send_keys(password)

    print("Confirmando login...")
    clicar_elemento(driver, By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')

def verificar_alerta(driver, esperado):
    print("Esperando alerta de erro...")
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alerta = driver.switch_to.alert
    texto_alerta = alerta.text
    print(f"⚠️ Alerta exibido: '{texto_alerta}'")

    if texto_alerta == esperado:
        print("✅ Teste passou: Alerta correto exibido!")
    else:
        print(f"❌ Teste falhou: Esperado '{esperado}', mas apareceu '{texto_alerta}'")

    print("Pausando 5 segundos para visualização...")
    time.sleep(5)
    alerta.accept()

def main():
    driver = None
    try:
        driver = iniciar_driver()
        time.sleep(2)
        realizar_login(driver, USERNAME, PASSWORD)
        verificar_alerta(driver, EXPECTED_ALERT)
    except Exception as e:
        print(f"🚨 Ocorreu um erro: {e}")
    finally:
        if driver:
            driver.quit()
            print("✅ Navegador fechado com sucesso!")
        else:
            print("⚠️ Driver não foi iniciado ou já foi fechado.")

if __name__ == "__main__":
    main()

# Cenário 7: Login com email preenchido e senha vazia

username = "Teste123@gmail.com"  
password = ""  # SENHA VAZIA

try:
    print("\nIniciando o driver...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print("Abrindo o site Demoblaze...")
    driver.get("https://demoblaze.com/")
    driver.maximize_window()
    time.sleep(3)

    print("Clicando no botão Login...")
    btn_login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login2"))
    )
    btn_login.click()
    time.sleep(2)

    print("Preenchendo nome de usuário...")
    input_username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    )
    input_username.clear()
    input_username.send_keys(username)

    print("Deixando senha vazia...")
    input_password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginpassword"))
    )
    input_password.clear()
    input_password.send_keys(password)

    time.sleep(1)

    print("Clicando para confirmar login...")
    btn_confirm_login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]'))
    )
    btn_confirm_login.click()

    print("Esperando mensagem de erro...")
    WebDriverWait(driver, 10).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"⚠️ Mensagem exibida: '{alert_text}'")

    expected_alert = "Please fill out Username and Password."  

    if alert_text == expected_alert:
        print("✅ Teste passou: Alerta correto exibido!")
    else:
        print(f"❌ Teste falhou: Esperado '{expected_alert}', mas apareceu '{alert_text}'")

    time.sleep(5)  
    alert.accept()

except Exception as e:
    print(f"🚨 Ocorreu um erro: {e}")

finally:
    try:
        driver.quit()
        print("✅ Navegador fechado com sucesso!")
    except:
        print("⚠️ Driver não foi iniciado ou já foi fechado.")


#Cenário 8: Login com nome de Email vazio e senha preenchida

username = ""  
password = "teste9090"  # senha válida

try:
    print("\nIniciando o driver...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print("Abrindo o site Demoblaze...")
    driver.get("https://demoblaze.com/")
    driver.maximize_window()
    time.sleep(3)

    print("Clicando no botão Login...")
    btn_login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login2"))
    )
    btn_login.click()
    time.sleep(2)

    print("Deixando nome de usuário vazio...")
    input_username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    )
    input_username.clear()
    input_username.send_keys(username)

    print("Preenchendo senha...")
    input_password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginpassword"))
    )
    input_password.clear()
    input_password.send_keys(password)

    time.sleep(1)

    print("Clicando para confirmar login...")
    btn_confirm_login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]'))
    )
    btn_confirm_login.click()

    print("Esperando mensagem de erro...")
    WebDriverWait(driver, 10).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"⚠️ Mensagem exibida: '{alert_text}'")

    expected_alert = "Please fill out Username and Password."  

    if alert_text == expected_alert:
        print("✅ Teste passou: Alerta correto exibido!")
    else:
        print(f"❌ Teste falhou: Esperado '{expected_alert}', mas apareceu '{alert_text}'")

    time.sleep(5)
    alert.accept()

except Exception as e:
    print(f"🚨 Ocorreu um erro: {e}")

finally:
    try:
        driver.quit()
        print("✅ Navegador fechado com sucesso!")
    except:
        print("⚠️ Driver não foi iniciado ou já foi fechado.")


# ✅ Cenário 9: Login com nome de usuário e senha não cadastrados

username = "NaoCadastrado123"
password = "errada456"

try:
    print("\nIniciando o driver...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print("Abrindo o site Demoblaze...")
    driver.get("https://demoblaze.com/")
    driver.maximize_window()
    time.sleep(3)

    print("Clicando no botão Login...")
    btn_login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login2"))
    )
    btn_login.click()
    time.sleep(2)

    print("Preenchendo nome de usuário...")
    input_username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    )
    input_username.clear()
    input_username.send_keys(username)

    print("Preenchendo senha...")
    input_password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginpassword"))
    )
    input_password.clear()
    input_password.send_keys(password)

    time.sleep(1)

    print("Clicando para confirmar login...")
    btn_confirm_login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]'))
    )
    btn_confirm_login.click()

    print("Esperando mensagem de erro...")
    WebDriverWait(driver, 10).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"⚠️ Mensagem exibida: '{alert_text}'")

    expected_alert = "User does not exist."

    if expected_alert in alert_text:
        print("✅Teste passou: Alerta correto exibido!")
    else:
        print(f"❌Teste falhou: Esperado algo parecido com '{expected_alert}', mas apareceu '{alert_text}'")

    alert.accept()

except Exception as e:
    print(f"🚨Ocorreu um erro: {e}")

finally:
    try:
        driver.quit()
        print("✅Navegador fechado com sucesso!")
    except:
        print("⚠️Driver não foi iniciado ou já foi fechado.")


# ✅ Cenário 10: Login com ambos os campos vazios

username = ""
password = ""

try:
    print("\nIniciando o driver...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print("Abrindo o site Demoblaze...")
    driver.get("https://demoblaze.com/")
    driver.maximize_window()
    time.sleep(3)

    print("Clicando no botão Login...")
    btn_login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login2"))
    )
    btn_login.click()
    time.sleep(2)

    print("Deixando usuário vazio...")
    input_username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    )
    input_username.clear()
    input_username.send_keys(username)

    print("Deixando senha vazia...")
    input_password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginpassword"))
    )
    input_password.clear()
    input_password.send_keys(password)

    time.sleep(1)

    print("Tentando logar com campos vazios...")
    btn_confirm_login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]'))
    )
    btn_confirm_login.click()

    print("Esperando alerta aparecer...")
    WebDriverWait(driver, 10).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Mensagem exibida: '{alert_text}'")

    expected_alert = "Please fill out Username and Password."

    if alert_text == expected_alert:
        print("✅Teste passou: Alerta correto exibido!")
    else:
        print(f"❌Teste falhou: Esperado '{expected_alert}', mas apareceu '{alert_text}'")

    alert.accept()

except Exception as e:
    print(f"🚨Ocorreu um erro: {e}")
    time.sleep(5) 

finally:
    try:
        driver.quit()
        print("✅Navegador fechado com sucesso!")
    except:
        print("⚠️Driver não foi iniciado ou já foi fechado.")


