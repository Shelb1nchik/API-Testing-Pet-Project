import os
import time
import allure
BASE_URL = "https://the-internet.herokuapp.com"

def test_add_elements(driver):

    driver.get(f"{BASE_URL}/add_remove_elements/")

    for i in range(4):
        driver.find_element("xpath", "//button[text()='Add Element']").click()
        if i % 2 == 0:
            driver.find_element("xpath", "//button[text()='Delete']").click()

    buttonsDelete = driver.find_elements("xpath", "//button[text()='Delete']")

    count = len(buttonsDelete)

    assert count == 2

def test_basic_auth(driver):
    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

    text = driver.find_element("tag name", "p").text
    assert "Congratulations" in text

def test_dropdown_list(driver):
    driver.get(f"{BASE_URL}/dropdown")

    driver.find_element("xpath", "//select[@id='dropdown']").click()
    driver.find_element("xpath", '//*[@id="dropdown"]/option[3]').click()

def wait_for_download(download_dir, files_before, timeout=10):
    """
    Ждём появления нового файла в папке download_dir.
    Возвращает имя нового файла.
    """
    for _ in range(timeout):
        files_after = set(os.listdir(download_dir))
        new_files = files_after - files_before
        if new_files:
            return new_files.pop()
        time.sleep(1)
    raise TimeoutError("Файл не появился в папке за отведённое время")
def test_file_downloader(driver):
    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)
    files_before = set(os.listdir(download_dir))

    driver.get("https://the-internet.herokuapp.com/download")
    driver.find_elements("xpath", "//a")[1].click()

    downloaded_file = wait_for_download(download_dir, files_before)
    print(f"Скачан файл: {downloaded_file}")

    assert downloaded_file is not None

def test_file_uploader(driver):
    driver.get(f"{BASE_URL}/upload")

    upload_files = driver.find_element("xpath", "//input[@id='file-upload']")

    upload_files.send_keys(f"{os.getcwd()}/downloads/e226c28c-8c66-471c-9230-dd14bf4c1c09.tmp")

def test_login(driver):

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element("id", "username").send_keys("tomsmith")
    driver.find_element("id", "password").send_keys("SuperSecretPassword!")

    driver.find_element("css selector", "button[type='submit']").click()

    message = driver.find_element("id", "flash").text

    assert "You logged into a secure area!" in message

def test_wrong_password(driver):

    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element("id", "username").send_keys("tomsmith")
    driver.find_element("id", "password").send_keys("wrongpassword")

    driver.find_element("css selector", "button[type='submit']").click()

    message = driver.find_element("id", "flash").text

    assert "Your password is invalid!" in message

@allure.feature("UI Testing")
@allure.story("Add/Remove Elements")
def test_add_elements(driver):
    with allure.step("Открываем страницу Add/Remove Elements"):
        driver.get(f"{BASE_URL}/add_remove_elements/")

    with allure.step("Добавляем 4 элемента и удаляем каждый второй"):
        for i in range(4):
            driver.find_element("xpath", "//button[text()='Add Element']").click()
            if i % 2 == 0:
                driver.find_element("xpath", "//button[text()='Delete']").click()

    with allure.step("Проверяем количество кнопок Delete"):
        buttons_delete = driver.find_elements("xpath", "//button[text()='Delete']")
        assert len(buttons_delete) == 2


@allure.feature("UI Testing")
@allure.story("Basic Auth")
def test_basic_auth(driver):
    with allure.step("Открываем страницу Basic Auth с логином и паролем"):
        driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

    with allure.step("Проверяем сообщение после авторизации"):
        text = driver.find_element("tag name", "p").text
        assert "Congratulations" in text


@allure.feature("UI Testing")
@allure.story("Dropdown List")
def test_dropdown_list(driver):
    with allure.step("Открываем страницу Dropdown"):
        driver.get(f"{BASE_URL}/dropdown")

    with allure.step("Выбираем третий пункт из списка"):
        driver.find_element("xpath", "//select[@id='dropdown']").click()
        driver.find_element("xpath", '//*[@id="dropdown"]/option[3]').click()


@allure.feature("UI Testing")
@allure.story("File Download")
def test_file_downloader(driver):
    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)
    files_before = set(os.listdir(download_dir))

    with allure.step("Открываем страницу Download"):
        driver.get(f"{BASE_URL}/download")

    with allure.step("Кликаем на файл для скачивания"):
        driver.find_elements("xpath", "//a")[1].click()

    with allure.step("Ждём появления нового файла в папке downloads"):
        downloaded_file = wait_for_download(download_dir, files_before)
        assert downloaded_file is not None
        allure.attach.file(
            os.path.join(download_dir, downloaded_file),
            name="Downloaded File",
            attachment_type=allure.attachment_type.TEXT
        )


@allure.feature("UI Testing")
@allure.story("File Upload")
def test_file_uploader(driver):
    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)
    file_path = os.path.join(download_dir, "test_file.txt")
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Hello, Selenium!")

    with allure.step("Открываем страницу Upload"):
        driver.get(f"{BASE_URL}/upload")

    with allure.step("Загружаем тестовый файл"):
        upload_input = driver.find_element("xpath", "//input[@id='file-upload']")
        upload_input.send_keys(file_path)


@allure.feature("UI Testing")
@allure.story("Login")
def test_login(driver):
    with allure.step("Открываем страницу Login"):
        driver.get(f"{BASE_URL}/login")

    with allure.step("Вводим правильный логин и пароль"):
        driver.find_element("id", "username").send_keys("tomsmith")
        driver.find_element("id", "password").send_keys("SuperSecretPassword!")
        driver.find_element("css selector", "button[type='submit']").click()

    with allure.step("Проверяем сообщение успешного входа"):
        message = driver.find_element("id", "flash").text
        assert "You logged into a secure area!" in message


@allure.feature("UI Testing")
@allure.story("Login")
def test_wrong_password(driver):
    with allure.step("Открываем страницу Login"):
        driver.get(f"{BASE_URL}/login")

    with allure.step("Вводим правильный логин и неправильный пароль"):
        driver.find_element("id", "username").send_keys("tomsmith")
        driver.find_element("id", "password").send_keys("wrongpassword")
        driver.find_element("css selector", "button[type='submit']").click()

    with allure.step("Проверяем сообщение об ошибке"):
        message = driver.find_element("id", "flash").text
        assert "Your password is invalid!" in message