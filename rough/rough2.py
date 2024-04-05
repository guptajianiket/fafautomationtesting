import time

from selenium import webdriver
from selenium.common import NoSuchElementException

from PageElements.Component_Variable import Component_Variable
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Test_Edit_Component:
    driver = webdriver.Chrome()
    driver.implicitly_wait(25)
    driver.get(Component_Variable.comp_url)
    driver.maximize_window()
    time.sleep(10)
    # original_window = driver.current_window_handle  # Store the original window handle
    # try:
    #     # Wait for the new window to appear
    #     WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)
    #     # Switch to the new window
    #     driver.switch_to.window(driver.window_handles[1])  # Assuming the new window is the second window handle
    #     time.sleep(10)
    #     # Mimic keyboard actions using pyautogui
    #     email = "avyas"
    #     pyautogui.write(email)
    #     # Press Tab to move to the password field
    #     pyautogui.press('tab')
    #      password = "Tr1d10n"
    #     pyautogui.write(password)
    #     # Press Tab to move to the OK button and then press Enter
    #     pyautogui.press('tab')
    #     pyautogui.press('enter')
    #     driver.switch_to.window(original_window)
    # print(comp)
    # exp = driver.find_element(By.ID, "PublishModal")
    # print(exp)
    # time.sleep(10)
    # act = driver.title
    # # comp_name = driver.find_element(By.CSS_SELECTOR, "#kaeser01").screenshot_as_png
    # # print(comp_name)
    # print(act)
    # exp = "Tridion Smart Authoring"
    # if (act == exp):
    #     print("User is on the Fonto editor")
    # else:
    #     print("User is not on the Fonto editor")

    driver.switch_to.frame(0)

    def test_001(self):  # Heading
        try:
            heading = self.driver.find_element(By.XPATH, Component_Variable.heading)
            heading.clear()
            heading.send_keys("Component Content Alliance sets new standard in content development and strategy")
            # self.driver.find_element(By.XPATH, Component_Variable.save).click()
            # self.driver.refresh();
            # original_window = self.driver.current_window_handle  # Store the original window handle
            # try:
            #     # Wait for the new window to appear
            #     time.sleep(10)
            #     pyautogui.press('enter')
            #     time.sleep(10)
            assert True
        except NoSuchElementException:
            self.driver.title()
            # print("Test case Failed")
            # self.driver.get_screenshot_as_png(self.driver.get_screenshot_as_file(self, filename="C:\\Users\\akanksha.vyas\\Downloads\\screenshot.png"))
            assert False

    def test_002(self):  # Description
        try:
            des = self.driver.find_element(By.XPATH, Component_Variable.description)
            des.clear()
            pyautogui.press('down')
            # des.send_keys("We take our role as a key component of the global and sustainable supply chain seriously and look forward to sharing our success in this area with our clients worldwide.")
            pyautogui.write(
                "RWS, a unique, world-leading provider of technology-enabled language, content and intellectual property solutions, announces the launch of the Component Content Alliance (CCA), a global community that brings together content experts, thought leaders and technical professionals to collaborate, share insights and drive innovation in component content development.")
            pyautogui.press('enter')
            pyautogui.write(
                "“While the benefits of component content – also known as structured content – are clear, many teams still rely on outdated approaches that result in content duplication, poor findability and inconsistent experiences,” comments Elsa Sklavounou, VP of Global Partnerships in the Content Technology Solution Group at RWS. “Our community, which is brought together by a shared passion for advancing component content, seeks to address these issues by collaborating on best practice.”")
            # self.driver.find_element(By.XPATH, Component_Variable.save).click()
            # self.driver.refresh();
            time.sleep(10)
            assert True
        except NoSuchElementException:
            # print("Test case Failed")
            # self.driver.get_screenshot_as_png(self.driver.get_screenshot_as_file(self, filename="C:\\Users\\akanksha.vyas\\Downloads\\screenshot.png"))
            assert False

    def test_003(self):  # Date
        try:
            comp_date = self.driver.find_element(By.XPATH, Component_Variable.date)
            comp_date.clear()
            pyautogui.press('down')
            # comp_date.send_keys("2024-02-17T17:43:14.583")
            pyautogui.write("2024-02x   -17T17:43:14.583")
            # comp_date.click()
            # comp_date.find_element(By.XPATH, Component_Variable.date_select)
            # comp_date.find_element(By.XPATH, Component_Variable.date_submit).click()
            assert True
        except NoSuchElementException:
            assert False

    def test_004(self):  # Author
        try:
            comp_date = self.driver.find_element(By.XPATH, Component_Variable.author)
            comp_date.clear()
            pyautogui.press('down')
            pyautogui.write("Chalfont Saint Peter, UK")
            self.driver.find_element(By.XPATH, Component_Variable.save).click()
            # comp_date.click()
            # comp_date.find_element(By.XPATH, Component_Variable.date_select)
            # comp_date.find_element(By.XPATH, Component_Variable.date_submit).click()
            assert True
        except NoSuchElementException:
            assert False

    def test_005(self):  # Image
        try:
            comp_date = self.driver.find_element(By.XPATH, Component_Variable.image)
            comp_date.clear()
            pyautogui.press('down')
            self.driver.find_element(By.XPATH, Component_Variable.image_replace).click()
            time.sleep(0.5)
            if self.driver.find_element(By.XPATH, Component_Variable.popup_xpath).is_displayed():
                self.driver.find_element(By.XPATH, Component_Variable.tridion_image)
                pyautogui.doubleClick
                time.sleep(2)
                self.driver.find_element(By.XPATH, Component_Variable.select_image)
                pyautogui.doubleClick
                time.sleep(2)
            else:
                print(Exception)
                assert False
            # comp_date.send_keys("2024-02-17T17:43:14.583")
            # pyautogui.write("")
            self.driver.find_element(By.XPATH, Component_Variable.save).click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, Component_Variable.comp_url)
            # comp_date.click()
            # comp_date.find_element(By.XPATH, Component_Variable.date_select)
            # comp_date.find_element(By.XPATH, Component_Variable.date_submit).click()
            assert True
        except NoSuchElementException:
            assert False