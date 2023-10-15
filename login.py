import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# クロームの立ち上げ
driver = webdriver.Chrome()

# ログインページ接続
driver.get("https://experience.dev-salon.com/login/")

filecsv_userProf = "csv/userprof.csv"
with open(filecsv_userProf, encoding="utf-8-sig", newline="") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        csv_userNm = row[0]
        csv_pass = row[1]
        csv_pass2 = row[2]
        csv_mailAdd = row[3]
        csv_houjinNm = row[4]
        csv_houjinNo = row[5]

        loginUser = driver.find_element(By.XPATH, '//*[@id="username-6"]')
        loginPass = driver.find_element(By.XPATH, '//*[@id="user_password-6"]')
        loginBtn = driver.find_element(By.XPATH, '//*[@id="um-submit-btn"]')
        loginUser.send_keys(csv_userNm)
        loginPass.send_keys(csv_pass)
        loginBtn.click()

        # 案件トップに遷移
        # 案件トップのマイページをクリック
        mypage = driver.find_element(By.XPATH, '//*[@id="menu-item-341"]')
        mypage.click()
        time.sleep(5)
