from ..config import login_config as LOGIN
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def all_delete(ele):
    ele.send_keys(Keys.CONTROL,"a")
    ele.send_keys(Keys.DELETE)

class Fc2:

    def __init__(self,driver):
        self.driver = driver

    #fc2ログイン
    def login_fc2(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get(LOGIN.FC2_URL['LOGIN'])
        mail = wait.until(EC.presence_of_element_located((By.ID, "id")))
        password = wait.until(EC.presence_of_element_located((By.ID, "pass")))
        login_btn = wait.until(EC.presence_of_element_located((By.NAME, "image")))
        mail.send_keys(self.login_id())
        password.send_keys(self.login_pass())
        login_btn.click()

    #ブログ投稿
    def blog_post(self,blog_name,zone,will_year,will_month,will_day,will_second):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get(LOGIN.FC2_URL['BLOG'])

        if len(self.driver.find_elements_by_id('change_normal_link')) > 0:
            self.driver.execute_script("switchmenu('menu_simple_normal','not');switch_sipmle_normal();return false;")

        # #タイトル
        title = wait.until(EC.presence_of_element_located((By.ID, "entry_title")))
        title.send_keys(blog_name.blog_title())
        # #テキスト
        main_text = wait.until(EC.presence_of_element_located((By.ID, "body")))
        main_text.send_keys(blog_name.blog_text())

        self.driver.maximize_window()

        
        # #予約ラジオボタン
        reserve_radio = wait.until(EC.presence_of_element_located((By.ID, "entry_property3"))).click()
        # #予約時間
        input_year = self.driver.find_element_by_name("entry[year]")
        input_month = self.driver.find_element_by_name("entry[month]")
        input_day = self.driver.find_element_by_name("entry[day]")
        input_hour = self.driver.find_element_by_name("entry[hour]")
        input_minute = self.driver.find_element_by_name("entry[minute]")
        input_second = self.driver.find_element_by_name("entry[second]")
        dates = [input_year, input_month, input_day, input_hour, input_minute, input_second]
        for date in dates:
            all_delete(date)
        input_year.send_keys(will_year)
        input_month.send_keys(will_month)
        input_day.send_keys(will_day)
        input_hour.send_keys(self.return_will_hour(zone))
        input_minute.send_keys(self.return_will_minute(zone))
        input_second.send_keys(will_second)
        
        buttun = self.driver.find_element_by_class_name("admin_common_positive_btn").click()
        time.sleep(2)
