# Booking Automation with Selenium in Python

This project automates interactions with the Booking.com website using Selenium WebDriver. It includes functionalities such as loading the homepage, setting the currency, searching for a destination, selecting check-in and check-out dates.

## Project Structure

```
booking-automation/
│
├── booking/
│   ├── __init__.py
│   ├── booking.py
│   └── constants.py
├── requirements.txt
├── run.py
└── utils.py
```

## Files Description

- **booking/**
  - **booking.py**: Contains the main `Booking` class with methods to automate various actions on the Booking.com website.
  - **constants.py**: Stores constants used in the project, such as the base URL.
  - **__init__.py**: Makes the `booking` directory a package.

- **requirements.txt**: Lists the Python dependencies required to run the project.

- **run.py**: The main script to run the booking automation.

- **utils.py**: Contains utility functions, such as the function to start the WebDriver.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Saalehh/Selenium-Python.git
   cd Selenium-Python
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Download the Edge WebDriver**:
   Ensure you have the Edge WebDriver installed and it's compatible with your browser version. You can download it from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).

## Usage

1. **Modify the `constants.py` file**:
   Ensure the `BASE_URL` is set correctly:
   ```python
   BASE_URL = "https://www.booking.com"
   ```

2. **Run the automation script**:
   ```sh
   python run.py
   ```

   The script will perform the following actions:
   - Load the Booking.com homepage.
   - Start dismissing any signup suggestions that appear.
   - Set the currency to EUR.
   - Search for "New York".
   - Select check-in and check-out dates.

## Customization

- **Setting Different Currency**:
  Modify the currency code in `run.py`:
  ```python
  bot.set_currency("EUR")  # Change "EUR" to your desired currency code
  ```

- **Searching for a Different Place**:
  Modify the place in `run.py`:
  ```python
  bot.search_place_to_go("New York")  # Change "New York" to your desired destination
  ```

- **Selecting Different Dates**:
  Modify the dates in `run.py`:
  ```python
  bot.select_dates("2024-05-20", "2024-05-23")  # Change to your desired dates
  ```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
