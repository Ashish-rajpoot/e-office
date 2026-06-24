from selenium.webdriver.common.by import By


class CreateFilePageLocators:

    # Create File URL
    CREATE_FILE_URL = (
        # "https://districts.upeoffice.gov.in/efile"
        "https://districts.upeoffice.gov.in/efile/#/file/create"
    )

    EFILE_LINK = (
        By.XPATH,
        "//a[.//span[text()='eFile']]"
    )


    # EFILE_LINK = (
    # By.XPATH,
    # "//a[@href='https://districts.upeoffice.gov.in/eFile']"
    # )
    # Example fields (update after inspecting page)

    FILE_SUBJECT = (
        By.XPATH,
        "//input[@placeholder='Subject']"
    )


    FILE_DESCRIPTION = (
        By.XPATH,
        "//textarea"
    )


    UPLOAD_FILE = (
        By.XPATH,
        "//input[@type='file']"
    )


    SAVE_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Save')]"
    )


    SUBMIT_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Submit')]"
    )