from selenium.webdriver.common.by import By


class LoginPage:
    USERNAME_INPUT = (By.ID, "username_un")
    TNC_CHECKBOX = (By.ID, "tncCheckbox")
    NEXT_BUTTON = (By.ID, "next")

    TAP_AUTH_OPTION = (
        By.XPATH,
        "//li[contains(@class,'boxWrapper')][.//div[contains(.,'Tap Authentication')]]"
    )
    # Radio Button - raj*7103@up.gov.in
    RAJ_UP_GOV_EMAIL_RADIO = (
        By.CSS_SELECTOR,
        'input[type="radio"][name="email"][placeholder="raj*7103@up.gov.in"]'
    )
    
        # No Button
    NO_BUTTON = (
        By.XPATH,
        '//button[normalize-space()="No"]'
    )

class FileCreatePage:
    ROOT_URL = "https://districts.upeoffice.gov.in/"

    CREATE_FILE_BUTTON = (
        By.XPATH,
        "/html/body/div[2]/section/div/div/div/div[1]/button[2]"
    )


# # locators.py

# from selenium.webdriver.common.by import By

# class FileCreatePage:
#     ROOT_URL = "https://districts.upeoffice.gov.in"
#     # Button
#     CREATE_FILE_BUTTON = (
#         By.XPATH,
#         "/html/body/div[2]/section/div/div/div/div[1]/button[2]"
#     )

# class LoginPage:
#     USERNAME_INPUT = (By.ID,"username_un")
#     TNC_CHECKBOX = (By.ID, "tncCheckbox")
#     NEXT_BUTTON = (By.ID, "next")
#     TAP_AUTH_OPTION = (
#         By.XPATH,
#         "//li[contains(@class,'boxWrapper')]//div[contains(text(),'Tap Authentication')]"
#     )