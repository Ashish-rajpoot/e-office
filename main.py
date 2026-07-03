from pages.login import Login
from pages.steps_page import Steps

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException
)

from utils.screenshot import take_screenshot
from utils.clear_screenshots import clear_screenshots
from utils.excel_writer import write_login_status
from utils.excel_reader import get_all_users

import os

# --------------------------------------------------
# CONFIG
# --------------------------------------------------

USER_DATA_FILE = "data/userdata.xlsm"
SPECIAL_USER_ID = os.getenv("SPECIAL_USER_ID", "9412430321")
MAX_RETRIES = 3

clear_screenshots()

PROFILE_PATH = os.path.abspath("chrome_profile")

options = webdriver.ChromeOptions()

# options.add_argument("--headless=new")
options.add_argument("--start-maximized")
# options.add_argument("--start-minimized")
# options.add_argument("--disable-notifications")
# options.add_argument("--window-size=1920,1080")
# options.add_argument("--disable-gpu")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--no-sandbox")
options.set_capability(
    "acceptInsecureCerts",
    True
)

# Install/download chromedriver only once
driver_path = ChromeDriverManager().install()
# --------------------------------------------------
# PROCESS USER
# --------------------------------------------------

def process_user(user):

    user_id = str(user["user_id"]).strip()

    print(
        f"Processing User: {user_id} "
        f"User Name: {user['name']} "
        f"(Flag={user['flag']})"
    )

    driver = None

    try:

        # driver = webdriver.Chrome(
        #     service=Service(driver_path),
        #     options=options
        # )
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        login_page = Login(driver)
        login_page.login(user_id)

      
        steps_page = Steps(driver)
        steps_page.open_create_file_page(user_id)

        write_login_status(
            USER_DATA_FILE,
            row=user["row"],
            status="Login Successful",
            flag="Y"
        )

        print(f"SUCCESS: {user_id}")

        return True

    except TimeoutException:

        write_login_status(
            USER_DATA_FILE,
            row=user["row"],
            status="Timeout",
            flag="N"
        )

        if driver:
            take_screenshot(
                driver,
                f"{user_id}_TimeoutException"
            )

        print(
            f"TIMEOUT ERROR: {user_id}"
        )

        return False

    except NoSuchElementException:

        write_login_status(
            USER_DATA_FILE,
            row=user["row"],
            status="Element Not Found",
            flag="N"
        )

        if driver:
            take_screenshot(
                driver,
                f"{user_id}_NoSuchElement"
            )

        print(
            f"ELEMENT NOT FOUND: {user_id}"
        )

        return False

    except ElementClickInterceptedException:

        write_login_status(
            USER_DATA_FILE,
            row=user["row"],
            status="Click Intercepted",
            flag="N"
        )

        if driver:
            take_screenshot(
                driver,
                f"{user_id}_ClickIntercepted"
            )

        print(
            f"CLICK INTERCEPTED: {user_id}"
        )

        return False

    except Exception as e:

        write_login_status(
            USER_DATA_FILE,
            row=user["row"],
            status=f"Failed - {type(e).__name__}",
            flag="N"
        )

        if driver:
            take_screenshot(
                driver,
                f"{user_id}_Unexpected"
            )

        print(
            f"UNEXPECTED ERROR ({user_id}): {e}"
        )

        return False

    finally:

        if driver:
            driver.quit()


# --------------------------------------------------
# PROCESS NORMAL USERS
# --------------------------------------------------

for attempt in range(1, MAX_RETRIES + 1):

    print(
        f"\n{'=' * 50}"
        f"\nATTEMPT {attempt}/{MAX_RETRIES}"
        f"\n{'=' * 50}"
    )

    users = get_all_users(USER_DATA_FILE)

    pending_users = [
        u for u in users
        if str(u["user_id"]).strip() != SPECIAL_USER_ID
        and str(u["flag"]).strip().upper() == "N"
    ]

    if not pending_users:
        print(
            "All normal users completed successfully."
        )
        break

    print(
        f"Pending users: {len(pending_users)}"
    )

    for user in pending_users:
        process_user(user)

# --------------------------------------------------
# VERIFY ALL NORMAL USERS
# --------------------------------------------------

users = get_all_users(USER_DATA_FILE)

remaining_users = [
    u for u in users
    if str(u["user_id"]).strip() != SPECIAL_USER_ID
    and str(u["flag"]).strip().upper() == "N"
]

if remaining_users:

    print("\nSome users are still pending:")

    for user in remaining_users:
        print(
            f"User: {user['user_id']} "
            f"Flag: {user['flag']}"
        )

    print(
        "\nSkipping special user because "
        "not all users are Y."
    )

else:

    print(
        "\nAll normal users are Y."
    )

    special_user = next(
        (
            u for u in users
            if str(u["user_id"]).strip()
            == SPECIAL_USER_ID
        ),
        None
    )

    if special_user:

        if (
            str(special_user["flag"])
            .strip()
            .upper()
            == "N"
        ):

            print(
                f"\nProcessing Special User: "
                f"{SPECIAL_USER_ID}"
            )

            process_user(special_user)

        else:

            print(
                f"Special user "
                f"{SPECIAL_USER_ID} "
                f"is already Y."
            )

print(
    "\nExecution Completed."
)