from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# List of accounts with usernames and passwords
accounts = [
    ("user1", "user2"),
    ("user2", "password2"),
    ("user3", "password3"),
    ("user4", "password4"),
    ("user5", "password5"),
    ("user6", "password6"),
    ("user7", "password7"),
    ("user8", "password8"),
    ("user9", "password9"),
    ("user10", "password10"),
    ("user11", "password11"),
    ("user12", "password12"),
    ("user13", "password13"),
    ("user14", "password14"),
    ("user15", "password15"),
    ("user16", "password16"),
    ("user17", "password17"),
    ("user18", "password18"),
    ("user19", "password19"),
    ("user20", "password20"),
]

def login(driver, username, password):
    try:
        # Open Twitter login page
        driver.get("https://twitter.com/i/flow/login")

        # Wait for the email field to be present and interactable
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'text'))
        )
        email = driver.find_element(By.NAME, 'text')
        email.send_keys(username)
        email.send_keys(Keys.ENTER)

        # Wait for the password field to be present and interactable
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)
        
        # Wait for the login to complete
        WebDriverWait(driver, 10).until(
            EC.url_contains("home")
        )
    except TimeoutException:
        print(f"Login timed out for username: {username}")
    except NoSuchElementException as e:
        print(f"Element not found during login for username: {username}. Exception: {e}")

def vote(driver, poll_url):
    try:
        # Navigate to the poll tweet
        driver.get(poll_url)
        
        time.sleep(4)
        
        options_xpath = [
            # Here, I want to vote for 3 options in the poll, so I uncommented the corresponding lines. I removed the remaining options that I don't want.
            
            #"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[2]/div/div/div/div/div[2]/div[1]/div/span/span",  # Option 1
             #"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[2]/div/div/div/div/div[2]/div[2]/div/span/span",  # Option 2
            "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[2]/div/div/div/div/div[2]/div[3]/div/span/span",  # Option 3
            # "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[2]/div/div/div/div/div[2]/div[4]/div/span/span"   # Option 4
        ]

        # Ensure only one option is uncommented
        if len(options_xpath) == 1:
            driver.find_element(By.XPATH, options_xpath[0]).click()
        else:
            print("Please ensure only one option is uncommented.")
    except NoSuchElementException:
        print("Poll options not found.")
    except TimeoutException:
        print("Timed out while waiting for poll options.")

def logout(driver):
    try:
        # Log out from Twitter
        driver.get("https://twitter.com/logout")
        
        # Wait for the logout process to complete
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'text'))
        )
    except TimeoutException:
        print("Logout timed out.")

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# URL of the poll
poll_url = "https://twitter.com/Bolly_BoxOffice/status/1826235498278600977"  # Replace with your URL to vote...

# Iterate through each account
for current_index in range(len(accounts)):
    username, password = accounts[current_index]
    login(driver, username, password)
    vote(driver, poll_url)
    logout(driver)

# Close the browser once done
driver.quit()
