import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# クロームの立ち上げ
driver = webdriver.Chrome()


# ページ接続
driver.get("http://localhost/wordpress/register/")

# 会員登録
# touroku = driver.find_element(By.XPATH, '//*[@id="main-menu"]/li[2]/a')
# touroku.click()


# script2.focusToElement(driver, By.XPATH, '//*[@id="first_name-6"]', True)
# element = driver.find_element(By.XPATH, '//*[@id="first_name-6"]')
# driver.execute_script("arguments[0].click();", element)
# element.send_keys("namae")

# 新規登録ページの要素
userNm = driver.find_element(By.XPATH, '//*[@id="user_login-6"]')
userNm.send_keys("user1")
"""
userPass = driver.find_element(By.XPATH, '//*[@id="user_password-6"]')
userPass.send_keys("Test1111")
userPass2 = driver.find_element(By.XPATH, '//*[@id="confirm_user_password-6"]')
userPass2.send_keys("Test1111")
mailAddress = driver.find_element(By.XPATH, '//*[@id="user_email-6"]')
mailAddress.send_keys("u1@test.com")
houjinNm = driver.find_element(By.XPATH, '//*[@id="shop_name-6"]')
houjinNm.send_keys("Itec株式会社")
houjinNo = driver.find_element(By.XPATH, '//*[@id="corporate_number-6"]')
houjinNo.send_keys("1234567890123")
# 後半

busyo = driver.find_element(By.XPATH, '//*[@id="department-6"]')
driver.execute_script("arguments[0].click();", busyo)
busyo.send_keys("システム部")
yakusyoku = driver.find_element(By.XPATH, '//*[@id="job_title-6"]')
yakusyoku.send_keys("課長")
tantouSei = driver.find_element(By.XPATH, '//*[@id="first_name-6"]')
tantouSei.send_keys("田中")
tantouMei = driver.find_element(By.XPATH, '//*[@id="first_name-758"]')
tantouMei.send_keys("太郎")
Address = driver.find_element(By.XPATH, '//*[@id="address-758"]')
tel = driver.find_element(By.XPATH, '//*[@id="mobile_number-758"]')
kiyaku = driver.find_element(
    By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/div[2]/div/form/div[2]/div[2]/label/span[1]/i"
)
"""
addbutton = driver.find_element(By.XPATH, '//*[@id="um-submit-btn"]')
driver.execute_script("arguments[0].click();", addbutton)
time.sleep(10)
