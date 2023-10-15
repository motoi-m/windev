import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# クロームの立ち上げ
driver = webdriver.Chrome()

# ページ接続
driver.get("http://localhost/wordpress/register/")


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
        prof1 = row[6]
        prof2 = row[7]

        # 新規登録ページの要素
        username = driver.find_element(By.XPATH, '//*[@id="user_login-6"]')
        sei = driver.find_element(By.XPATH, '//*[@id="first_name-6"]')
        mei = driver.find_element(By.XPATH, '//*[@id="last_name-6"]')
        mailaddress = driver.find_element(By.XPATH, '//*[@id="user_email-6"]')
        userpass = driver.find_element(By.XPATH, '//*[@id="user_password-6"]')
        userpass2 = driver.find_element(By.XPATH, '//*[@id="confirm_user_password-6"]')
        addbutton = driver.find_element(By.XPATH, '//*[@id="um-submit-btn"]')
        # 新規登録ページにセット
        username.send_keys(name)
        sei.send_keys(name2)
        mei.send_keys(name3)
        mailaddress.send_keys(mailadd)
        userpass.send_keys(pass1)
        userpass2.send_keys(pass2)
        addbutton.click()

        # マイページに遷移
        # ギアアイコンをクリック
        gia = driver.find_element(By.XPATH, '//*[@id="page-10"]/div/div/div/div[1]/div[1]')
        gia.click()
        # プロフィールをクリック
        prof = driver.find_element(By.XPATH, '//*[@id="page-10"]/div/div/div/div[1]/div[1]/div/div/ul/li[1]/a')
        prof.click()
        # 項目１
        koumoku1 = driver.find_element(By.XPATH, '//*[@id="abc-8"]')
        koumoku1.send_keys(prof1)
        koumoku2 = driver.find_element(By.XPATH, '//*[@id="koumoku-8"]')
        koumoku2.send_keys(prof2)
        # 編集ボタンクリック
        button_prof = driver.find_element(By.XPATH, '//*[@id="page-10"]/div/div/div/form/div[4]/div[2]/div[1]/input')
        button_prof.click()
        time.sleep(5)

        # マイページのログアウトボタンをクリック
        logout = driver.find_element(By.XPATH, '//*[@id="main-menu"]/li[3]/a')
        logout.click()
        time.sleep(5)

        touroku = driver.find_element(By.XPATH, '//*[@id="main-menu"]/li[2]/a')
        touroku.click()

time.sleep(5)
# 画面キャプチャを取得
# driver.save_screenshot("次へ進む実行後の画面.png")


# 5秒終了を待つ
time.sleep(5)

# クロームの終了処理
# driver.close()
