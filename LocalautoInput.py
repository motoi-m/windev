import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# クロームの立ち上げ
driver = webdriver.Chrome()

# ページ接続
driver.get("http://localhost/wordpress/register/")

username = driver.find_element(By.XPATH, '//*[@id="user_login-6"]')
sei = driver.find_element(By.XPATH, '//*[@id="first_name-6"]')
mei = driver.find_element(By.XPATH, '//*[@id="last_name-6"]')
mailaddress = driver.find_element(By.XPATH, '//*[@id="user_email-6"]')
userpass = driver.find_element(By.XPATH, '//*[@id="user_password-6"]')
userpass2 = driver.find_element(By.XPATH, '//*[@id="confirm_user_password-6"]')
addbutton = driver.find_element(By.XPATH, '//*[@id="um-submit-btn"]')

filename = "sample.csv"
with open(filename, encoding="utf-8-sig", newline="") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        name = row[0]
        name2 = row[1]
        name3 = row[2]
        mailadd = row[3]
        pass1 = row[4]
        pass2 = row[5]
        username.send_keys(name)
        sei.send_keys(name2)
        mei.send_keys(name3)
        mailaddress.send_keys(mailadd)
        userpass.send_keys(pass1)
        userpass2.send_keys(pass2)
        addbutton.click()
        time.sleep(3)


time.sleep(5)
# 画面キャプチャを取得
# driver.save_screenshot("次へ進む実行後の画面.png")


# 10秒終了を待つ
time.sleep(10)

# クロームの終了処理
# driver.close()
