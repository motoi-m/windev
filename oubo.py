import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import utilize

# クロームの立ち上げ
driver = webdriver.Chrome()

# ログインページ接続
driver.get(utilize.siteUrl() + "login/")

userNm = ""
filecsv = "csv/oubo.csv"
with open(filecsv, encoding="utf-8-sig", newline="") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        csv_userNm = row[0]
        csv_pass = row[1]
        csv_cate1 = row[2]
        csv_cate2 = row[3]
        csv_type = row[4]
        csv_title = row[5]
        csv_budget = row[6]
        csv_sYear = row[7]
        csv_sMonth = row[8]
        csv_sDay = row[9]
        csv_eYear = row[10]
        csv_eMonth = row[11]
        csv_eDay = row[12]
        csv_detail = row[13]
        csv_pr = row[14]
        csv_file1 = row[15]
        csv_file2 = row[16]

        if userNm != csv_userNm:
            if userNm != "":
                # ユーザーが変わったらログアウト後再ログイン
                logoutBtn = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a")
                logoutBtn.click()
                # トップページからログイン
                loginBtn = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a[2]")
                loginBtn.click()
                lineCnt = 0
            # ログイン
            loginUser = driver.find_element(By.XPATH, '//*[@id="username-6"]')
            loginPass = driver.find_element(By.XPATH, '//*[@id="user_password-6"]')
            loginBtn = driver.find_element(By.XPATH, '//*[@id="um-submit-btn"]')
            loginUser.send_keys(csv_userNm)
            loginPass.send_keys(csv_pass)
            loginBtn.click()

        # 案件検索ボタンをクリック
        ankenSbtn = driver.find_element(By.XPATH, '//*[@id="menu-item-211"]/a')
        ankenSbtn.click()
        # 案件名
        srh_title = driver.find_element(By.XPATH, ('//*[@id="bzmp_worklist_search_keyword"]'))  # 案件名
        srh_title.send_keys(csv_title)

        time.sleep(1)
        # srh_type = driver.find_element(By.XPATH, ('//*[@id="bzmp_worklist_search_type"]'))  # 種別
        # srh_type.send_keys(csv_type)
        srhButton = driver.find_element(By.XPATH, ('//*[@id="bzmp_worklist_search_submit"]'))  # 検索ボタン
        srhButton.click()

        # 検索結果から案件をさがす
        matching_element = driver.find_element(By.LINK_TEXT, (csv_title))  # 案件名
        # 案件の位置までスクロール
        driver.execute_script("arguments[0].scrollIntoView();", matching_element)
        time.sleep(1)
        # 案件をクリック
        matching_element.click()
        # 案件表示画面から「応募する」をクリック
        ouboButton = driver.find_element(By.XPATH, ('//*[@id="work_view_apply"]'))
        driver.execute_script("arguments[0].click();", ouboButton)
        time.sleep(2)

        # 応募画面の各要素を取得
        budget = driver.find_element(By.XPATH, '//*[@id="apply_edit_price"]')
        fromYmd = driver.find_element(By.XPATH, '//*[@id="apply_edit_date_begin"]')
        toYmd = driver.find_element(By.XPATH, '//*[@id="apply_edit_date_end"]')
        detail = driver.find_element(By.XPATH, '//*[@id="apply_edit_note"]')
        pr = driver.find_element(By.XPATH, '//*[@id="apply_edit_skill"]')
        tempFile1 = driver.find_element(By.XPATH, '//*[@id="apply_edit_file"]')
        tempFile2 = driver.find_element(By.XPATH, '//*[@id="bzmp_apply_attachment_movie"]')

        # データセット
        budget.send_keys(csv_budget)
        fromYmd.send_keys(csv_sYear)
        time.sleep(1)
        # 月へフォーカス後入力
        fromYmd.send_keys(Keys.RIGHT)
        time.sleep(1)
        fromYmd.send_keys(csv_sMonth)
        time.sleep(1)
        # 日へフォーカス後入力
        fromYmd.send_keys(Keys.RIGHT)
        time.sleep(2)
        fromYmd.send_keys(csv_sDay)
        time.sleep(2)
        toYmd.send_keys(csv_eYear)
        time.sleep(2)
        toYmd.send_keys(Keys.RIGHT)
        time.sleep(2)
        toYmd.send_keys(csv_eMonth)
        time.sleep(1)
        toYmd.send_keys(Keys.RIGHT)
        time.sleep(1)
        toYmd.send_keys(csv_eDay)
        detail.send_keys(csv_detail)
        pr.send_keys(csv_pr)
        if csv_file1 != "-":
            tempFile1.send_keys(csv_file1)
        if csv_file2 != "-":
            tempFile2.send_keys(csv_file2)
        # time.sleep(10)

        # 内容確認に進むクリック
        button1 = driver.find_element(By.XPATH, '//*[@id="apply_edit_next"]')
        driver.execute_script("arguments[0].click();", button1)
        time.sleep(2)

        # 利用規約に同意して公開する
        button2 = driver.find_element(By.XPATH, '//*[@id="apply_confirm_submit"]')
        driver.execute_script("arguments[0].click();", button2)
        time.sleep(2)

        userNm = csv_userNm
