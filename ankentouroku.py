import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import utilize

# from selenium.webdriver.support.select import Select

# クロームの立ち上げ
driver = webdriver.Chrome()

# ログインページ接続
driver.get(utilize.siteUrl())

userName = ""
filecsv = "csv/anken.csv"
with open(filecsv, encoding="utf-8-sig", newline="") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        csv_userNm = row[0]
        csv_pass = row[1]
        csv_cate1 = row[2]
        csv_cate2 = row[3]
        csv_type = row[4]
        csv_title = row[5]
        csv_detail = row[6]
        csv_budget = row[7]
        csv_sYear = row[8]
        csv_sMonth = row[9]
        csv_sDay = row[10]
        csv_eYear = row[11]
        csv_eMonth = row[12]
        csv_eDay = row[13]
        csv_kibou = row[14]
        csv_file1 = row[15]
        csv_file2 = row[16]
        csv_file3 = row[17]

        if userName != "" and userName != csv_userNm:
            # ２回目以降の読み込みでユーザーが変わっていたらログアウト
            logoutBtn = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a")
            logoutBtn.click()

        # ユーザーが変わっていたらログイン
        if userName != csv_userNm:
            # ログイン画面に遷移
            loginBtn = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a[2]")
            loginBtn.click()
            # ログイン
            loginUser = driver.find_element(By.XPATH, '//*[@id="username-6"]')
            loginPass = driver.find_element(By.XPATH, '//*[@id="user_password-6"]')
            loginUser.send_keys(csv_userNm)
            loginPass.send_keys(csv_pass)
            loginBtn = driver.find_element(By.XPATH, '//*[@id="um-submit-btn"]')
            loginBtn.click()

        # 案件登録ボタンをクリック
        ankenBtn = driver.find_element(By.XPATH, '//*[@id="menu-item-210"]/a')
        ankenBtn.click()
        time.sleep(2)
        category1 = driver.find_element(By.XPATH, '//*[@id="work_edit_category_main"]')
        category1.send_keys(csv_cate1)
        time.sleep(2)
        category2 = driver.find_element(By.XPATH, '//*[@id="work_edit_category_sub"]')
        category2.send_keys(csv_cate2)
        time.sleep(1)
        matchType = driver.find_element(By.XPATH, '//*[@id="work_edit_type"]')
        matchType.send_keys(csv_type)
        """
        category1 = driver.find_element(By.CSS_SELECTOR, "#work_edit_category_main")
        select = Select(category1)
        select.select_by_index(int(csv_cate1))
        time.sleep(2)
        category2 = driver.find_element(By.CSS_SELECTOR, "#work_edit_category_sub")
        select = Select(category2)
        select.select_by_index(int(csv_cate2))
        time.sleep(3)
        # matchType = driver.find_element(By.CSS_SELECTOR, "#work_edit_type")
        # select = Select(matchType)
        # select.select_by_index(int(csv_type))
        """
        title = driver.find_element(By.XPATH, '//*[@id="work_edit_title"]')
        detail = driver.find_element(By.XPATH, '//*[@id="work_edit_about_work"]')
        budget = driver.find_element(By.XPATH, '//*[@id="work_edit_price"]')
        fromYmd = driver.find_element(By.XPATH, '//*[@id="work_edit_date_begin"]')
        toYmd = driver.find_element(By.XPATH, '//*[@id="work_edit_date_end"]')
        kibou = driver.find_element(By.XPATH, '//*[@id="work_edit_request"]')
        tempFile1 = driver.find_element(By.XPATH, '//*[@id="bzmp_work_attachment_file"]')
        tempFile2 = driver.find_element(By.XPATH, '//*[@id="bzmp_work_attachment_movie"]')

        # データセット
        title.send_keys(csv_title)
        detail.send_keys(csv_detail)
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
        time.sleep(1)
        fromYmd.send_keys(csv_sDay)
        time.sleep(1)

        toYmd.send_keys(csv_eYear)
        time.sleep(1)
        toYmd.send_keys(Keys.RIGHT)
        time.sleep(1)
        toYmd.send_keys(csv_eMonth)
        time.sleep(1)
        toYmd.send_keys(Keys.RIGHT)
        time.sleep(1)
        toYmd.send_keys(csv_eDay)

        kibou.send_keys(csv_kibou)

        driver.execute_script("arguments[0].scrollIntoView();", tempFile2)
        if (csv_file1) != "-":
            tempFile1.send_keys(csv_file1)
            time.sleep(1)

        if (csv_file3) != "-":
            tempFile2.send_keys(csv_file3)
            time.sleep(35)

        # 内容確認に進むクリック(フォーカス移動)
        button1 = driver.find_element(By.XPATH, '//*[@id="work_edit_next"]')
        driver.execute_script("arguments[0].click();", button1)
        time.sleep(2)

        if (csv_file2) != "-":
            # 添付ファイルが２つあれば一旦登録画面に戻る
            button_Back = driver.find_element(By.XPATH, '//*[@id="work_confirm_back"]')
            driver.execute_script("arguments[0].click();", button_Back)

            tempFile1 = driver.find_element(By.XPATH, '//*[@id="bzmp_work_attachment_file"]')
            driver.execute_script("arguments[0].scrollIntoView();", tempFile1)
            tempFile1.send_keys(csv_file2)
            time.sleep(1)
            # 内容確認に進むクリック(フォーカス移動)
            button1 = driver.find_element(By.XPATH, '//*[@id="work_edit_next"]')
            driver.execute_script("arguments[0].click();", button1)
            time.sleep(2)

        # 利用規約に同意して公開する
        button2 = driver.find_element(By.XPATH, '//*[@id="work_confirm_submit"]')
        driver.execute_script("arguments[0].click();", button2)
        time.sleep(2)

        userName = csv_userNm
