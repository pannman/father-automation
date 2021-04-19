from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text import sakimononikkei_text_config as TEXT
from .fc2 import Fc2

class Sakimononikkei(Fc2):
    def login_id(self):
        return LOGIN.SAKIMONONIKKEI_LOGIN['ID']

    def login_pass(self):
        return LOGIN.SAKIMONONIKKEI_LOGIN['PASS']
    
    def get_titile(self,zone):
        return TEXT.sakimononikkei_title(zone)
    
    def get_text(self,zone,buy,sub_sign,main_sign,sub_total,main_total):
        return TEXT.sakimononikkei_text(zone,buy,sub_sign,main_sign,sub_total,main_total)
    
    def return_will_hour(self,zone):
        if zone == "日中":
            return self.day_will_hour
        if zone == "前場":
            return self.before_will_hour
        if zone == "後場":
            return self.after_will_hour
    
    def return_will_minute(self,zone):
        if zone == "日中":
            return self.day_will_minute
        if zone == "前場":
            return self.before_will_minute
        if zone == "後場":
            return self.after_will_minute
    
    def get_sub_result(self,zone):
        if zone == "日中":
            if CONFIG.sakimononikkei_sub(zone) == "勝ち":
                self.sub_total+= int(CONFIG.nikkei_mini_result(zone))
                self.sub_total = "+" + str(self.sub_total) if self.sub_total > 0 else "±" + str(self.sub_total) if self.sub_total == 0 else str(self.sub_total)
                return "+" + CONFIG.nikkei_mini_result(zone)
            if CONFIG.sakimononikkei_sub(zone) == "負け":
                self.sub_total+= int(CONFIG.nikkei_mini_result(zone))
                self.sub_total = "+" + str(self.sub_total) if self.sub_total > 0 else "±" + str(self.sub_total) if self.sub_total == 0 else str(self.sub_total)
                return "-" + CONFIG.nikkei_mini_result(zone)
            if CONFIG.sakimononikkei_sub(zone) == "引き分け":
                self.sub_total+= int(CONFIG.nikkei_mini_result(zone))
                self.sub_total = "+" + str(self.sub_total) if self.sub_total > 0 else "±" + str(self.sub_total) if self.sub_total == 0 else str(self.sub_total)
                return "±" + CONFIG.nikkei_mini_result(zone)
        if zone == "前場":
            if CONFIG.sakimononikkei_sub(zone) == "勝ち":
                self.sub_total-= int(CONFIG.nikkei_mini_result(zone))
                self.sub_total = "+" + str(self.sub_total) if self.sub_total > 0 else "±" + str(self.sub_total) if self.sub_total == 0 else str(self.sub_total)
                return "+" + CONFIG.nikkei_mini_result(zone)
            if CONFIG.sakimononikkei_sub(zone) == "負け":
                self.sub_total-= int(CONFIG.nikkei_mini_result(zone))
                self.sub_total = "+" + str(self.sub_total) if self.sub_total > 0 else "±" + str(self.sub_total) if self.sub_total == 0 else str(self.sub_total)
                return "-" + CONFIG.nikkei_mini_result(zone)
            if CONFIG.sakimononikkei_sub(zone) == "引き分け":
                self.sub_total-= int(CONFIG.nikkei_mini_result(zone))
                self.sub_total = "+" + str(self.sub_total) if self.sub_total > 0 else "±" + str(self.sub_total) if self.sub_total == 0 else str(self.sub_total)
                return "±" + CONFIG.nikkei_mini_result(zone)
        if zone == "後場":
            if CONFIG.sakimononikkei_sub(zone) == "勝ち":
                self.sub_total+= int(CONFIG.nikkei_mini_result(zone))
                self.sub_total = "+" + str(self.sub_total) if self.sub_total > 0 else "±" + str(self.sub_total) if self.sub_total == 0 else str(self.sub_total)
                return "+" + CONFIG.nikkei_mini_result(zone)
            if CONFIG.sakimononikkei_sub(zone) == "負け":
                self.sub_total+= int(CONFIG.nikkei_mini_result(zone))
                self.sub_total = "+" + str(self.sub_total) if self.sub_total > 0 else "±" + str(self.sub_total) if self.sub_total == 0 else str(self.sub_total)
                return "-" + CONFIG.nikkei_mini_result(zone)
            if CONFIG.sakimononikkei_sub(zone) == "引き分け":
                self.sub_total+= int(CONFIG.nikkei_mini_result(zone))
                self.sub_total = "+" + str(self.sub_total) if self.sub_total > 0 else "±" + str(self.sub_total) if self.sub_total == 0 else str(self.sub_total)
                return "±" + CONFIG.nikkei_mini_result(zone)

    def get_main_result(self,zone):
        if zone == "日中":
            if CONFIG.sakimononikkei_main(zone) == "勝ち":
                self.main_total+= int(CONFIG.nikkei_mini_result(zone))
                self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
                return "+" + CONFIG.nikkei_mini_result(zone)
            if CONFIG.sakimononikkei_main(zone) == "負け":
                self.main_total+= int(CONFIG.nikkei_mini_result(zone))
                self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
                return "-" + CONFIG.nikkei_mini_result(zone)
            if CONFIG.sakimononikkei_main(zone) == "引き分け":
                self.main_total+= int(CONFIG.nikkei_mini_result(zone))
                self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
                return "±" + CONFIG.nikkei_mini_result(zone)
        if zone == "前場":
            if CONFIG.sakimononikkei_main(zone) == "勝ち":
                self.main_total-= int(CONFIG.nikkei_mini_result(zone))
                self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
                return "+" + CONFIG.nikkei_mini_result(zone)
            if CONFIG.sakimononikkei_main(zone) == "負け":
                self.main_total-= int(CONFIG.nikkei_mini_result(zone))
                self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
                return "-" + CONFIG.nikkei_mini_result(zone)
            if CONFIG.sakimononikkei_main(zone) == "引き分け":
                self.main_total-= int(CONFIG.nikkei_mini_result(zone))
                self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
                return "±" + CONFIG.nikkei_mini_result(zone)
        if zone == "後場":
            if CONFIG.sakimononikkei_main(zone) == "勝ち":
                self.main_total+= int(CONFIG.nikkei_mini_result(zone))
                self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
                return "+" + CONFIG.nikkei_mini_result(zone)
            if CONFIG.sakimononikkei_main(zone) == "負け":
                self.main_total+= int(CONFIG.nikkei_mini_result(zone))
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
            self.main_total = open('other_txt/sakimononikkei/sakimononikkei_after_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "後場":
            self.main_total = open('other_txt/sakimononikkei/sakimononikkei_before_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)

    def get_sub_total_file(self,zone):
        if zone == "日中":
            self.sub_total = open('other_txt/sakimononikkei/sakimononikkei_day_sub_total.txt', 'r').read()
            self.sub_total = 0 if self.sub_total == "±0" else int(self.sub_total)
        if zone == "前場":
            self.sub_total = open('other_txt/sakimononikkei/sakimononikkei_after_sub_total.txt', 'r').read()
            self.sub_total = 0 if self.sub_total == "±0" else int(self.sub_total)
        if zone == "後場":
            self.sub_total = open('other_txt/sakimononikkei/sakimononikkei_before_sub_total.txt', 'r').read()
            self.sub_total = 0 if self.sub_total == "±0" else int(self.sub_total)
    
    def save_main_total_file(self,zone):
        if zone == "日中":
            open('other_txt/sakimononikkei/sakimononikkei_day_main_total.txt', 'w').write(str(self.main_total))
        if zone == "前場":
            open('other_txt/sakimononikkei/sakimononikkei_after_main_total.txt', 'w').write(str(self.main_total))
        if zone == "後場":
            open('other_txt/sakimononikkei/sakimononikkei_before_main_total.txt', 'w').write(str(self.main_total))
    
    def save_sub_total_file(self,zone):
        if zone == "日中":
            open('other_txt/sakimononikkei/sakimononikkei_day_sub_total.txt', 'w').write(str(self.sub_total))
        if zone == "前場":
            open('other_txt/sakimononikkei/sakimononikkei_after_sub_total.txt', 'w').write(str(self.sub_total))
        if zone == "後場":
            open('other_txt/sakimononikkei/sakimononikkei_before_sub_total.txt', 'w').write(str(self.sub_total))

    def __init__(self,driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()  
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.day_will_hour = "6"
        self.before_will_hour = "6"
        self.after_will_hour = "12"

        self.day_will_minute = "30"
        self.before_will_minute = "35"
        self.after_will_minute = "00"

        self.will_second = "00"
    
    def automation(self):
        self.login_fc2()
        zones = ["日中","前場","後場"]
        for zone in zones:
            self.get_main_total_file(zone)
            self.get_sub_total_file(zone)
            self.blog_post(zone,CONFIG.sakimononikkei_sub_buy_result(zone),self.get_sub_result(zone),self.get_main_result(zone),self.sub_total,self.main_total,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_main_total_file(zone)
            self.save_sub_total_file
