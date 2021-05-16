from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.bara_text_config import BaraText
from .fc2 import Fc2
import datetime


class Bara(Fc2):
    def login_id(self):
        return LOGIN.BARA_LOGIN['ID']

    def login_pass(self):
        return LOGIN.BARA_LOGIN['PASS']
    
    def return_will_hour(self,zone):
        return self.will_hour

    def return_will_minute(self,zone):
        return self.will_minute

    def get_main_result(self,zone):
        if zone == "前場":
            if CONFIG.bara_main(zone) == "勝ち":
                self.before_main_total+= int(CONFIG.nikkei_result(zone))
                self.before_main_total = "+" + str(self.before_main_total) if self.before_main_total > 0 else "±" + str(self.before_main_total) if self.before_main_total == 0 else str(self.before_main_total)
                return "+" + CONFIG.nikkei_result(zone)
            if CONFIG.bara_main(zone) == "負け":
                self.before_main_total-= int(CONFIG.nikkei_result(zone))
                self.before_main_total = "+" + str(self.before_main_total) if self.before_main_total > 0 else "±" + str(self.before_main_total) if self.before_main_total == 0 else str(self.before_main_total)
                return "-" + CONFIG.nikkei_result(zone)
            if CONFIG.bara_main(zone) == "引き分け":
                self.before_main_total+= int(CONFIG.nikkei_result(zone))
                self.before_main_total = "+" + str(self.before_main_total) if self.before_main_total > 0 else "±" + str(self.before_main_total) if self.before_main_total == 0 else str(self.before_main_total)
                return "±" + CONFIG.nikkei_result(zone)
        if zone == "後場":
            if CONFIG.bara_main(zone) == "勝ち":
                self.after_main_total+= int(CONFIG.nikkei_result(zone))
                self.after_main_total = "+" + str(self.after_main_total) if self.after_main_total > 0 else "±" + str(self.after_main_total) if self.after_main_total == 0 else str(self.after_main_total)
                return "+" + CONFIG.nikkei_result(zone)
            if CONFIG.bara_main(zone) == "負け":
                self.after_main_total-= int(CONFIG.nikkei_result(zone))
                self.after_main_total = "+" + str(self.after_main_total) if self.after_main_total > 0 else "±" + str(self.after_main_total) if self.after_main_total == 0 else str(self.after_main_total)
                return "-" + CONFIG.nikkei_result(zone)
            if CONFIG.bara_main(zone) == "引き分け":
                self.after_main_total+= int(CONFIG.nikkei_result(zone))
                self.after_main_total = "+" + str(self.after_main_total) if self.after_main_total > 0 else "±" + str(self.after_main_total) if self.after_main_total == 0 else str(self.after_main_total)
                return "±" + CONFIG.nikkei_result(zone)
        if zone == "ナイトセッション":
            if CONFIG.bara_main(zone) == "勝ち":
                self.nightsession_main_total+= int(CONFIG.nikkei_result(zone))
                self.nightsession_main_total = "+" + str(self.nightsession_main_total) if self.nightsession_main_total > 0 else "±" + str(self.nightsession_main_total) if self.nightsession_main_total == 0 else str(self.nightsession_main_total)
                return "+" + CONFIG.nikkei_result(zone)
            if CONFIG.bara_main(zone) == "負け":
                self.nightsession_main_total-= int(CONFIG.nikkei_result(zone))
                self.nightsession_main_total = "+" + str(self.nightsession_main_total) if self.nightsession_main_total > 0 else "±" + str(self.nightsession_main_total) if self.nightsession_main_total == 0 else str(self.nightsession_main_total)
                return "-" + CONFIG.nikkei_result(zone)
            if CONFIG.bara_main(zone) == "引き分け":
                self.nightsession_main_total+= int(CONFIG.nikkei_result(zone))
                self.nightsession_main_total = "+" + str(self.nightsession_main_total) if self.nightsession_main_total > 0 else "±" + str(self.nightsession_main_total) if self.nightsession_main_total == 0 else str(self.nightsession_main_total)
                return "±" + CONFIG.nikkei_result(zone)
        if zone == "オーバーナイト2":
            if CONFIG.bara_main(zone) == "勝ち":
                self.overnight2_main_total+= int(CONFIG.nikkei_result(zone))
                self.overnight2_main_total = "+" + str(self.overnight2_main_total) if self.overnight2_main_total > 0 else "±" + str(self.overnight2_main_total) if self.overnight2_main_total == 0 else str(self.overnight2_main_total)
                return "+" + CONFIG.nikkei_result(zone)
            if CONFIG.bara_main(zone) == "負け":
                self.overnight2_main_total-= int(CONFIG.nikkei_result(zone))
                self.overnight2_main_total = "+" + str(self.overnight2_main_total) if self.overnight2_main_total > 0 else "±" + str(self.overnight2_main_total) if self.overnight2_main_total == 0 else str(self.overnight2_main_total)
                return "-" + CONFIG.nikkei_result(zone)
            if CONFIG.bara_main(zone) == "引き分け":
                self.overnight2_main_total+= int(CONFIG.nikkei_result(zone))
                self.overnight2_main_total = "+" + str(self.overnight2_main_total) if self.overnight2_main_total > 0 else "±" + str(self.overnight2_main_total) if self.overnight2_main_total == 0 else str(self.overnight2_main_total)
                return "±" + CONFIG.nikkei_result(zone)

    def get_total_file(self,zone):
        if zone == "前場":
            self.before_main_total = open('other_txt/bara/bara_before_main_total.txt', 'r').read()
            self.before_main_total = 0 if self.before_main_total == "±0" else int(self.before_main_total)
        if zone == "後場":
            self.after_main_total = open('other_txt/bara/bara_after_main_total.txt', 'r').read()
            self.after_main_total = 0 if self.after_main_total == "±0" else int(self.after_main_total)
        if zone == "ナイトセッション":
            self.nightsession_main_total = open('other_txt/bara/bara_nightsession_main_total.txt', 'r').read()
            self.nightsession_main_total = 0 if self.nightsession_main_total == "±0" else int(self.nightsession_main_total)
        if zone == "オーバーナイト2":
            self.overnight2_main_total = open('other_txt/bara/bara_overnight2_main_total.txt', 'r').read()
            self.overnight2_main_total = 0 if self.overnight2_main_total == "±0" else int(self.overnight2_main_total)


    def save_total_file(self,zone):
        if zone == "前場":
            open('other_txt/bara/bara_before_main_total.txt', 'w').write(str(self.before_main_total))
        if zone == "後場":
            open('other_txt/bara/bara_after_main_total.txt', 'w').write(str(self.after_main_total))
        if zone == "ナイトセッション":
            open('other_txt/bara/bara_nightsession_main_total.txt', 'w').write(str(self.nightsession_main_total))
        if zone == "オーバーナイト2":
            open('other_txt/bara/bara_overnight2_main_total.txt', 'w').write(str(self.overnight2_main_total))
            
    def __init__(self,driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()  
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.will_hour = "12"

        self.will_minute = "15"

        self.will_second = "00"
    
    def automation(self):
        print("薔薇の人生")
        print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
        self.login_fc2()
        zones = ["前場","後場","ナイトセッション","オーバーナイト2"]
        for zone in zones:
            self.get_total_file(zone)
        bara_text = BaraText(CONFIG.bara_main_buy_result(zones[0]),self.get_main_result(zones[0]),self.before_main_total,CONFIG.bara_main_buy_result(zones[1]),self.get_main_result(zones[1]),self.after_main_total,CONFIG.bara_main_buy_result(zones[2]),self.get_main_result(zones[2]),self.nightsession_main_total,CONFIG.bara_main_buy_result(zones[3]),self.get_main_result(zones[3]),self.overnight2_main_total)
        for zone in zones:
            self.blog_post(bara_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)
            