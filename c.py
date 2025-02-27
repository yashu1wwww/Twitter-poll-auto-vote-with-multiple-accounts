from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# change user with twitter username & password with your password 
accounts = [
    ("user1", "password1"),
    ("user2", "password2"),
    ("user3", "password3"),
    ("user4", "password4"),
    ("user5", "password5"),
]

def login(username, password):
    try:
        driver = webdriver.Chrome()  # Open new browser instance
        driver.get("https://twitter.com/i/flow/login")

        # Wait for email field
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'text')))
        email = driver.find_element(By.NAME, 'text')
        email.send_keys(username)
        email.send_keys(Keys.ENTER)

        # Wait for password field
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)

        # Wait until login is successful
        WebDriverWait(driver, 10).until(EC.url_contains("home"))
        return driver  # Return driver instance for further use
    except Exception as e:
        print(f"Login failed for {username}: {e}")
        return None

def vote(driver, poll_url):
    try:
        driver.get(poll_url)
        time.sleep(4)  # Wait for poll to load
        
        option_xpath = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[2]/div/div/div/div/div[2]/div[3]/div/span/span"  # Selects Option 3

        driver.find_element(By.XPATH, option_xpath).click()
        time.sleep(2)  # Allow the vote to register
    except NoSuchElementException:
        print("Poll option not found.")
    except TimeoutException:
        print("Timed out while waiting for poll options.")

# Poll tweet URL (replace with actual poll link)
poll_url = "https://twitter.com/Bolly_BoxOffice/status/1826235498278600977"

# Iterate through accounts
for username, password in accounts:
    driver = login(username, password)
    if driver:
        vote(driver, poll_url)
        driver.quit()  # Close the browser after voting

print("Voting process completed.")
