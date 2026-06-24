from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 300)

    def handle_ssl_warning(self):

        try:
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "details-button")
                )
            ).click()

            self.wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "proceed-link")
                )
            ).click()

        except TimeoutException:
            pass


    ERROR_MESSAGE = (
        By.XPATH,
        "//div[@role='alert']//p[contains(text(),'Something went wrong')]"
    )


    def check_and_refresh_on_error(self):

        try:

            error = self.driver.find_element(
                *self.ERROR_MESSAGE
            )

            if error.is_displayed():

                print(
                    "Error detected: Refreshing page..."
                )

                self.driver.refresh()

                time.sleep(5)

                return True


        except Exception:
            pass


        return False
    

    def wait_until_page_ready(self):

        for i in range(5):

            if self.check_and_refresh_on_error():

                print(
                    f"Retry attempt {i+1}"
                )

            else:
                break