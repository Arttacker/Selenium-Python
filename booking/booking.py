import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from booking import constants as const
from selenium.webdriver.common.action_chains import ActionChains


class Booking:
    def __init__(self, driver: webdriver.Edge, teardown=False):
        self.driver = driver
        self.teardown = teardown
        self.stop_checking = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.stop_dismissing_suggestions()
            self.driver.quit()

    def load_home_page(self):
        self.driver.get(const.BASE_URL)

    def set_currency(self, currency: str = None):
        try:
            # Wait until the element is clickable
            set_currency_element = WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='header-currency-picker-trigger']")))
            # Scroll the element into view
            self.driver.execute_script("arguments[0].scrollIntoView();", set_currency_element)

            # Ensure no other element is covering the button
            ActionChains(self.driver).move_to_element(set_currency_element).perform()

            # Click the button using JavaScript to avoid interception
            self.driver.execute_script("arguments[0].click();", set_currency_element)

            # Now handle the currency selection
            currency_btn_to_choose = self.driver.find_element(By.XPATH,
                f"//button/div/div/span[div[text()='{currency}']]")
            self.driver.execute_script("arguments[0].click();", currency_btn_to_choose)

        except TimeoutException:
            print("The currency picker button was not found or not clickable.")
        except Exception as e:
            print(f"An error occurred while setting the currency: {e}")

    def dismiss_signup_suggestion(self, timeout=2, check_interval=1):
        while not self.stop_checking:
            try:
                WebDriverWait(self.driver, timeout, poll_frequency=check_interval).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Dismiss sign-in info.']")))
                cancel_btn = self.driver.find_element(By.XPATH, "//button[@aria-label='Dismiss sign-in info.']")
                print("Sign-up suggestion dismissed.")
                cancel_btn.click()
            except TimeoutException:
                print("No sign-up suggestion found, continuing to check...")
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                time.sleep(check_interval)

    def start_dismissing_suggestions(self, timeout=2, check_interval=1):
        self.stop_checking = False
        self.thread = threading.Thread(target=self.dismiss_signup_suggestion, args=(timeout, check_interval))
        self.thread.start()

    def stop_dismissing_suggestions(self):
        self.stop_checking = True
        self.thread.join()

    def search_place_to_go(self, place: str):
        search_field = self.driver.find_element(By.ID, ":re:")
        search_field.clear()
        search_field.send_keys(place)
        time_to_sleep = 0.5
        try:
            time.sleep(time_to_sleep)
            self.choose_first_suggested_place()
        except NoSuchElementException:
            print("couldn't catch it")
            time_to_sleep += 1
            time.sleep(time_to_sleep)
            self.choose_first_suggested_place()

    def choose_first_suggested_place(self):
        first_suggested_place = self.driver.find_element(By.XPATH, "//div[@class='d7430561e2']")
        # Ensure no other element is covering the button
        ActionChains(self.driver).move_to_element(first_suggested_place).perform()
        # Click the button using JavaScript to avoid interception
        self.driver.execute_script("arguments[0].click();", first_suggested_place)

    def select_dates(self, checkin_date, checkout_date):
        # Select check-in date
        checkin_date_to_be_selected = self.driver.find_element(
            By.CSS_SELECTOR,
            f'span[data-date="{checkin_date}"]'
        )
        # Ensure no other element is covering the button
        ActionChains(self.driver).move_to_element(checkin_date_to_be_selected).perform()
        # Click the button using JavaScript to avoid interception
        self.driver.execute_script("arguments[0].click();", checkin_date_to_be_selected)

        # Select check-out date
        checkout_date_to_be_selected = self.driver.find_element(
            By.CSS_SELECTOR,
            f'span[data-date="{checkout_date}"]'
        )
        # Ensure no other element is covering the button
        ActionChains(self.driver).move_to_element(checkout_date_to_be_selected).perform()
        # Click the button using JavaScript to avoid interception
        self.driver.execute_script("arguments[0].click();", checkout_date_to_be_selected)
