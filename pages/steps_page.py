from time import sleep

from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

from locators.steps_loc import StepsPageLocators
from utils.file_manager import FileManager
from utils.loader import wait_for_loader_to_disappear
from utils.workflow_runner import Step, WorkflowRunner
# from utils.loader import wait_for_loader

load_dotenv()

description = os.getenv("DESCRIPTION", "e-office Pramaan Patra")
class Steps:
   
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def wait_for_loader(self):
        try:
            self.wait.until(
                EC.invisibility_of_element_located(
                    (By.CSS_SELECTOR, ".progress-loader-wrapper")
                )
            )
        except Exception:
            pass


    def click_e_file_btn(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(StepsPageLocators.CLICK_EFILE_BTN)
        )

        element = self.wait.until(
            EC.element_to_be_clickable(StepsPageLocators.CLICK_EFILE_BTN)
        )
        element.click()

        wait_for_loader_to_disappear(self)
        
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(
                StepsPageLocators.CLICK_CREATE_FILE_BTN
            )
        )


    def click_create_file_btn(self):
        element = self.wait.until(
            EC.element_to_be_clickable(StepsPageLocators.CLICK_CREATE_FILE_BTN)
        )
        element.click()

    def select_file_head_1(self):
        self.wait_for_loader()
        element = self.wait.until(
                    EC.presence_of_element_located(
                        (By.ID, "input-fileHeadBasic")
                    )
                )

        select = Select(element)

                # Recommended
        select.select_by_value("190")

        print("File head selected successfully")

    def select_file_head_2(self):
        self.wait_for_loader()
        element=self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "input-fileHeadPrimary")
            )
        )

        self.wait.until(
            lambda driver:
            any(
                option.get_attribute("value") == "6603"
                for option in Select(
                    driver.find_element(By.ID, "input-fileHeadPrimary")
                ).options
            )
        )

        select = Select(
           element
        )

        select.select_by_value("6603")
        

    def select_file_head_3(self):
        self.wait_for_loader()
        element=self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "input-fileHeadSecondary")
            )
        )

        self.wait.until(
            lambda driver:
            any(
                option.get_attribute("value") == "61975"
                for option in Select(
                    driver.find_element(By.ID, "input-fileHeadSecondary")
                ).options
            )
        )

        select = Select(
           element
        )

        select.select_by_value("61975")
        print("File head selected successfully")

    def add_description(self):
        try:
            textarea = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.DESCRIPTION_TEXTAREA
                )
            )

            textarea.clear()
            textarea.send_keys(description)
            # textarea.send_keys(Keys.TAB)
            # self.driver.find_element(
            #     By.XPATH,
            #     "//label[contains(.,'Main Category')]"
            # ).click()
        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/description_error.png"
            )
            raise Exception(f"Adding description failed: {e}")
        


    def select_category_eoffice(self):
        try:
            self.wait_for_loader()

            # Leave textarea if still focused
            self.driver.switch_to.active_element.send_keys(Keys.TAB)

            # Open dropdown
            dropdown = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.CATEGORY_DROPDOWN
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                dropdown
            )

            # Wait for search box to appear
            search_box = self.wait.until(
                EC.visibility_of_element_located(
                    StepsPageLocators.CATEGORY_FILTER
                )
            )

            search_box.clear()
            search_box.send_keys("eOffice")

            # Select option
            option = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.CATEGORY_OPTION_EOFFICE
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                option
            )

            print("eOffice selected successfully")

        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/category_error.png"
            )
            raise Exception(
                f"Category selection failed: {e}"
            ) 
        


    def click_continue(self):
        try:
            btn = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.CONTINUE_BUTTON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                btn
            )

        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/continue_error.png"
            )
            raise Exception(f"Clicking continue failed: {e}")


    def click_proceed(self):
        try:
            btn = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.PROCEED_BUTTON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                btn
            )

        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/proceed_error.png"
            )
            raise Exception(f"Clicking proceed failed: {e}")


    def click_draft_menu(self):
        try:
            menu = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.DRAFT_MENU
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                menu
            )

        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/draft_menu_error.png"
            )
            raise Exception(f"Clicking draft menu failed: {e}")
        
    def click_create_new_draft(self):
        try:
            option = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.CREATE_NEW_DRAFT
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                option
            )

        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/create_new_draft_error.png"
            )
            raise Exception(f"Clicking create new draft failed: {e}")


    def upload_draft(self, mobile_number):

        file_path = FileManager.get_draft_file(
            mobile_number
        )

        upload = self.wait.until(
            EC.presence_of_element_located(
                StepsPageLocators.UPLOAD_BUTTON
            )
        )

        upload.send_keys(file_path)

        print(f"Uploaded: {file_path}")


    def enter_draft_subject(self, subject):
        try:
            textarea = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.DRAFT_SUBJECT_TEXTAREA
                )
            )

            textarea.clear()
            textarea.send_keys(subject)

        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/draft_subject_error.png"
            )
            raise Exception(f"Entering draft subject failed: {e}")
        
        
    def save_draft(self):
        try:
            btn = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.DRAFT_SAVE_BUTTON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                btn
            )

        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/draft_save_error.png"
            )
            raise Exception(f"Saving draft failed: {e}")

    def click_approve(self):
        try:
            btn = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.APPROVE_BUTTON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                btn
            )

        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/approve_error.png"
            )
            raise Exception(f"Clicking approve failed: {e}")
    
    def confirm_approval(self):
        try:
            btn = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.CONFIRM_YES_BUTTON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                btn
            )

        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/confirm_approval_error.png"
            )
            raise Exception(f"Approval confirmation failed: {e}")
        
        
    def click_dsc_sign(self):
        try:
            btn = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.DSC_SIGN_BUTTON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                btn
            )

        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/dsc_sign_error.png"
            )
            raise Exception(f"DSC Sign click failed: {e}")
        
        
    def select_dsc_custom(self):
        try:
            btn = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.DSC_CUSTOM_BUTTON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                btn
            )
            
            input("Please complete the DSC signing process and press Enter to continue...")

        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/dsc_custom_error.png"
            )
            raise Exception(f"Selecting DSC Custom failed: {e}")
        
        

    def click_send_menu(self):
        try:
            btn = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.SEND_MENU_BUTTON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                btn
            )

        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/send_menu_error.png"
            )
            raise Exception(f"Opening send menu failed: {e}")
        
    def click_recent_10_tab(self):
        try:
            btn = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.RECENT_10_TAB
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                btn
            )

        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/recent_10_tab_error.png"
            )
            raise Exception(f"Opening Recent 10 tab failed: {e}")
        
        
    def select_recent_user(self,name,marking_abbr,section):
        try:

            rows = self.wait.until(
                EC.presence_of_all_elements_located(
                    StepsPageLocators.RECENT_10_TABLE_ROWS
                )
            )

            print("Rows found:", len(rows))

            for row in rows:
                print(row.text)
                
            for row in rows:

                row_name = row.find_element(
                    By.CSS_SELECTOR,
                    'td[data-id-attr="name"]'
                ).text.strip()

                row_abbr = row.find_element(
                    By.CSS_SELECTOR,
                    'td[data-id-attr="marking-abbr"]'
                ).text.strip()

                row_section = row.find_element(
                    By.CSS_SELECTOR,
                    'td[data-id-attr="section"]'
                ).text.strip()

                if (
                    row_name == name
                    and row_abbr == marking_abbr
                    and row_section == section
                ):

                    radio = row.find_element(
                        By.CSS_SELECTOR,
                        'input[type="radio"]'
                    )

                    self.driver.execute_script(
                        "arguments[0].click();",
                        radio
                    )

                    return

            raise Exception(
                f"User not found: {name} | {marking_abbr}"
            )

        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/select_recent_user_error.png"
            )
            raise Exception(
                f"Selecting user from Recent 10 failed: {e}"
            )
            
            
    def click_final_send(self):
        try:
            btn = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.FINAL_SEND_BUTTON
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                btn
            )

        except Exception as e:
            self.driver.save_screenshot(
                "screenshots/final_send_error.png"
            )
            raise Exception(f"Sending file failed: {e}")
    
    
    def logout(self):
        try:

            self.wait_for_loader()

            # Open profile menu
            profile_btn = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.PROFILE_MENU
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                profile_btn
            )

            # Click logout
            logout_btn = self.wait.until(
                EC.element_to_be_clickable(
                    StepsPageLocators.LOGOUT_BUTTON
                )
            )
            print("Clicking logout button...")
            sleep(2)  # Wait for any potential animations or transitions
            self.driver.execute_script(
                "arguments[0].click();",
                logout_btn
            )

            print("Logout successful")

        except Exception as e:

            self.driver.save_screenshot(
                "screenshots/logout_error.png"
            )

            raise Exception(
                f"Logout failed: {e}"
            )
                 

    def open_create_file_page(self, user_id):

        steps = [
            Step(self.click_e_file_btn, 5),
            Step(self.click_create_file_btn, 2),
            Step(self.select_file_head_1, 1),
            Step(self.select_file_head_2, 1),
            Step(self.select_file_head_3, 1),
            Step(self.add_description, 1),
            Step(self.select_category_eoffice, 1),
            Step(self.click_continue, 3),
            Step(self.click_proceed, 3),
            Step(self.click_draft_menu, 2),
            Step(self.click_create_new_draft, 2),
            Step(lambda: self.upload_draft(user_id), 20),
            Step(lambda: self.enter_draft_subject(description), 1),
            Step(self.save_draft, 3),
            Step(self.click_approve, 2),
            Step(self.confirm_approval, 3),
            # Step(self.click_dsc_sign, 2),
            # Step(self.select_dsc_custom, 0),
            Step(self.click_send_menu, 2),
            Step(self.click_recent_10_tab, 2),
            Step(
                lambda: self.select_recent_user(
                    name=os.getenv("TARGET_NAME"),
                    marking_abbr=os.getenv("TARGET_ABBR"),
                    section=os.getenv("TARGET_SECTION")
                ),
                2
            ),
            Step(self.click_final_send, 3),
        ]

        WorkflowRunner.run(steps)
        # input("Press Enter to logout...")
        self.logout()
   