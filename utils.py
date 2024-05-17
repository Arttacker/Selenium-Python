from selenium import webdriver
from selenium.webdriver.edge.options import Options


def start_driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    driver.implicitly_wait(2)
    return driver
