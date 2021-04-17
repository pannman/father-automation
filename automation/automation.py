from selenium import webdriver
import sys
import time
import datetime
import login_config as LOGIN
import text_config as TEXT
import all_config as CONFIG
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#関数一覧
def return_r_sub_total_file(zone):
    if zone == "日中":
        return r_day_sub_total
    if zone == "前場":
        return r_before_sub_total
    if zone == "後場":
        return r_after_sub_total

def return_r_main_total_file(zone):
    if zone == "日中":
        return r_day_main_total
    if zone == "前場":
        return r_before_main_total
    if zone == "後場":
        return r_after_main_total

def return_w_sub_total_file(zone):
    if zone == "日中":
        return w_day_sub_total
    if zone == "前場":
        return w_before_sub_total
    if zone == "後場":
        return w_after_sub_total

def return_w_main_total_file(zone):
    if zone == "日中":
        return w_day_main_total
    if zone == "前場":
        return w_before_main_total
    if zone == "後場":
        return w_after_main_total

def return_yes_hour(zone):
    if zone == "日中":
        return day_yes_hour
    if zone == "前場":
        return before_yes_hour
    if zone == "後場":
        return after_yes_hour

def return_yes_minute(zone):
    if zone == "日中":
        return day_yes_minute
    if zone == "前場":
        return before_yes_minute
    if zone == "後場":
        return after_yes_minute

def all_delete(ele):
    ele.send_keys(Keys.CONTROL,"a")
    ele.send_keys(Keys.DELETE)

# Chrome のオプションを設定する
options = webdriver.ChromeOptions()

# Selenium Server に接続する
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options,
)

wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
driver.set_window_size('1200', '1000')

#時間取得
yes_date = datetime.datetime.now() + datetime.timedelta(days = 1)
yes_year = str(yes_date.year)
yes_month = str(yes_date.month)
yes_day = str(yes_date.day)

day_yes_hour = "6"
before_yes_hour = "6"
after_yes_hour = "12"

day_yes_minute = "30"
before_yes_minute = "35"
after_yes_minute = "00"

yes_second = "00"

# 日中累計読み込み
r_day_main_total = open('day_main_total.txt', 'r').read()
r_day_sub_total = open('day_sub_total.txt', 'r').read()
w_day_main_total = open('day_main_total.txt', 'w')
w_day_sub_total = open('day_sub_total.txt', 'w')
# 前場累計読み込み
r_before_main_total = open('before_main_total.txt', 'r').read()
r_before_sub_total = open('before_sub_total.txt', 'r').read()
w_before_main_total = open('before_main_total.txt', 'w')
w_before_sub_total = open('before_sub_total.txt', 'w')
# 後場累計読み込み
r_after_main_total = open('after_main_total.txt', 'r').read()
r_after_sub_total = open('after_sub_total.txt', 'r').read()
w_after_main_total = open('after_main_total.txt', 'w')
w_after_sub_total = open('after_sub_total.txt', 'w')

# 時間配列に格納
zones = ['日中', '前場', '後場']

try:
    #fcsログイン
    driver.get('https://fc2.com/login.php?ref=blog')
    print(driver.current_url)
    mail = wait.until(EC.presence_of_element_located((By.ID, "id")))
    password = wait.until(EC.presence_of_element_located((By.ID, "pass")))
    login_btn = wait.until(EC.presence_of_element_located((By.NAME, "image")))
    mail.send_keys(LOGIN.FC2_LOGIN['ID'])
    password.send_keys(LOGIN.FC2_LOGIN['PASS'])
    login_btn.click()
    print(driver.current_url)

    #ブログ投稿
    for zone in zones:
        driver.get('https://admin.blog.fc2.com/control.php?mode=editor&process=new')
        print(driver.current_url)

        #タイトル
        title = wait.until(EC.presence_of_element_located((By.ID, "entry_title")))
        title.send_keys(TEXT.fc2_title(zone))

        #テキスト
        main_text = wait.until(EC.presence_of_element_located((By.ID, "body")))
        main_text.send_keys(TEXT.fc2_text(zone,CONFIG.sub_sign(zone),CONFIG.main_sign(zone),return_r_sub_total_file(zone),return_r_main_total_file(zone)))

        #予約ラジオボタン
        reserve_radio = wait.until(EC.presence_of_element_located((By.ID, "entry_property3"))).click()
        # reserve_radio = driver.find_element_by_id("entry_property3").send_keys(Keys.SPACE)

        #予約時間
        input_year = driver.find_element_by_name("entry[year]")
        input_month = driver.find_element_by_name("entry[month]")
        input_day = driver.find_element_by_name("entry[day]")
        input_hour = driver.find_element_by_name("entry[hour]")
        input_minute = driver.find_element_by_name("entry[minute]")
        input_second = driver.find_element_by_name("entry[second]")
        dates = [input_year, input_month, input_day, input_hour, input_minute, input_second]
        for date in dates:
            all_delete(date)
        input_year.send_keys(yes_year)
        input_month.send_keys(yes_month)
        input_day.send_keys(yes_day)
        input_hour.send_keys(return_yes_hour(zone))
        input_minute.send_keys(return_yes_minute(zone))
        input_second.send_keys(yes_second)
        
        # input_hour = driver.find_element_by_class_name("entry[hour]")
        buttun = driver.find_element_by_class_name("admin_common_positive_btn").click()
        time.sleep(2)

        # 累計読み込み
        return_w_sub_total_file(zone).write(str(int(return_r_sub_total_file(zone)) - int(CONFIG.sub_sign(zone))))
        return_w_main_total_file(zone).write(str(int(return_r_main_total_file(zone)) - int(CONFIG.main_sign(zone))))

        print(TEXT.fc2_text(zone,CONFIG.sub_sign(zone),CONFIG.main_sign(zone),return_r_sub_total_file(zone),return_r_main_total_file(zone)))

except Exception as e:
    print(e)

    # 日中累計書き込み
    w_day_sub_total.write(r_day_sub_total)
    w_day_main_total.write(r_day_main_total)
    # 前場累計書き込み
    w_before_sub_total.write(r_before_sub_total)
    w_before_main_total.write(r_before_main_total)
    # 後場累計書き込み
    w_after_sub_total.write(r_after_sub_total)
    w_after_main_total.write(r_after_main_total)

    driver.quit()
finally:
    driver.quit()
