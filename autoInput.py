import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# クロームの立ち上げ
driver = webdriver.Chrome()

# ページ接続
driver.get("https://account.onamae.com/accountCreate")

username = driver.find_element(By.XPATH, '//*[@id="lnameML"]')
userpass = driver.find_element(By.XPATH, '//*[@id="editAccountForm"]/p[2]')
addbutton = driver.find_element(By.XPATH, '//*[@id="editAccountForm"]/p[2]')

filename = "sample.csv"
with open(filename, encoding="utf-8-sig", newline="") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        name = row[0]
        code = row[1]
        username.send_keys(name)
        userpass.send_keys(code)
        addbutton.click()
        time.sleep(3)


time.sleep(5)
# 画面キャプチャを取得
driver.save_screenshot("次へ進む実行後の画面.png")


# 10秒終了を待つ
time.sleep(10)

# クロームの終了処理
# driver.close()
