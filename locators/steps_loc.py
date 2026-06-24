from selenium.webdriver.common.by import By


class StepsPageLocators:
   
    CLICK_EFILE_BTN = (
        By.XPATH,
        "//a[contains(@href,'/eFile') and .//span[normalize-space()='eFile']]"
    )

    CLICK_CREATE_FILE_BTN = (
        By.XPATH,
        "//a[@data-id-attr='file-create-on-navigation-bar' and @aria-label='FILE Create']"
    )
        
    DESCRIPTION_TEXTAREA = (
    By.ID,
    "input-file-creation-description"
    )
    CATEGORY_DROPDOWN = (
        By.XPATH,
        "//div[@role='button' and contains(@class,'p-dropdown-trigger')]"
    )

    CATEGORY_FILTER = (
        By.XPATH,
        "//input[contains(@class,'p-dropdown-filter')]"
    )

    CATEGORY_OPTION_EOFFICE = (
        By.XPATH,
        "//li[@role='option']//span[normalize-space()='eOffice']"
    )

    PROFILE_MENU = (
        By.XPATH,
        "//button[contains(@class,'user-profile-link')]"
    )

    # Continue button locator
    CONTINUE_BUTTON = (
        By.XPATH,
        "//button[@id='fileCreationSubmit']"
    )

    # Proceed button locator
    PROCEED_BUTTON = (
    By.XPATH,
    "//button[@type='submit' and @data-id-attr='ok']"
    )

    # Create Draft button locator
    DRAFT_MENU = (
    By.XPATH,
    "//a[@data-id-attr='menubar.fileView.draft']"
    )

    # Create New Draft button locator
    CREATE_NEW_DRAFT = (
    By.XPATH,
    "//a[@data-id-attr='menubar.fileView.createNewDraft']"
    )

    # upload file input locator
    UPLOAD_BUTTON = (
    By.ID,
    "draft-file-upload"
    )

    # Draft Subject
    DRAFT_SUBJECT_TEXTAREA = (
    By.ID,
    "subject"
    )
    # Draft Save
    DRAFT_SAVE_BUTTON = (
    By.ID,
    "save"
    )
    # Approve Button
    APPROVE_BUTTON = (
        By.ID,
        "approve"
    )

    # Confirmation Yes Button
    CONFIRM_YES_BUTTON = (
        By.CSS_SELECTOR,
        'button[data-id-attr="ok"]'
    )

    # DSC Sign Button
    DSC_SIGN_BUTTON = (
        By.ID,
        "DSC"
    )

    # DSC Custom Option
    DSC_CUSTOM_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'dropdown-menu')]//button[normalize-space()='Custom']"
    )

        # Send Menu
    SEND_MENU_BUTTON = (
        By.CSS_SELECTOR,
        '[data-id-attr="menubar.fileView.send"]'
    )

    # Recent 10 Tab
    RECENT_10_TAB = (
        By.CSS_SELECTOR,
        '[data-id-attr="recent-tab"] button'
    )

    # Final Send Button
    FINAL_SEND_BUTTON = (
        By.ID,
        'send'
    )

    # Recent 10 Table Rows
    RECENT_10_TABLE_ROWS = (
        By.CSS_SELECTOR,
        'table[data-id-attr="send-to-recent-five-table"] tbody tr'
    )

    # Logout button locator
    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[@data-id-attr='logout']"
    )

