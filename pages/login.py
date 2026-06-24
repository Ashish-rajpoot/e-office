from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.login_page import LoginPage, FileCreatePage


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open_login_page(self):
        self.driver.get(FileCreatePage.ROOT_URL)

        create_btn = self.wait.until(
            EC.element_to_be_clickable(
                FileCreatePage.CREATE_FILE_BUTTON
            )
        )

        create_btn.click()

    def enter_user_id(self, user_id):
        username_box = self.wait.until(
            EC.presence_of_element_located(
                LoginPage.USERNAME_INPUT
            )
        )

        username_box.clear()
        username_box.send_keys(user_id)

    def accept_terms(self):
        checkbox = self.wait.until(
            EC.element_to_be_clickable(
                LoginPage.TNC_CHECKBOX
            )
        )

        if not checkbox.is_selected():
            checkbox.click()

    def click_next(self):
        self.wait.until(
            lambda d: d.find_element(
                *LoginPage.NEXT_BUTTON
            ).is_enabled()
        )

        next_btn = self.driver.find_element(
            *LoginPage.NEXT_BUTTON
        )

        next_btn.click()

    def select_tap_authentication(self):
        tap_auth = self.wait.until(
            EC.element_to_be_clickable(
                LoginPage.TAP_AUTH_OPTION
            )
        )

        tap_auth.click()

    def select_raj_up_gov_email(self):
        try:
            radio_btn = self.wait.until(
                EC.element_to_be_clickable(
                    LoginPage.RAJ_UP_GOV_EMAIL_RADIO
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                radio_btn
            )

        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/select_raj_up_gov_email_error.png"
            )
            raise Exception(
                f"Selecting raj*7103@up.gov.in radio button failed: {e}"
            )
        
    def click_no_button(self):
        try:
            btn = self.wait.until(
                EC.element_to_be_clickable(
                    LoginPage.NO_BUTTON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                btn
            )

            # Wait until popup/button disappears
            self.wait.until(
                EC.invisibility_of_element(
                    btn
                )
            )

        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/no_button_error.png"
            )
            raise Exception(
                f"Clicking No button failed: {e}"
            )
    def login(self, user_id):
        self.open_login_page()

        self.enter_user_id(user_id)
        sleep(2)  # Optional: Add a short delay to ensure the user ID is processed
        self.accept_terms()
        sleep(2)  # Optional: Add a short delay to ensure the user ID is processed
        self.click_next()
        sleep(2)  # Optional: Add a short delay to ensure the user ID is processed

        if user_id == "7705017103":
            self.select_raj_up_gov_email()
            self.click_next()
            self.click_no_button()

        self.select_tap_authentication()
        sleep(2)  # Optional: Add a short delay to ensure the user ID is processed

        self.click_next()