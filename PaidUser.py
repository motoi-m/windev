import csv
import time

from selenium import webdriver

# from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.support.wait import WebDriverWait

# クロームの立ち上げ
driver = webdriver.Chrome()

# ページ接続
driver.get("https://experience.dev-salon.com/")
# 会員登録
touroku = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a[1]")
touroku.click()
# 有料会員選択
freeuser = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/section[2]/div[4]/a")
freeuser.click()

filecsv = "csv/paiduser.csv"
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
        csv_atena = row[12]
        csv_cardNm = row[13]
        csv_cardNO = "4242424242424242"
        csv_ymd = row[14]
        csv_seqNo = row[15]

        # 新規登録ページの要素
        userNm = driver.find_element(By.XPATH, '//*[@id="user_login-536"]')
        userPass = driver.find_element(By.XPATH, '//*[@id="user_password-536"]')
        userPass2 = driver.find_element(By.XPATH, '//*[@id="confirm_user_password-536"]')
        mailAddress = driver.find_element(By.XPATH, '//*[@id="user_email-536"]')
        houjinNm = driver.find_element(By.XPATH, '//*[@id="shop_name-536"]')
        houjinNo = driver.find_element(By.XPATH, '//*[@id="corporate_number-536"]')
        busyo = driver.find_element(By.XPATH, '//*[@id="department-536"]')
        yakusyoku = driver.find_element(By.XPATH, '//*[@id="job_title-536"]')
        tantouSei = driver.find_element(By.XPATH, '//*[@id="last_name-536"]')
        tantouMei = driver.find_element(By.XPATH, '//*[@id="first_name-536"]')
        Address = driver.find_element(By.XPATH, '//*[@id="address-536"]')
        tel = driver.find_element(By.XPATH, '//*[@id="mobile_number-536"]')
        atena = driver.find_element(By.XPATH, '//*[@id="invoice_title-536"]')
        addbutton = driver.find_element(By.XPATH, '//*[@id="um-submit-btn"]')
        kiyaku = driver.find_element(
            By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/div[2]/div/form/div[2]/div[2]/label/span[1]/i"
        )

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
        atena.send_keys(csv_atena)
        # スクロール
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(3)
        kiyaku.click()
        # 登録ボタンクリック
        addbutton.click()

        time.sleep(3)
        # 決済画面に遷移
        cardNm = driver.find_element(By.XPATH, '//*[@id="wpfs-card-holder-name--MzQ4MDB"]')
        cardNm.send_keys(csv_cardNm)

        # カード情報のiframeにスイッチ
        # iflame = driver.find_element(By.XPATH, '//*[@id="cardnumber--ZWYyZTc"]/div/iframe')
        # driver.switch_to.frame(iflame)
        # cardNo = driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input')
        iflame = driver.find_element(By.XPATH, '//*[@id="cardnumber--MzQ4MDB"]/div/iframe')
        driver.switch_to.frame(iflame)
        cardNo = driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[1]/span[2]/div/div[2]/span/input')
        ymd = driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[2]/span[1]')
        seqNo = driver.find_element(By.XPATH, '//*[@id="root"]/form/div/div[2]/span[2]/span[2]')
        # カード情報をセット
        cardNo.send_keys("42424242424242421231229")
        """
        cardNo.send_keys(Keys.RIGHT)
        cardNo.send_keys("1224")
        cardNo.send_keys(Keys.RIGHT)
        cardNo.send_keys("123")
        # seqNo.send_keys(csv_seqNo)
        """
        # 元に戻す
        driver.switch_to.default_content()
        # 決済登録
        payment = driver.find_element(By.XPATH, '//*[@id="submit--MzQ4MDB"]')
        payment.click()
        time.sleep(8)

        # 決済完了画面に遷移:マイページへボタンクリック←案件トップへ
        mypage = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/div[3]/div/a")
        mypage.click()

        logout = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a")
        logout.click()
        time.sleep(5)

        # 会員登録
        touroku = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a[1]")
        touroku.click()
        # 有料会員選択
        freeuser = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/section[2]/div[4]/a")
        freeuser.click()

time.sleep(5)
# 画面キャプチャを取得
# driver.save_screenshot("次へ進む実行後の画面.png")


time.sleep(5)

# クロームの終了処理
driver.close()
