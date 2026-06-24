import os
from datetime import datetime


def take_screenshot(driver, name="error"):
    """
    Save screenshot with timestamp.

    :param driver: Selenium webdriver instance
    :param name: Screenshot name prefix
    :return: screenshot file path
    """

    folder = "screenshots"

    # Create folder if not exists
    os.makedirs(folder, exist_ok=True)

    filename = os.path.join(
        folder,
        f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    )

    driver.save_screenshot(filename)

    return filename