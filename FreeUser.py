import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# クロームの立ち上げ
driver = webdriver.Chrome()

# ページ接続
driver.get("https://experience.dev-salon.com/register/")
# 無料会員選択
freeuser = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/div/section[2]/div[3]/a")
freeuser.click()

filecsv_userNm = "user.csv"
with open(filecsv_userNm, encoding="utf-8-sig", newline="") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        csv_userNm = row[0]
        csv_pass = row[1]
        csv_pass2 = row[2]
        csv_mailAdd = row[3]
        csv_houjinNm = row[4]
        csv_houjinNo = row[5]
        csv_busyo = row[6]
        csv_yakusyoku = row[7]
        csv_tantouSei = row[8]
        csv_tantouMei = row[9]
        csv_add = row[10]
        csv_telNo = row[11]

        # 新規登録ページの要素
        userNm = driver.find_element(By.XPATH, '//*[@id="user_login-307"]')
        userPass = driver.find_element(By.XPATH, '//*[@id="user_password-307"]')
        userPass2 = driver.find_element(By.XPATH, '//*[@id="confirm_user_password-307"]')
        mailAddress = driver.find_element(By.XPATH, '//*[@id="user_email-307"]')
        houjinNm = driver.find_element(By.XPATH, '//*[@id="shop_name-307"]')
        houjinNo = driver.find_element(By.XPATH, '//*[@id="corporate_numbe-307"]')
        busyo = driver.find_element(By.XPATH, '//*[@id="manager_department-307"]')
        yakusyoku = driver.find_element(By.XPATH, '//*[@id="manager_title-307"]')
        tantouSei = driver.find_element(By.XPATH, '//*[@id="last_name-307"]')
        tantouMei = driver.find_element(By.XPATH, '//*[@id="first_name-307"]')
        Address = driver.find_element(By.XPATH, '//*[@id="address-307"]')
        tel = driver.find_element(By.XPATH, '//*[@id="mobile_number-307"]')
        addbutton = driver.find_element(By.XPATH, '//*[@id="um-submit-btn"]')

        # 新規登録ページにセット
        userNm.send_keys(csv_userNm)
        userPass.send_keys(csv_pass)
        userPass2.send_keys(csv_pass2)
        mailAddress.send_keys(csv_mailAdd)
        houjinNm.send_keys(csv_houjinNm)
        houjinNo.send_keys(csv_houjinNo)
        busyo.send_keys(csv_busyo)
        yakusyoku.send_keys(csv_yakusyoku)
        tantouSei.send_keys(csv_tantouSei)
        tantouMei.send_keys(csv_tantouMei)
        Address.send_keys(csv_add)
        tel.send_keys(csv_telNo)
        time.sleep(3)
        # 登録ボタンクリック
        addbutton.click()

        # 案件トップに遷移
        # 案件トップのログアウトボタンをクリック
        logout = driver.find_element(By.XPATH, '//*[@id="main-menu"]/li[3]/a')
        logout.click()
        time.sleep(5)


time.sleep(5)
# 画面キャプチャを取得
# driver.save_screenshot("次へ進む実行後の画面.png")


# 5秒終了を待つ
time.sleep(5)

# クロームの終了処理
# driver.close()
