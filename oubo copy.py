import csv
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# ユーザーごとに3件の応募を登録
MAXCOUNT = 3

# クロームの立ち上げ
driver = webdriver.Chrome()

# ログインページ接続
driver.get("https://experience.dev-salon.com/login/")
loginUser = driver.find_element(By.XPATH, '//*[@id="username-6"]')
loginPass = driver.find_element(By.XPATH, '//*[@id="user_password-6"]')
loginBtn = driver.find_element(By.XPATH, '//*[@id="um-submit-btn"]')
loginUser.send_keys("paiduser01")
loginPass.send_keys("Test1111")
loginBtn.click()

# 案件トップページの新着案件から案件をさがす
csv_ankenNm = "おまかせください２"
matching_element = driver.find_element(By.LINK_TEXT, (csv_ankenNm))
# 案件の位置までスクロール
driver.execute_script("arguments[0].scrollIntoView();", matching_element)
time.sleep(1)
# 案件をクリック
matching_element.click()

#応募するをクリック
ouboBtn=driver.find_element(By.XPATH,('//*[@id="work_view_apply"]'))
ouboBtn.click()

 
lineCnt = 0
filecsv_userProf = "oubo.csv"
with open(filecsv_userProf, encoding="utf-8-sig", newline="") as f:
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

        if lineCnt == 0:
            # ログイン


        # 案件登録ボタンをクリック
        ankenBtn = driver.find_element(By.XPATH, '//*[@id="menu-item-210"]/a')
        ankenBtn.click()
        time.sleep(2)

        category1 = driver.find_element(By.CSS_SELECTOR, "#work_edit_category_main")
        select = Select(category1)
        select.select_by_index(int(csv_cate1))
        time.sleep(2)
        category2 = driver.find_element(By.CSS_SELECTOR, "#work_edit_category_sub")
        select = Select(category2)
        select.select_by_index(int(csv_cate2))
        time.sleep(2)
        matchType = driver.find_element(By.CSS_SELECTOR, "#work_edit_type")
        select = Select(matchType)
        select.select_by_index(int(csv_type))
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
        tempFile1.send_keys(csv_file1)
        tempFile2.send_keys(csv_file2)
        time.sleep(10)

        # スクロール
        driver.find_element(By.TAG_NAME, "body").click()
        for i in range(5):
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)

        # 内容確認に進むクリック
        button1 = driver.find_element(By.XPATH, '//*[@id="work_edit_next"]')
        button1.click()
        time.sleep(2)
        # 利用規約に同意して公開する
        button2 = driver.find_element(By.XPATH, '//*[@id="work_confirm_submit"]')
        button2.click()
        time.sleep(2)

        lineCnt += 1

        # ユーザー案件がMAXになったらログアウト後再ログイン
        if lineCnt == MAXCOUNT:
            logoutBtn = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a")
            logoutBtn.click()

            loginBtn = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a[2]")
            loginBtn.click()
            lineCnt = 0

