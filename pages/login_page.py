from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    EMAIL = (By.CSS_SELECTOR, "form[data-cy='signin-form'] input[name='loginId']")
    PASSWORD = (By.CSS_SELECTOR, "form[data-cy='signin-form'] input[name='password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "form[data-cy='signin-form'] button[type='submit']")
    ERROR_TEXT = (By.CSS_SELECTOR, "form[data-cy='signin-form'] p.MuiFormHelperText-root")

    def __init__(self, driver, wait_time=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    def fill_email(self, email):
        el = self.wait.until(EC.visibility_of_element_located(self.EMAIL))
        el.clear()
        el.send_keys(email)

    def fill_password(self, password):
        el = self.wait.until(EC.visibility_of_element_located(self.PASSWORD))
        el.clear()
        el.send_keys(password)

    def submit(self):
        btn = self.wait.until(EC.presence_of_element_located(self.LOGIN_BTN))
        self.wait.until(lambda d: btn.is_enabled())
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        self.driver.execute_script("arguments[0].click();", btn)
