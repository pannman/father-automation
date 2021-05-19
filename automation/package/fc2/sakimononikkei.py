from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.sakimononikkei_text_config import SakimononikkeiText
from .fc2 import Fc2
import datetime


class Sakimononikkei(Fc2):
    def login_id(self):
        if self.zone == "ナイトセッション":
            return LOGIN.NIGHTSESSION_LOGIN['ID']
        elif self.zone == "オーバーナイト1" or self.zone == "オーバーナイト2":
            return LOGIN.OVERNIGHT1_LOGIN['ID']
        else:
            return LOGIN.SAKIMONONIKKEI_LOGIN['ID']

    def login_pass(self):
        if self.zone == "ナイトセッション":
            return LOGIN.NIGHTSESSION_LOGIN['PASS']
        elif self.zone == "オーバーナイト1":
            return LOGIN.OVERNIGHT1_LOGIN['PASS']
        else:
            return LOGIN.SAKIMONONIKKEI_LOGIN['PASS']
    
    def get_category_num(self,zone):
        if zone == "日中":
            self.category_num = 0
        if zone == "前場":
            self.category_num = 0
        if zone == "後場":
            self.category_num = 0
        if zone == "ナイトセッション":
            self.category_num = 0
        if zone == "オーバーナイト1":
            self.category_num = 0
        if zone == "オーバーナイト2":
            self.category_num = 0
    
    def return_will_hour(self,zone):
        if zone == "日中":
            return self.day_will_hour
        if zone == "前場":
            return self.before_will_hour
        if zone == "後場":
            return self.after_will_hour
        if zone == "ナイトセッション":
            return self.nightsession_will_hour
        if zone == "オーバーナイト1":
            return self.overnight1_will_hour
        if zone == "オーバーナイト2":
            return self.overnight2_will_hour
    
    def return_will_minute(self,zone):
        if zone == "日中":
            return self.day_will_minute
        if zone == "前場":
            return self.before_will_minute
        if zone == "後場":
            return self.after_will_minute
        if zone == "ナイトセッション":
            return self.nightsession_will_minute
        if zone == "オーバーナイト1":
            return self.overnight1_will_minute
        if zone == "オーバーナイト2":
            return self.overnight2_will_minute
    
    def get_sub_result(self,zone):
        if CONFIG.sakimononikkei_sub(zone) == "勝ち":
            self.sub_total+= int(CONFIG.nikkei_mini_result(zone))
            self.sub_total = "+" + str(self.sub_total) if self.sub_total > 0 else "±" + str(self.sub_total) if self.sub_total == 0 else str(self.sub_total)
            return "+" + CONFIG.nikkei_mini_result(zone)
        if CONFIG.sakimononikkei_sub(zone) == "負け":
            self.sub_total-= int(CONFIG.nikkei_mini_result(zone))
            self.sub_total = "+" + str(self.sub_total) if self.sub_total > 0 else "±" + str(self.sub_total) if self.sub_total == 0 else str(self.sub_total)
            return "-" + CONFIG.nikkei_mini_result(zone)
        if CONFIG.sakimononikkei_sub(zone) == "引き分け":
            self.sub_total+= int(CONFIG.nikkei_mini_result(zone))
            self.sub_total = "+" + str(self.sub_total) if self.sub_total > 0 else "±" + str(self.sub_total) if self.sub_total == 0 else str(self.sub_total)
            return "±" + CONFIG.nikkei_mini_result(zone)

    def get_main_result(self,zone):
        if CONFIG.sakimononikkei_main(zone) == "勝ち":
            self.main_total+= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "+" + CONFIG.nikkei_mini_result(zone)
        if CONFIG.sakimononikkei_main(zone) == "負け":
            self.main_total-= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "-" + CONFIG.nikkei_mini_result(zone)
        if CONFIG.sakimononikkei_main(zone) == "引き分け":
            self.main_total+= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "±" + CONFIG.nikkei_mini_result(zone)

    def get_main_total_file(self,zone):
        if zone == "日中":
            self.main_total = open('other_txt/sakimononikkei/sakimononikkei_day_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "前場":
            self.main_total = open('other_txt/sakimononikkei/sakimononikkei_before_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "後場":
            self.main_total = open('other_txt/sakimononikkei/sakimononikkei_after_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "ナイトセッション":
            self.main_total = open('other_txt/sakimononikkei/sakimononikkei_nightsession_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "オーバーナイト1":
            self.main_total = open('other_txt/sakimononikkei/sakimononikkei_overnight1_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "オーバーナイト2":
            self.main_total = open('other_txt/sakimononikkei/sakimononikkei_overnight2_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)

    def get_sub_total_file(self,zone):
        if zone == "日中":
            self.sub_total = open('other_txt/sakimononikkei/sakimononikkei_day_sub_total.txt', 'r').read()
            self.sub_total = 0 if self.sub_total == "±0" else int(self.sub_total)
        if zone == "前場":
            self.sub_total = open('other_txt/sakimononikkei/sakimononikkei_before_sub_total.txt', 'r').read()
            self.sub_total = 0 if self.sub_total == "±0" else int(self.sub_total)
        if zone == "後場":
            self.sub_total = open('other_txt/sakimononikkei/sakimononikkei_after_sub_total.txt', 'r').read()
            self.sub_total = 0 if self.sub_total == "±0" else int(self.sub_total)
        if zone == "ナイトセッション":
            self.sub_total = open('other_txt/sakimononikkei/sakimononikkei_nightsession_sub_total.txt', 'r').read()
            self.sub_total = 0 if self.sub_total == "±0" else int(self.sub_total)
        if zone == "オーバーナイト1":
            self.sub_total = open('other_txt/sakimononikkei/sakimononikkei_overnight1_sub_total.txt', 'r').read()
            self.sub_total = 0 if self.sub_total == "±0" else int(self.sub_total)
        if zone == "オーバーナイト2":
            self.sub_total = open('other_txt/sakimononikkei/sakimononikkei_overnight2_sub_total.txt', 'r').read()
            self.sub_total = 0 if self.sub_total == "±0" else int(self.sub_total)
    
    def save_main_total_file(self,zone):
        if zone == "日中":
            open('other_txt/sakimononikkei/sakimononikkei_day_main_total.txt', 'w').write(str(self.main_total))
        if zone == "前場":
            open('other_txt/sakimononikkei/sakimononikkei_before_main_total.txt', 'w').write(str(self.main_total))
        if zone == "後場":
            open('other_txt/sakimononikkei/sakimononikkei_after_main_total.txt', 'w').write(str(self.main_total))
        if zone == "ナイトセッション":
            open('other_txt/sakimononikkei/sakimononikkei_nightsession_main_total.txt', 'w').write(str(self.main_total))
        if zone == "オーバーナイト1":
            open('other_txt/sakimononikkei/sakimononikkei_overnight1_main_total.txt', 'w').write(str(self.main_total))
        if zone == "オーバーナイト2":
            open('other_txt/sakimononikkei/sakimononikkei_overnight2_main_total.txt', 'w').write(str(self.main_total))
    def save_sub_total_file(self,zone):
        if zone == "日中":
            open('other_txt/sakimononikkei/sakimononikkei_day_sub_total.txt', 'w').write(str(self.sub_total))
        if zone == "前場":
            open('other_txt/sakimononikkei/sakimononikkei_before_sub_total.txt', 'w').write(str(self.sub_total))
        if zone == "後場":
            open('other_txt/sakimononikkei/sakimononikkei_after_sub_total.txt', 'w').write(str(self.sub_total))
        if zone == "ナイトセッション":
            open('other_txt/sakimononikkei/sakimononikkei_nightsession_sub_total.txt', 'w').write(str(self.sub_total))
        if zone == "オーバーナイト1":
            open('other_txt/sakimononikkei/sakimononikkei_overnight1_sub_total.txt', 'w').write(str(self.sub_total))
        if zone == "オーバーナイト2":
            open('other_txt/sakimononikkei/sakimononikkei_overnight2_sub_total.txt', 'w').write(str(self.sub_total))

    def __init__(self,driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()  
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.day_will_hour = "6"
        self.before_will_hour = "6"
        self.after_will_hour = "12"
        self.nightsession_will_hour = "12"
        self.overnight1_will_hour = "15"
        self.overnight2_will_hour = "22"

        self.day_will_minute = "30"
        self.before_will_minute = "35"
        self.after_will_minute = "00"
        self.nightsession_will_minute = "12"
        self.overnight1_will_minute = "55"
        self.overnight2_will_minute = "55"

        self.will_second = "00"
    
    def automation(self,num):
        print("日経225ミニ先物ブログ")
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.zone = ""
            self.login_fc2()
            zones = ["日中","前場","後場"]
            for zone in zones:
                print(zone)
                self.get_category_num(zone)
                self.get_main_total_file(zone)
                self.get_sub_total_file(zone)
                sakimononikkei_text = SakimononikkeiText(zone,CONFIG.sakimononikkei_sub_buy_result(zone),self.get_sub_result(zone),self.get_main_result(zone),self.sub_total,self.main_total)
                self.blog_post(self.category_num,sakimononikkei_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
                self.save_main_total_file(zone)
                self.save_sub_total_file(zone)
        if num == 5:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.zone = "ナイトセッション"
            self.login_fc2()
            print(self.zone)
            self.get_category_num(self.zone)
            self.get_main_total_file(self.zone)
            self.get_sub_total_file(self.zone)
            sakimononikkei_text = SakimononikkeiText(self.zone,CONFIG.sakimononikkei_sub_buy_result(self.zone),self.get_sub_result(self.zone),self.get_main_result(self.zone),self.sub_total,self.main_total)
            self.blog_post(self.category_num,sakimononikkei_text,self.zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_main_total_file(self.zone)
            self.save_sub_total_file(self.zone)
        if num == 9:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.zone = "オーバーナイト1"
            self.login_fc2()
            zones = ["オーバーナイト1","オーバーナイト2"]
            for zone in zones:
                print(zone)
                self.get_category_num(zone)
                self.get_main_total_file(zone)
                self.get_sub_total_file(zone)
                sakimononikkei_text = SakimononikkeiText(zone,CONFIG.sakimononikkei_sub_buy_result(zone),self.get_sub_result(zone),self.get_main_result(zone),self.sub_total,self.main_total)
                self.blog_post(self.category_num,sakimononikkei_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
                self.save_main_total_file(zone)
                self.save_sub_total_file(zone)
