from pages.create_file_page import CreateFile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from excel_reader import get_user_id
from pages.login import Login
from locators.create_file_page_loc import CreateFilePageLocators
from pages.base_page import BasePage


USER_DATA_FILE = "data/userdata.xlsm"

PROFILE_PATH = os.path.abspath("chrome_profile")


user_id = get_user_id(USER_DATA_FILE)


options = webdriver.ChromeOptions()

# Persistent Chrome session
options.add_argument(
    f"--user-data-dir={PROFILE_PATH}"
)


driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    ),
    options=options
)


wait = WebDriverWait(driver, 60)


def is_logged_in():

    """
    Check whether current session is already authenticated
    """

    driver.get(CreateFilePageLocators.CREATE_FILE_URL)

    time.sleep(5)

    current_url = driver.current_url.lower()

    # print("Current URL:", current_url)


    # Login page indicators
    if (
        "login" in current_url
        or "username_un" in driver.page_source
        or "signin" in driver.page_source.lower()
    ):
        return False

    return True



try:

    if is_logged_in():

        print(
            "Existing session found ✅"
        )



    else:

        print(
            "Session expired. Starting login..."
        )


        login_page = Login(driver)

        login_page.login(user_id)


        print(
            f"Login started for: {user_id}"
        )


        input(
            "Approve Tap Authentication on mobile and press Enter..."
        )


    # Open Create File page

    create_file = CreateFile(driver)
    # base_page = BasePage(driver)
    # base_page.check_and_refresh_on_error()

    create_file.open_create_file()


    # print(
    #     "Create File page opened"
    # )


    # create_file.enter_subject(
    #     "Test File From Selenium"
    # )


    # Future:
    # create_file.enter_description()
    # create_file.upload_document()
    # create_file.save_file()


    input(
        "Press Enter to close..."
    )


finally:
    driver.quit()


# from pages.create_file import CreateFile
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import os

# from excel_reader import get_user_id
# from pages.login import Login

# user_id = get_user_id("data/userdata.xlsm")

# PROFILE_PATH = os.path.abspath("chrome_profile")


# options = webdriver.ChromeOptions()

# # Store browser session
# options.add_argument(
#     f"--user-data-dir={PROFILE_PATH}"
# )


# driver = webdriver.Chrome(
#     service=Service(
#         ChromeDriverManager().install()
#     ),
#     options=options
# )

# try:
#     login_page = Login(driver)

#     login_page.login(user_id)

#     print(f"Logged in with: {user_id}")

#     input(
#         "Complete Tap Authentication on mobile and press Enter..."
#     )

#  # Create File
#     create_file = CreateFile(driver)

#     create_file.open_create_file()


#     create_file.enter_subject(
#         "Test File From Selenium"
#     )


#     # create_file.enter_description(
#     #     "Created automatically using Selenium"
#     # )


#     # create_file.upload_document(
#     #     r"C:\Documents\test.pdf"
#     # )


#     # create_file.save_file()

#     input(
#         "Complete Tap Authentication on mobile and press Enter..."
#     )

# finally:
#     driver.quit()







# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from webdriver_manager.chrome import ChromeDriverManager
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC

# # from locators.login_page import FileCreatePage, LoginPage
# # from excel_reader import get_user_id

# # # Read mobile number from Excel
# # user_id = get_user_id("data/userdata.xlsm")

# # driver = webdriver.Chrome(
# #     service=Service(ChromeDriverManager().install())
# # )

# # driver.get(FileCreatePage.ROOT_URL)

# # wait = WebDriverWait(driver, 60)

# # create_btn = wait.until(
# #     EC.element_to_be_clickable(FileCreatePage.CREATE_FILE_BUTTON)
# # )

# # create_btn.click()


# # username_box = wait.until(
# #     EC.presence_of_element_located(LoginPage.USERNAME_INPUT)
# # )

# # username_box.clear()
# # username_box.send_keys(user_id)

# # print(f"Entered User ID: {user_id}")
# # # Check Terms & Conditions checkbox
# # checkbox = wait.until(
# #     EC.element_to_be_clickable(LoginPage.TNC_CHECKBOX)
# # )

# # if not checkbox.is_selected():
# #     checkbox.click()

# # # Wait for Next button to become enabled
# # wait.until(
# #     lambda d: d.find_element(*LoginPage.NEXT_BUTTON).is_enabled()
# # )

# # # Click Next
# # next_btn = driver.find_element(*LoginPage.NEXT_BUTTON)
# # next_btn.click()

# # # Wait for Tap Authentication option
# # tap_auth = wait.until(
# #     EC.element_to_be_clickable(LoginPage.TAP_AUTH_OPTION)
# # )

# # tap_auth.click()

# # # Wait for Next button
# # next_btn = wait.until(
# #     EC.element_to_be_clickable(LoginPage.NEXT_BUTTON)
# # )

# # next_btn.click()

# # input("Press Enter to close...")
# # driver.quit()