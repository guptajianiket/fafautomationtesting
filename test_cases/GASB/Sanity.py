import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#project library
from page_elements.GASB.page_pobjects import header, footer
from automated_actions import testactions, basicuseraction, techactions
from page_elements.GASB.gasb_url_txt import basic_url, contructed_url


class BaseTest:
    @pytest.fixture(scope='class')
    def driver_setup(self):
        path = "C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe"
        driver = webdriver.Chrome(service=Service(path))
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(basic_url.home)
        yield driver
        driver.quit()

class TestHeader(BaseTest):
    ''' Sanity Test for header'''

    @pytest.fixture(scope='session')
    def setup(self):
        self.word = techactions.generate_random_finance_word(self)
        return self.word

    def test_headermenu_check_aboutus(self, driver_setup):
        '''To check the click and redirection functionality of the about us.'''
        driver = driver_setup
        try:
            driver.find_element(By.XPATH, header.aboutus).click()
            WebDriverWait(driver, 20).until(EC.url_changes(driver.current_url))
            assert driver.current_url == basic_url.about_us
        except (NoSuchElementException, TimeoutException):
            pytest.fail("About Us link not found or URL didn't change.")



    def test_headermenu_check_standards_guidance(self):
        '''To check the click and redirection functionality of the standards and guidance.'''
        try:
            self.driver.find_element(By.XPATH, header.standards_guidance).click()

            # Wait for the URL to change
            WebDriverWait(self.driver, 20).until(
                EC.url_changes(self.driver.current_url)
            )

        except (NoSuchElementException, TimeoutException):
            assert False
        else:
            # If the expected URL is reached, verify it
            assert self.driver.current_url == basic_url.standards_and_guidance

    def test_headermenu_check_projects(self):
        '''To check the click and redirection functionality of the projects.'''
        try:
            self.driver.find_element(By.XPATH, header.projects).click()

            # Wait for the URL to change
            WebDriverWait(self.driver, 20).until(
                EC.url_changes(self.driver.current_url)
            )

        except (NoSuchElementException, TimeoutException):
            assert False
        else:
            # If the expected URL is reached, verify it
            assert self.driver.current_url == basic_url.projects

    def test_headermenu_check_news_meetings(self):
        '''To check the click and redirection functionality of the about us.'''
        try:
            self.driver.find_element(By.XPATH, header.news_meetings).click()

            # Wait for the URL to change
            WebDriverWait(self.driver, 20).until(
                EC.url_changes(self.driver.current_url)
            )

        except (NoSuchElementException, TimeoutException):
            assert False
        else:
            # If the expected URL is reached, verify it
            assert self.driver.current_url == basic_url.news_and_meetings

    def test_logo_redirection_check(self):
        '''To check whether header logo is clickable and redirects to homepage'''
        try:
            self.driver.find_element(By.CLASS_NAME, header.logo).click()

            # Wait for the URL to change
            WebDriverWait(self.driver, 20).until(
                EC.url_changes(self.driver.current_url)
            )

        except (NoSuchElementException, TimeoutException):
            assert False
        else:
            # If the expected URL is reached, verify it
            assert self.driver.current_url == basic_url.home

    def test_about_us_hovercheck(self):
        try:
            element_to_hover = self.driver.find_element(By.XPATH,header.aboutus)
            basicuseraction.hover(self,element_to_hover)
        except NoSuchElementException:
            assert False
        else:
            time.sleep(0.5)
            element = self.driver.find_element(By.CLASS_NAME,header.menu_hover_section)
            return element.is_displayed()


    def test_standards_guidance_hovercheck(self):
        try:
            element_to_hover = self.driver.find_element(By.XPATH,header.standards_guidance)
            basicuseraction.hover(self, element_to_hover)
        except NoSuchElementException:
            assert False
        else:
            time.sleep(0.5)
            element = self.driver.find_elements(By.CLASS_NAME,header.menu_hover_section)[1]
            return element.is_displayed()

    def test_projects_hovercheck(self):
        try:
            element_to_hover = self.driver.find_element(By.XPATH, header.projects)
            basicuseraction.hover(self, element_to_hover)
        except NoSuchElementException:
            assert False
        else:
            time.sleep(0.5)
            element = self.driver.find_elements(By.CLASS_NAME, header.menu_hover_section)[2]
            return element.is_displayed()

    def test_news_meetings_hovercheck(self):
        try:
            element_to_hover = self.driver.find_element(By.XPATH, header.news_meetings)
            basicuseraction.hover(self, element_to_hover)
        except NoSuchElementException:
            assert False
        else:
            time.sleep(0.5)
            element = self.driver.find_elements(By.CLASS_NAME, header.menu_hover_section)[3]
            return element.is_displayed()

    @pytest.mark.search
    def test_header_search_icon(self):
        try:
            self.driver.find_element(By.XPATH, header.search_logo).click()
            time.sleep(1)
            element = self.driver.find_element(By.CLASS_NAME, header.search_box)
            assert element.is_displayed()
        except NoSuchElementException:
            assert False

    @pytest.mark.search
    def test_search_keyword(self, setup):
        time.sleep(2)
        try:
            self.driver.find_element(By.ID, header.search_box_text).send_keys(setup)
        except (NoSuchElementException, ElementNotInteractableException):
            assert False

    @pytest.mark.search
    def test_searchbox_search_icon(self, setup):
        try:
            self.driver.find_element(By.XPATH, header.search_icon).click()
        except (NoSuchElementException, ElementNotInteractableException):
            assert False
        else:
            time.sleep(2)
            expected_url = contructed_url.construct_expected_url(setup)
            testactions.verifyurl(self, expected_url)

    def test_headermenu_aboutus_aboutthegasb_menu_check(self):
        if self.test_about_us_hovercheck() == True:
            try:
                basicuseraction.hover(self,self.driver.find_element(By.XPATH, header.aboutus))
                time.sleep(0.5)
                self.driver.find_elements(By.CLASS_NAME,header.second_level_menu)[0].click()
                # Wait for the expected URL to be reached
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )

            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:

                assert self.driver.current_url == basic_url.about_the_gasb
        else:
            pytest.skip("About us hover check is failed.")

    def test_headermenu_aboutus_standardsettings_menu_check(self):
        if self.test_about_us_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.aboutus))
                time.sleep(0.5)
                basicuseraction.hover(self, self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[0])
                time.sleep(0.5)
                self.driver.find_element(By.XPATH,header.aboutus_aboutthegasb_menu1).click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:

                assert self.driver.current_url == basic_url.standards_setting_process
        else:
            pytest.skip("About us hover check is failed.")

    def test_headermenu_aboutus_pirprocess_menu_check(self):
        if self.test_about_us_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.aboutus))
                time.sleep(0.5)
                basicuseraction.hover(self, self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[0])
                time.sleep(1)
                self.driver.find_element(By.XPATH,header.aboutus_aboutthegasb_menu2).click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:

                assert self.driver.current_url == basic_url.post_implementation_review_process
        else:
            pytest.skip("About us hover check is failed.")


    def test_headermenu_aboutus_baordmembers_menu_check(self):
        if self.test_about_us_hovercheck() == True:
            try:
                basicuseraction.hover(self,self.driver.find_element(By.XPATH, header.aboutus))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME,header.second_level_menu)[1].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )

            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:

                assert self.driver.current_url == basic_url.board_members
        else:
            pytest.skip("About us hover check is failed.")

    def test_headermenu_aboutus_seniorstaff_menu_check(self):
        if self.test_about_us_hovercheck() == True:
            try:
                basicuseraction.hover(self,self.driver.find_element(By.XPATH, header.aboutus))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME,header.second_level_menu)[2].click()
                # Wait for the expected URL to be reached
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.senior_staff
        else:
            pytest.skip("About us hover check is failed.")


    def test_headermenu_aboutus_gasac_menu_check(self):
        if self.test_about_us_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.aboutus))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[3].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.governmental_accounting_standards_advisory_council
        else:
            pytest.skip("About us hover check is failed.")

    def test_headermenu_aboutus_gasbandtheusercommunity_menu_check(self):
        if self.test_about_us_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.aboutus))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[4].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.gasb_and_the_user_community
        else:
            pytest.skip("About us hover check is failed.")

    def test_headermenu_aboutus_academics_menu_check(self):
        if self.test_about_us_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.aboutus))
                time.sleep(0.5)
                basicuseraction.hover(self, self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[4])
                time.sleep(0.5)
                self.driver.find_element(By.XPATH,header.aboutus_gasbcommunity_menu1).click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:

                assert self.driver.current_url == basic_url.academics
        else:
            pytest.skip("About us hover check is failed.")

    def test_headermenu_aboutus_financialstatementusers_menu_check(self):
        if self.test_about_us_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.aboutus))
                time.sleep(0.5)
                basicuseraction.hover(self, self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[4])
                time.sleep(0.5)
                self.driver.find_element(By.XPATH,header.aboutus_gasbcommunity_menu2).click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:

                assert self.driver.current_url == basic_url.financial_statement_users
        else:
            pytest.skip("About us hover check is failed.")


    def test_headermenu_aboutus_contactus_menu_check(self):
        if self.test_about_us_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.aboutus))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[5].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.contact_us
        else:
            pytest.skip("About us hover check is failed.")


    def test_headermenu_standards_GARS_menu_check(self):
        if self.test_standards_guidance_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.standards_guidance))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[6].click()
                time.sleep(1)
                # Switch to the new tab
                self.driver.switch_to.window(self.driver.window_handles[1])
                # Wait for the new tab to open
                WebDriverWait(self.driver, 20).until(lambda driver: len(driver.window_handles) > 1)
                # get the current url in new tab
                new_tab_url = self.driver.current_url
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert new_tab_url == basic_url.gars
                # Close the new tab and switch back to the main tab

        else:
            pytest.skip("Standard and Guidance hover check is failed.")

    def test_headermenu_standards_pronouncements_menu_check(self):
        if self.test_standards_guidance_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.standards_guidance))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[7].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.pronouncements
        else:
            pytest.skip("Standard and Guidance hover check is failed.")

    def test_headermenu_standards_TIS_menu_check(self):
        if self.test_standards_guidance_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.standards_guidance))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[8].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.technical_inquiry_service
        else:
            pytest.skip("Standard and Guidance hover check is failed.")

    def test_headermenu_projects_currentprojects_menu_check(self):
        if self.test_projects_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.projects))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[9].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.current_projects
        else:
            pytest.skip("Projects hover check is failed.")

    def test_headermenu_projects_recentlycompleted_menu_check(self):
        if self.test_projects_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.projects))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[10].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.recently_completed_projects
        else:
            pytest.skip("Projects hover check is failed.")


    def test_headermenu_projects_otherresearch_staff_menu_check(self):
        if self.test_projects_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.projects))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[11].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.other_research_and_staff_projects
        else:
            pytest.skip("Projects hover check is failed.")

    def test_headermenu_projects_documentsforpubliccomment_staff_menu_check(self):
        if self.test_projects_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.projects))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[12].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.documents_for_public_comment
        else:
            pytest.skip("Projects hover check is failed.")

    def test_headermenu_projects_commentletters_menu_check(self):
        if self.test_projects_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.projects))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[13].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.comment_letters
        else:
            pytest.skip("Projects hover check is failed.")

    def test_headermenu_newsmeetings_livemeeting_menu_check(self):
        if self.test_news_meetings_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.news_meetings))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[14].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.live_meetings
        else:
            pytest.skip("News & Meetings hover check is failed.")

    def test_headermenu_newsmeetings_upcomingmeetings_menu_check(self):
        if self.test_news_meetings_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.news_meetings))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[15].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.upcoming_meetings
        else:
            pytest.skip("News & Meetings hover check is failed.")

    def test_headermenu_newsmeetings_pastmeetings_menu_check(self):
        if self.test_news_meetings_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.news_meetings))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[16].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.past_meetings
        else:
            pytest.skip("News & Meetings hover check is failed.")

    def test_headermenu_newsmeetings_inthenews_menu_check(self):
        if self.test_news_meetings_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.news_meetings))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[17].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.in_the_news
        else:
            pytest.skip("News & Meetings hover check is failed.")

    def test_headermenu_newsmeetings_otherarticles_menu_check(self):
        if self.test_news_meetings_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.news_meetings))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[18].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.other_articles
        else:
            pytest.skip("News & Meetings hover check is failed.")

    def test_headermenu_newsmeetings_educationwebinarvideo_menu_check(self):
        if self.test_news_meetings_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.news_meetings))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[19].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.educational_webinars
        else:
            pytest.skip("News & Meetings hover check is failed.")

    def test_headermenu_newsmeetings_podcast_menu_check(self):
        if self.test_news_meetings_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.news_meetings))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[20].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.podcasts
        else:
            pytest.skip("News & Meetings hover check is failed.")

    def test_headermenu_newsmeetings_requestagasbspeaker_menu_check(self):
        if self.test_news_meetings_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.news_meetings))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[21].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.request_a_gasb_speaker
        else:
            pytest.skip("News & Meetings hover check is failed.")

    def test_headermenu_newsmeetings_mediacontacts_menu_check(self):
        if self.test_news_meetings_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.news_meetings))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[22].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.media_contacts
        else:
            pytest.skip("News & Meetings hover check is failed.")

    def test_headermenu_newsmeetings_stayconnected_menu_check(self):
        if self.test_news_meetings_hovercheck() == True:
            try:
                basicuseraction.hover(self, self.driver.find_element(By.XPATH, header.news_meetings))
                time.sleep(1)
                self.driver.find_elements(By.CLASS_NAME, header.second_level_menu)[23].click()
                # Wait for the URL to change
                WebDriverWait(self.driver, 20).until(
                    EC.url_changes(self.driver.current_url)
                )
            except (NoSuchElementException, ElementNotInteractableException):
                assert False
            else:
                assert self.driver.current_url == basic_url.signup
        else:
            pytest.skip("News & Meetings hover check is failed.")

