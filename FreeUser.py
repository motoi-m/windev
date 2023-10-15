import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.select import Select

# クロームの立ち上げ
driver = webdriver.Chrome()

# ページ接続
driver.get("https://experience.dev-salon.com/")
# 会員登録
touroku = driver.find_element(By.CLASS_NAME, "btn_member")
touroku.click()
# 無料会員選択
freeuser = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/section[1]/div[3]/a")
freeuser.click()

filecsv = "csv/freeuser.csv"
with open(filecsv, encoding="utf-8-sig", newline="") as f:
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
        userNm = driver.find_element(By.XPATH, '//*[@id="user_login-758"]')
        userPass = driver.find_element(By.XPATH, '//*[@id="user_password-758"]')
        userPass2 = driver.find_element(By.XPATH, '//*[@id="confirm_user_password-758"]')
        mailAddress = driver.find_element(By.XPATH, '//*[@id="user_email-758"]')
        houjinNm = driver.find_element(By.XPATH, '//*[@id="shop_name-758"]')
        houjinNo = driver.find_element(By.XPATH, '//*[@id="corporate_number-758"]')
        busyo = driver.find_element(By.XPATH, '//*[@id="department-758"]')
        yakusyoku = driver.find_element(By.XPATH, '//*[@id="job_title-758"]')
        tantouSei = driver.find_element(By.XPATH, '//*[@id="last_name-758"]')
        tantouMei = driver.find_element(By.XPATH, '//*[@id="first_name-758"]')
        Address = driver.find_element(By.XPATH, '//*[@id="address-758"]')
        tel = driver.find_element(By.XPATH, '//*[@id="mobile_number-758"]')
        kiyaku = driver.find_element(
            By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/div[2]/div/form/div[2]/div[2]/label/span[1]/i"
        )
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
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(3)
        # 登録ボタンクリック
        kiyaku.click()
        addbutton.click()

        # 案件トップに遷移
        # 案件トップのログアウトボタンをクリック
        logout = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a")
        logout.click()
        time.sleep(5)

        # 会員登録
        touroku = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a[1]")
        touroku.click()
        # 無料会員選択
        freeuser = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/section[1]/div[3]/a")
        freeuser.click()

time.sleep(5)

# クロームの終了処理
driver.close()
