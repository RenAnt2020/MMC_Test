from selenium.webdriver.common.by import By
def login(driver,username,password):
    driver.find_element(By.XPATH, '//input[@type="text"]').send_keys(username)
    driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//button[@type="button"]').click()
