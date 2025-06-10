from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_button = (By.ID, "login2")
        self.username_input = (By.ID, "loginusername")
        self.password_input = (By.ID, "loginpassword")
        self.confirm_login_button = (By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        self.logged_user = (By.ID, "nameofuser")

    def abrir(self):
        self.driver.get("https://demoblaze.com/")
        self.driver.maximize_window()

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.login_button)).click()
        wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(username)
        wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)
        wait.until(EC.element_to_be_clickable(self.confirm_login_button)).click()

    def obter_usuario_logado(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.logged_user)).text
