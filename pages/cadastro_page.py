from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CadastroPage:
    def __init__(self, driver):
        self.driver = driver
        self.signup_button = (By.ID, "signin2")
        self.username_input = (By.ID, "sign-username")
        self.password_input = (By.ID, "sign-password")
        self.confirm_button = (By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')

    def abrir(self):
        self.driver.get("https://demoblaze.com/")
        self.driver.maximize_window()

    def cadastrar(self, username, password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.signup_button)).click()
        wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(username)
        wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)
        wait.until(EC.element_to_be_clickable(self.confirm_button)).click()