from pages.create_file_page import CreateFile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException
)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from excel_reader import get_user_id
from pages.login import Login
from locators.create_file_page_loc import CreateFilePageLocators
from pages.base_page import BasePage
from pages.steps_page import Steps
from utils.screenshot import take_screenshot
from utils.clear_screenshots import clear_screenshots
from utils.excel_writer import write_login_status
from utils.excel_reader import get_all_users
from time import sleep

clear_screenshots()

PROFILE_PATH = os.path.abspath("chrome_profile")

options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")
options.set_capability(
    "acceptInsecureCerts",
    True
)


USER_DATA_FILE = "data/userdata.xlsm"
SPECIAL_USER_ID = "9412430321"

# Step 1: Process all users except special user until all become Y
while True:

    users = get_all_users(USER_DATA_FILE)

    pending_users = [
        u for u in users
        if str(u["user_id"]).strip() != SPECIAL_USER_ID
        and u["flag"].strip().upper() == "N"
    ]

    if not pending_users:
        print("All normal users are Y.")
        break

    for user in pending_users:

        print(f"Processing: {user['user_id']}, Flag: {user['flag']}")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        try:
            login_page = Login(driver)
            login_page.login(user["user_id"])

            write_login_status(
                USER_DATA_FILE,
                row=user["row"],
                status="Login Successful",
                flag="Y"
            )

            steps_page = Steps(driver)
            steps_page.open_create_file_page(
                user["user_id"]
            )

        except Exception as e:

            write_login_status(
                USER_DATA_FILE,
                row=user["row"],
                status=f"Failed - {type(e).__name__}",
                flag="N"
            )

            print(f"Error: {e}")

        finally:
            driver.quit()

# Step 2: Process special user after everyone else is Y
users = get_all_users(USER_DATA_FILE)

special_user = next(
    (
        u for u in users
        if str(u["user_id"]).strip() == SPECIAL_USER_ID
        and u["flag"].strip().upper() == "N"
    ),
    None
)

if special_user:

    print(
        f"All users completed. Processing special user "
        f"{SPECIAL_USER_ID}, Flag: {special_user['flag']}"
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        login_page = Login(driver)
        login_page.login(special_user["user_id"])

        write_login_status(
            USER_DATA_FILE,
            row=special_user["row"],
            status="Login Successful",
            flag="Y"
        )

        steps_page = Steps(driver)
        steps_page.open_create_file_page(
            special_user["user_id"]
        )

    finally:
        driver.quit()

print("All users including special user completed.")










# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--ignore-ssl-errors")
# options.add_argument("--allow-insecure-localhost")

# USER_DATA_FILE = "data/userdata.xlsm"


# users = get_all_users(USER_DATA_FILE)


# for user in users:

#     count_n = sum(1 for user in users if user["flag"].strip().upper() == "N")
#     count_y = sum(1 for user in users if user["flag"].strip().upper() == "Y")
#     print(f"Total users with flag 'N': {count_n}")
#     print(f"Total users with flag 'Y': {count_y}")
#     print(f"Running login for: {user['user_id']}, Flag: {user['flag']}")
    
#     if user["flag"].strip().upper() == "N" :

#         driver = webdriver.Chrome(
#             service=Service(
#                 ChromeDriverManager().install()
#             ),
#             options=options
#         )
#         # base_page = BasePage(driver)
#         # base_page.handle_ssl_warning()
#         try:

          

#             login_page = Login(driver)
#             login_page.login(user["user_id"])

#             write_login_status(
#                 USER_DATA_FILE,
#                 row=user["row"],
#                 status="Login Successful",
#                 flag="Y"
#             )

#             steps_page = Steps(driver)
#             steps_page.open_create_file_page(user["user_id"])

#             # Optional
#             # steps_page.logout()

#         except TimeoutException:

#             write_login_status(
#                 USER_DATA_FILE,
#                 row=user["row"],
#                 status="Timeout",
#                 flag="N"
#             )

#             take_screenshot(
#                 driver,
#                 "TimeoutException"
#             )

#             print(
#                 "ERROR: Dropdown or option not visible within timeout"
#             )

#         except NoSuchElementException:

#             write_login_status(
#                 USER_DATA_FILE,
#                 row=user["row"],
#                 status="Element Not Found",
#                 flag="N"
#             )

#             take_screenshot(
#                 driver,
#                 "NoSuchElementException"
#             )

#             print(
#                 "ERROR: Category dropdown/option not found"
#             )

#         except ElementClickInterceptedException:

#             write_login_status(
#                 USER_DATA_FILE,
#                 row=user["row"],
#                 status="Click Intercepted",
#                 flag="N"
#             )

#             take_screenshot(
#                 driver,
#                 "ElementClickInterceptedException"
#             )

#             print(
#                 "ERROR: Element click intercepted by another element"
#             )

#         except Exception as e:

#             write_login_status(
#                 USER_DATA_FILE,
#                 row=user["row"],
#                 status=f"Failed - {type(e).__name__}",
#                 flag="N"
#             )

#             take_screenshot(
#                 driver,
#                 "Exception_error"
#             )

#             print(
#                 f"Unexpected error: {e}"
#             )

#         finally:
#             driver.quit()


# # All users completed - shutdown PC
# # print("All users processed. Shutting down PC...")
# # sleep(5)

# # os.system("shutdown /s /t 0")   # Windows shutdown