class Test_footer_sanity:
    ''' Sanity Test for footer'''
    from selenium.webdriver.common.action_chains import ActionChains
    path = Service("C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe")
    driver = webdriver.Chrome(service=path)
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(basic_url.home)
    time.sleep(3)


    driver.execute_script("window.scrollBy(0, 2800);")
    time.sleep(2)
    def test_footer_logo(self):
        testactions.click_and_verify_url(self,self.driver.find_element(By.XPATH,footer.footer_logo),basic_url.home)

    def test_footer_archive(self):
        testactions.click_and_verify_url(self,self.driver.find_element(By.XPATH, footer.archive), basic_url.archive)

    def test_footer_contact_us(self):
        testactions.click_and_verify_url(self, self.driver.find_element(By.XPATH, footer.contact_us), basic_url.contact_us)

    def test_footer_terms_of_use(self):
        testactions.click_and_verify_url(self, self.driver.find_element(By.XPATH, footer.terms_of_use), basic_url.terms_of_use)

    def test_footer_career(self):
        testactions.click_and_verify_url(self, self.driver.find_element(By.XPATH, footer.career), basic_url.faf_careers_and_advisory_roles)

    def test_footer_subscribe_button(self):
        testactions.click_and_verify_url(self, self.driver.find_element(By.CLASS_NAME,footer.subscribe), basic_url.signup)

    def test_footer_twitter_icon(self):
        pytest.skip("Test is not written yet")

    def test_footer_youtube_icon(self):
        pytest.skip("Test is not written yet")

    def test_footer_facebook_icon(self):
        pytest.skip("Test is not written yet")

    def test_footer_linkdn_icon(self):
        pytest.skip("Test is not written yet")

    def test_footer_privacy_policy(self):
        pytest.skip("Test is not written yet")

    def test_footer_copyright(self):
        pytest.skip("Test is not written yet")

    def test_footer_FASB(self):
        pytest.skip("Test is not written yet")

    def test_footer_GASB(self):
        pytest.skip("Test is not written yet")

    def test_footer_FAF(self):
        pytest.skip("Test is not written yet")
