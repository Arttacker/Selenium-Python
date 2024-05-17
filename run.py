from booking.booking import Booking
from utils import start_driver
import threading


def run_booking_script():
    driver = start_driver()
    with Booking(driver, teardown=False) as bot:
        bot.load_home_page()
        bot.start_dismissing_suggestions()
        bot.set_currency("EUR")
        bot.search_place_to_go("New York")
        bot.select_dates("2024-05-20", "2024-05-23")
        bot.define_passengers_ages()


if __name__ == '__main__':
    # Create a thread to run the booking script
    booking_thread = threading.Thread(target=run_booking_script)
    booking_thread.start()

    # Wait for the thread to complete if necessary
    booking_thread.join()
