from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.habatake_text_config import HabatakeText
from .fc2 import Fc2
import datetime


class Habatake(Fc2):
    def login_id(self):
        return LOGIN.HABATAKE_LOGIN['ID']

    def login_pass(self):
        return LOGIN.HABATAKE_LOGIN['PASS']

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

    def get_main_result(self,zone):
        if CONFIG.habatake_main(zone) == "勝ち":
            self.main_total+= int(CONFIG.nikkei_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "+" + CONFIG.nikkei_result(zone)
        if CONFIG.habatake_main(zone) == "負け":
            self.main_total-= int(CONFIG.nikkei_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "-" + CONFIG.nikkei_result(zone)
        if CONFIG.habatake_main(zone) == "引き分け":
            self.main_total+= int(CONFIG.nikkei_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "±" + CONFIG.nikkei_result(zone)

    def get_total_file(self,zone):
        if zone == "日中":
            self.main_total = open('other_txt/habatake/habatake_day_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "前場":
            self.main_total = open('other_txt/habatake/habatake_before_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "後場":
            self.main_total = open('other_txt/habatake/habatake_after_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "ナイトセッション":
            self.main_total = open('other_txt/habatake/habatake_nightsession_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "オーバーナイト1":
            self.main_total = open('other_txt/habatake/habatake_overnight1_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "オーバーナイト2":
            self.main_total = open('other_txt/habatake/habatake_overnight2_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)

    def save_total_file(self,zone):
        if zone == "日中":
            open('other_txt/habatake/habatake_day_main_total.txt', 'w').write(str(self.main_total))
        if zone == "前場":
            open('other_txt/habatake/habatake_before_main_total.txt', 'w').write(str(self.main_total))
        if zone == "後場":
            open('other_txt/habatake/habatake_after_main_total.txt', 'w').write(str(self.main_total))
        if zone == "ナイトセッション":
            open('other_txt/habatake/habatake_nightsession_main_total.txt', 'w').write(str(self.main_total))
        if zone == "オーバーナイト1":
            open('other_txt/habatake/habatake_overnight1_main_total.txt', 'w').write(str(self.main_total))
        if zone == "オーバーナイト2":
            open('other_txt/habatake/habatake_overnight2_main_total.txt', 'w').write(str(self.main_total))
            
    def __init__(self,driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()  
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.day_will_hour = "8"
        self.before_will_hour = "8"
        self.after_will_hour = "11"
        self.nightsession_will_hour = "16"
        self.overnight1_will_hour = "16"
        self.overnight2_will_hour = "22"

        self.day_will_minute = "15"
        self.before_will_minute = "20"
        self.after_will_minute = "55"
        self.nightsession_will_minute = "10"
        self.overnight1_will_minute = "20"
        self.overnight2_will_minute = "15"

        self.will_second = "00"
    
    def automation(self,num):
        print("はばたけ未来へ")
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zones = ["日中","前場","後場"]
            for zone in zones:
                print(zone)
                self.get_category_num(zone)
                self.get_total_file(zone)
                habatake_text = HabatakeText(zone,CONFIG.habatake_main_buy_result(zone),self.get_main_result(zone),self.main_total)
                self.blog_post(self.category_num,habatake_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
                self.save_total_file(zone)

        if num == 5:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "ナイトセッション"
            print(zone)
            self.get_category_num(zone)
            self.get_total_file(zone)
            habatake_text = HabatakeText(zone,CONFIG.habatake_main_buy_result(zone),self.get_main_result(zone),self.main_total)
            self.blog_post(self.category_num,habatake_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)
        if num == 9:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zones = ["オーバーナイト1","オーバーナイト2"]
            for zone in zones:
                print(zone)
                self.get_category_num(zone)
                self.get_total_file(zone)
                habatake_text = HabatakeText(zone,CONFIG.habatake_main_buy_result(zone),self.get_main_result(zone),self.main_total)
                self.blog_post(self.category_num,habatake_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
                self.save_total_file(zone)