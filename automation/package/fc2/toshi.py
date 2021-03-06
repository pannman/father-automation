from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.toshi_text_config import ToshiText
from .fc2 import Fc2
import datetime


class Toshi(Fc2):
    def login_id(self):
        return LOGIN.TOSHI_LOGIN['ID']

    def login_pass(self):
        return LOGIN.TOSHI_LOGIN['PASS']
    
    def get_category_num(self,zone):
        if zone == "日中":
            self.category_num = 1
        if zone == "前場":
            self.category_num = 1
        if zone == "後場":
            self.category_num = 1
        if zone == "ナイトセッション":
            self.category_num = 1
        if zone == "オーバーナイト2":
            self.category_num = 1
    
    def return_will_hour(self,zone):
        if zone == "日中":
            return self.day_will_hour
        if zone == "前場":
            return self.before_will_hour
        if zone == "後場":
            return self.after_will_hour
        if zone == "ナイトセッション":
            return self.nightsession_will_hour
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
        if zone == "オーバーナイト2":
            return self.overnight2_will_minute

    def get_main_result(self,zone):
        if CONFIG.toshi_main(zone) == "勝ち":
            self.main_total+= int(CONFIG.nikkei_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "+" + CONFIG.nikkei_result(zone)
        if CONFIG.toshi_main(zone) == "負け":
            self.main_total-= int(CONFIG.nikkei_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "-" + CONFIG.nikkei_result(zone)
        if CONFIG.toshi_main(zone) == "引き分け":
            self.main_total+= int(CONFIG.nikkei_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "±" + CONFIG.nikkei_result(zone)

    def get_total_file(self,zone):
        if zone == "日中":
            self.main_total = open('other_txt/toshi/toshi_day_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "前場":
            self.main_total = open('other_txt/toshi/toshi_before_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "後場":
            self.main_total = open('other_txt/toshi/toshi_after_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "ナイトセッション":
            self.main_total = open('other_txt/toshi/toshi_nightsession_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "オーバーナイト2":
            self.main_total = open('other_txt/toshi/toshi_overnight2_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)

    def save_total_file(self,zone):
        if zone == "日中":
            open('other_txt/toshi/toshi_day_main_total.txt', 'w').write(str(self.main_total))
        if zone == "前場":
            open('other_txt/toshi/toshi_before_main_total.txt', 'w').write(str(self.main_total))
        if zone == "後場":
            open('other_txt/toshi/toshi_after_main_total.txt', 'w').write(str(self.main_total))
        if zone == "ナイトセッション":
            open('other_txt/toshi/toshi_nightsession_main_total.txt', 'w').write(str(self.main_total))
        if zone == "オーバーナイト2":
            open('other_txt/toshi/toshi_overnight2_main_total.txt', 'w').write(str(self.main_total))
            
    def __init__(self,driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()  
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.day_will_hour = "7"
        self.before_will_hour = "7"
        self.after_will_hour = "12"
        self.nightsession_will_hour = "16"
        self.overnight2_will_hour = "23"

        self.day_will_minute = "00"
        self.before_will_minute = "05"
        self.after_will_minute = "00"
        self.nightsession_will_minute = "05"
        self.overnight2_will_minute = "00"

        self.will_second = "00"
    
    def automation(self,num):
        print("投資日記")
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zones = ["日中","前場","後場"]
            for zone in zones:
                print(zone)
                self.get_category_num(zone)
                self.get_total_file(zone)
                toshi_text = ToshiText(zone,CONFIG.toshi_main_buy_result(zone),self.get_main_result(zone),self.main_total)
                self.blog_post(self.category_num,toshi_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
                self.save_total_file(zone)

        if num == 5:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "ナイトセッション"
            print(zone)
            self.get_category_num(zone)
            self.get_total_file(zone)
            toshi_text = ToshiText(zone,CONFIG.toshi_main_buy_result(zone),self.get_main_result(zone),self.main_total)
            self.blog_post(self.category_num,toshi_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)
        if num == 9:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "オーバーナイト2"
            print(zone)
            self.get_category_num(zone)
            self.get_total_file(zone)
            toshi_text = ToshiText(zone,CONFIG.toshi_main_buy_result(zone),self.get_main_result(zone),self.main_total)
            self.blog_post(self.category_num,toshi_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)