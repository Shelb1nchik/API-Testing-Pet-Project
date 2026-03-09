from selenium.webdriver.common.by import By

BASE_URL = "https://the-internet.herokuapp.com"

def test_add_elements(driver):

    driver.get(f"{BASE_URL}/add_remove_elements/")

    for i in range(4):
        driver.find_element(By.XPATH, "//button[text()='Add Element']").click()
        if i % 2 == 0:
            driver.find_element(By.XPATH, "//button[text()='Delete']").click()

    buttonsDelete = driver.find_elements(By.XPATH, "//button[text()='Delete']")

    count = len(buttonsDelete)

    assert count == 2

def test_basic_auth(driver):
    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

    text = driver.find_element("tag name", "p").text
    assert "Congratulations" in text

def test_login(driver):

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    message = driver.find_element(By.ID, "flash").text

    assert "You logged into a secure area!" in message

def test_wrong_password(driver):

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    message = driver.find_element(By.ID, "flash").text

    assert "Your password is invalid!" in message

# def test_wrong_password():
#     options = Options()
#     options.add_argument("--disable-blink-features=AutomationControlled")
#
#     driver = webdriver.Chrome(options=options)
#
#     driver.get("https://papajohns.ru/sankt-peterburg")
#
#     driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
#
#     time.sleep(random.uniform(2, 3))
#
#     driver.find_element(By.CSS_SELECTOR, ".zoI7DuOAdLXS9CS9Ke6KB").click()
#
#     driver.find_element(By.XPATH, "//div[contains(text(),'Вход')]").click()
#     driver.find_element(By.XPATH, "//div[contains(text(),'Регистрация')]").click()
#
#     buttons = driver.find_elements(By.CSS_SELECTOR, "._1JE-0XQ7auJ3yGzkkNIOAR")
#     buttons[1].click()
#     buttons[2].click()
#
#     phone_input = driver.find_element(By.NAME, "phone")
#
#     for digit in "9999999999":
#         phone_input.send_keys(digit)
#         time.sleep(0.2)
#
#     time.sleep(2)
#
#     driver.find_element(By.XPATH, "//div[contains(text(),'Отправить код')]").click()