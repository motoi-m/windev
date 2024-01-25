import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import subtask
import utilize

# クロームの立ち上げ
driver = webdriver.Chrome()
# ActionChainsをインスタンス化
action = webdriver.ActionChains(driver)

# 接続
driver.get(utilize.siteUrl())

filecsv = "csv/torihiki.csv"
with open(filecsv, encoding="utf-8-sig", newline="") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        csv_orderNm = row[0]  # 発注者
        csv_contractorNm = row[1]  # 受注者
        csv_pass = row[2]  # pass
        csv_title = row[3]  # タイトル
        csv_status = row[4]  # ステータス
        csv_stUser = row[5]  # コメント開始User
        csv_comment1 = row[6]  # coment1
        csv_comment2 = row[7]
        csv_comment3 = row[8]
        csv_comment4 = row[9]
        csv_comment5 = row[10]
        csv_comment6 = row[11]
        csv_comment7 = row[12]
        csv_comment8 = row[13]
        csv_comment9 = row[14]
        csv_comment10 = row[15]
        csv_comment11 = row[16]
        csv_reviewH = row[17]  # 発注者のレビュー
        csv_starH = row[18]  # 発注者の評価
        csv_reviewJ = row[19]  # 受注者のレビュー
        csv_starJ = row[20]  # 受注者の評価

        nextUser = csv_stUser

        # コメント
        comments = [
            csv_comment1,
            csv_comment2,
            csv_comment3,
            csv_comment4,
            csv_comment5,
            csv_comment6,
            csv_comment7,
            csv_comment8,
            csv_comment9,
            csv_comment10,
            csv_comment11,
        ]
        for str in comments:
            if str != "-":
                subtask.loginToKeiyaku(driver, nextUser, csv_pass, csv_title)
                time.sleep(2)
                # メッセージボックスの要素
                msgBox = driver.find_element(By.XPATH, '//*[@id="add_work_comment"]')
                # 送信ボタンの要素
                msgButton = driver.find_element(By.XPATH, '//*[@id="add_work_comment_container"]/div[1]/button')

                msgBox.send_keys(str)
                msgButton.click()
                time.sleep(1)

                # logout
                logoutBtn = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a")
                logoutBtn.click()

                # コメント開始が発注者なら次のログインは受注者
                if nextUser == csv_orderNm:
                    nextUser = csv_contractorNm
                else:
                    nextUser = csv_orderNm
            else:
                break

        if csv_status != "作業中":
            # 受注者で再ログイン
            subtask.loginToKeiyaku(driver, csv_contractorNm, csv_pass, csv_title)
            time.sleep(2)

            # この内容で契約ボタンをクリック
            keiyakuButton = driver.find_element(By.XPATH, '//*[@id="contract_view_button_check"]')
            keiyakuButton.click()
            time.sleep(2)
            alert = driver.switch_to.alert
            alert.accept()
            time.sleep(1)
            # logout
            logoutBtn = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a")
            logoutBtn.click()

            if csv_status == "検収完了":
                # 発注者で再ログイン
                subtask.loginToKeiyaku(driver, csv_orderNm, csv_pass, csv_title)
                time.sleep(2)
                # 合意して終了ボタンをクリック
                endButton = driver.find_element(By.XPATH, '//*[@id="contract_view_button_finish"]')
                endButton.click()
                alert = driver.switch_to.alert
                alert.accept()
                time.sleep(1)
                # 発注者のレビュー入力
                subtask.review(driver, csv_reviewH, csv_starH)
                time.sleep(2)

                # logout
                logoutBtn = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a")
                logoutBtn.click()

                # 受注者で再ログイン
                subtask.loginToKeiyaku(driver, csv_contractorNm, csv_pass, "")
                time.sleep(1)

                strReview = csv_title + "のユーザーレビュー"
                matching_element = driver.find_element(By.LINK_TEXT, (strReview))  # 案件名
                # レビューの位置までスクロール
                driver.execute_script("arguments[0].scrollIntoView();", matching_element)
                time.sleep(1)
                # レビューをクリック
                matching_element.click()
                strReview = "案件『" + csv_title + "』のユーザーレビューを書きましょう"
                matching_element = driver.find_element(By.LINK_TEXT, (strReview))
                # レビューの位置までスクロール
                driver.execute_script("arguments[0].scrollIntoView();", matching_element)
                time.sleep(1)
                # レビューをクリック
                matching_element.click()
                # 受注者のレビュー入力
                subtask.review(driver, csv_reviewJ, csv_starJ)
                time.sleep(3)
                # logout
                logoutBtn = driver.find_element(By.XPATH, "/html/body/header/div/div/div[3]/div/a")
                logoutBtn.click()
