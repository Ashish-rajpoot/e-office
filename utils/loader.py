from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

def wait_for_loader(wait):
    """
    Wait until Angular loader disappears.
    
    :param wait: WebDriverWait object
    """
    try:
        wait.until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, ".progress-loader-wrapper")
            )
        )
    except TimeoutException:
        raise Exception("Loader did not disappear within timeout")
    
    
    



def wait_for_loader_to_disappear(self, timeout=30):
    try:
        print("loader to appeared...")
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, ".loading-img-bg")
            )
        )
        print("loader disappeared...")
    except Exception:
        pass  # loader may not appear