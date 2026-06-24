from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.create_file_page_loc import CreateFilePageLocators


class CreateFile(BasePage):

    def open_create_file(self):

        self.driver.get(
            CreateFilePageLocators.CREATE_FILE_URL
        )

    def click_create_file(self):

        create_btn = self.wait.until(
            EC.element_to_be_clickable(
                CreateFilePageLocators.CREATE_FILE_BUTTON
            )
        )

        create_btn.click()


    def enter_subject(self, subject):

        field = self.wait.until(
            EC.element_to_be_clickable(
                CreateFilePageLocators.FILE_SUBJECT
            )
        )

        field.clear()
        field.send_keys(subject)


    def enter_description(self, description):

        field = self.wait.until(
            EC.element_to_be_clickable(
                CreateFilePageLocators.FILE_DESCRIPTION
            )
        )

        field.send_keys(description)


    def upload_document(self, file_path):

        upload = self.wait.until(
            EC.presence_of_element_located(
                CreateFilePageLocators.UPLOAD_FILE
            )
        )

        upload.send_keys(file_path)


    def save_file(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                CreateFilePageLocators.SAVE_BUTTON
            )
        )

        button.click()


    def submit_file(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                CreateFilePageLocators.SUBMIT_BUTTON
            )
        )

        button.click()