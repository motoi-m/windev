import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# 案件を登録(有料会員の発注データ＝ユーザーごとに3件/無料会員の受注データ＝ユーザーごとに2件)
PAIDMAXCOUNT = 3
FREEMAXCOUNT = 2
userCnt = 0
maxCnt = PAIDMAXCOUNT

# クロームの立ち上げ
driver = webdriver.Chrome()

# ログインページ接続
driver.get("https://experience.dev-salon.com/login/")

lineCnt = 0
filecsv = "csv/paiduserprof.csv"
with open(filecsv, encoding="utf-8-sig", newline="") as f:
    csvreader = csv.reader(f)  # まず有料会員が10件読み込まれる
    for row in csvreader:
        csv_userNm = row[0]
        csv_pass = row[1]
        csv_syoukai = row[2]
        csv_skill = row[3]
        csv_sikaku = row[4]
        csv_type = row[5]

        if lineCnt == 0:
            # ログイン
            loginUser = driver.find_element(By.XPATH, '//*[@id="username-6"]')
            loginPass = driver.find_element(By.XPATH, '//*[@id="user_password-6"]')
            loginBtn = driver.find_element(By.XPATH, '//*[@id="um-submit-btn"]')
            loginUser.send_keys(csv_userNm)
            loginPass.send_keys(csv_pass)
            loginBtn.click()

        # マイページボタンをクリック
        mypageBtn = driver.find_element(By.XPATH, '//*[@id="menu-item-341"]/a')
        mypageBtn.click()
        time.sleep(2)

        # 編集
        editBtn = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/div/div/div[5]/a")
        editBtn.click()

        # 要素取得
        syoukai = driver.find_element(By.XPATH, '//*[@id="description"]')
        skill = driver.find_element(By.XPATH, '//*[@id="skill"]')
        sikaku = driver.find_element(By.XPATH, '//*[@id="credential"]')
        type = driver.find_element(By.XPATH, '//*[@id="um_field_575_business-type"]/div[2]/span/span[1]/span/ul')
        # select = Select(type)
        # select.select_by_index(int(csv_type))
        type.send_keys(csv_type)
        time.sleep(2)

        # データセット
        syoukai.send_keys(csv_syoukai)
        skill.send_keys(csv_skill)
        sikaku.send_keys(csv_sikaku)

        time.sleep(10)

        # スクロール
        driver.find_element(By.TAG_NAME, "body").click()
        for i in range(5):
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)

        # 更新
        kousinBtn = driver.find_element(
            By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/div/div/div[5]/form/div[2]/div[1]/input"
        )
        kousinBtn.click()
        time.sleep(2)

        logoutBtn = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a")
        logoutBtn.click()

        loginBtn = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a[2]")
        loginBtn.click()
