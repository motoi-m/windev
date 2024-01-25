import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import subtask

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select

# クロームの立ち上げ
driver = webdriver.Chrome()
# ActionChainsをインスタンス化
action = webdriver.ActionChains(driver)

# ログインページ接続
driver.get("https://stage.webmatchingsystem.com/")

userName = ""

filecsv = "csv/keiyaku.csv"
with open(filecsv, encoding="utf-8-sig", newline="") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        csv_orderNm = row[0]  # 発注者
        csv_contractorNm = row[1]  # 受注者
        csv_pass = row[2]  # pass
        # csv_cate1 = row[3]  # カテゴリ
        # csv_cate2 = row[4]  # サブカテゴリ
        csv_title = row[5]  # タイトル

        # 発注者でログイン後、案件一覧から案件を検索し案件表示画面へ
        subtask.loginToKakutei(driver, csv_orderNm, csv_pass, csv_title)

        # 提案を見るをクリック
        box1 = driver.find_element(By.XPATH, '//*[@id="bzmp_apply_list"]/div[1]/div[1]')
        # box2 = driver.find_element(By.XPATH, '//*[@id="bzmp_apply_list"]/div[2]/div[1]')
        # box3 = driver.find_element(By.XPATH, '//*[@id="bzmp_apply_list"]/div[3]/div[1]')
        if box1.text == csv_contractorNm:
            btn1 = driver.find_element(By.XPATH, '//*[@id="bzmp_apply_list"]/div[1]/div[6]/a')
            driver.execute_script("arguments[0].click();", btn1)
        # elif box2.text == csv_contractorNm:
        #    btn2 = driver.find_element(By.XPATH, '//*[@id="bzmp_apply_list"]/div[2]/div[6]/a')
        #   driver.execute_script("arguments[0].click();", btn2)
        # elif box3.text == csv_contractorNm:
        # btn3 = driver.find_element(By.XPATH, '//*[@id="bzmp_apply_list"]/div[3]/div[6]/a')
        # driver.execute_script("arguments[0].click();", btn3)

        # 選定するをクリック
        senteiButton = driver.find_element(By.XPATH, ('//*[@id="apply_view_select"]'))
        driver.execute_script("arguments[0].click();", senteiButton)
        alert = driver.switch_to.alert
        alert.accept()

        # 発注するをクリック
        time.sleep(2)
        orderButton = driver.find_element(By.XPATH, ('//*[@id="apply_view_order"]'))
        driver.execute_script("arguments[0].click();", orderButton)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(1)

        # ログアウト
        logoutBtn = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a")
        logoutBtn.click()

        # 受注者でログイン後、案件一覧から案件を検索し案件表示画面へ
        subtask.loginToKakutei(driver, csv_contractorNm, csv_pass, csv_title)

        # お気に入りに登録ボタンクリック
        # favoriteButton = driver.find_element(By.XPATH, '//*[@id="work_view_favadd"]')
        # favoriteButton.click()
        time.sleep(1)
        # 提案を見るをクリック
        teianButton = driver.find_element(By.XPATH, '//*[@id="bzmp_apply_list"]/div/div[6]/a')
        driver.execute_script("arguments[0].click();", teianButton)

        # 受注ボタンクリック
        contButton = driver.find_element(By.XPATH, ('//*[@id="apply_view_accept"]'))
        driver.execute_script("arguments[0].click();", contButton)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)

        # ログアウト
        logoutBtn = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a")
        logoutBtn.click()
        time.sleep(1)
