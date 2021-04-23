from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.sakusesunikki_text_config import SakusesunikkiText
from .fc2 import Fc2
import datetime

class Sakusesunikki(Fc2):
    def login_id(self):
        return LOGIN.SAKUSESUNIKKI_LOGIN['ID']

    def login_pass(self):
        return LOGIN.SAKUSESUNIKKI_LOGIN['PASS']
    
    def return_will_hour(self,zone):
        if zone == "日中":
            return self.day_will_hour
        if zone == "ナイトセッション":
            return self.nightsession_will_hour
        if zone == "オーバーナイト2":
            return self.overnigh2_will_hour
    
    def return_will_minute(self,zone):
        if zone == "日中":
            return self.day_will_minute
        if zone == "ナイトセッション":
            return self.nightsession_will_minute
        if zone == "オーバーナイト2":
            return self.overnight2_will_minute
    
    def get_sub_result(self,zone):
        if CONFIG.sakusesunikki_sub(zone) == "勝ち":
            self.sub_total+= int(CONFIG.nikkei_mini_result(zone))
            self.sub_total = "+" + str(self.sub_total) if self.sub_total > 0 else "±" + str(self.sub_total) if self.sub_total == 0 else str(self.sub_total)
            return "+" + CONFIG.nikkei_mini_result(zone)
        if CONFIG.sakusesunikki_sub(zone) == "負け":
            self.sub_total-= int(CONFIG.nikkei_mini_result(zone))
            self.sub_total = "+" + str(self.sub_total) if self.sub_total > 0 else "±" + str(self.sub_total) if self.sub_total == 0 else str(self.sub_total)
            return "-" + CONFIG.nikkei_mini_result(zone)
        if CONFIG.sakusesunikki_sub(zone) == "引き分け":
            self.sub_total+= int(CONFIG.nikkei_mini_result(zone))
            self.sub_total = "+" + str(self.sub_total) if self.sub_total > 0 else "±" + str(self.sub_total) if self.sub_total == 0 else str(self.sub_total)
            return "±" + CONFIG.nikkei_mini_result(zone)

    def get_main_result(self,zone):
        if CONFIG.sakusesunikki_main(zone) == "勝ち":
            self.main_total+= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "+" + CONFIG.nikkei_mini_result(zone)
        if CONFIG.sakusesunikki_main(zone) == "負け":
            self.main_total-= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "-" + CONFIG.nikkei_mini_result(zone)
        if CONFIG.sakusesunikki_main(zone) == "引き分け":
            self.main_total+= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "±" + CONFIG.nikkei_mini_result(zone)

    def get_main_total_file(self,zone):
        if zone == "日中":
            self.main_total = open('other_txt/sakusesunikki/sakusesunikki_day_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "ナイトセッション":
            self.main_total = open('other_txt/sakusesunikki/sakusesunikki_nightsession_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "オーバーナイト":
            self.main_total = open('other_txt/sakusesunikki/sakusesunikki_overnight2_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if datetime.datetime.now().day == 1:
            self.main_total = 0

    def get_sub_total_file(self,zone):
        if zone == "日中":
            self.sub_total = open('other_txt/sakusesunikki/sakusesunikki_day_sub_total.txt', 'r').read()
            self.sub_total = 0 if self.sub_total == "±0" else int(self.sub_total)
        if zone == "ナイトセッション":
            self.sub_total = open('other_txt/sakusesunikki/sakusesunikki_nightsession_sub_total.txt', 'r').read()
            self.sub_total = 0 if self.sub_total == "±0" else int(self.sub_total)
        if zone == "オーバーナイト2":
            self.sub_total = open('other_txt/sakusesunikki/sakusesunikki_overnight2_sub_total.txt', 'r').read()
            self.sub_total = 0 if self.sub_total == "±0" else int(self.sub_total)
        if datetime.datetime.now().day == 1:
            self.sub_total = 0
    
    def save_main_total_file(self,zone):
        if zone == "日中":
            open('other_txt/sakusesunikki/sakusesunikki_day_main_total.txt', 'w').write(str(self.main_total))
        if zone == "ナイトセッション":
            open('other_txt/sakusesunikki/sakusesunikki_nightsession_main_total.txt', 'w').write(str(self.main_total))
        if zone == "オーバーナイト2":
            open('other_txt/sakusesunikki/sakusesunikki_overnight2_main_total.txt', 'w').write(str(self.main_total))
    
    def save_sub_total_file(self,zone):
        if zone == "日中":
            open('other_txt/sakusesunikki/sakusesunikki_day_sub_total.txt', 'w').write(str(self.sub_total))
        if zone == "ナイトセッション":
            open('other_txt/sakusesunikki/sakusesunikki_nightsession_sub_total.txt', 'w').write(str(self.sub_total))
        if zone == "オーバーナイト2":
            open('other_txt/sakusesunikki/sakusesunikki_overnight2_sub_total.txt', 'w').write(str(self.sub_total))

    def __init__(self,driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()  
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.day_will_hour = "7"
        self.nightsession_will_hour = "16"
        # self.overnight2_will_hour = 

        self.day_will_minute = "45"
        self.nightsession_will_minute = "15"
        # self.overnight2_will_minute = 

        self.will_second = "00"
    
    def automation(self,num):
        if num == 3:
            self.login_fc2()
            zone = "日中"
            self.get_main_total_file(zone)
            self.get_sub_total_file(zone)
            sakusesunikki_text = SakusesunikkiText(zone,CONFIG.sakusesunikki_sub_buy_result(zone),self.get_sub_result(zone),self.get_main_result(zone),self.sub_total,self.main_total)
            self.blog_post(sakusesunikki_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_main_total_file(zone)
            self.save_sub_total_file(zone)
        if num == 5:
            self.login_fc2()
            zone = "ナイトセッション"
            self.get_main_total_file(zone)
            self.get_sub_total_file(zone)
            sakusesunikki_text = SakusesunikkiText(zone,CONFIG.sakusesunikki_sub_buy_result(zone),self.get_sub_result(zone),self.get_main_result(zone),self.sub_total,self.main_total)
            self.blog_post(sakusesunikki_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_main_total_file(zone)
            self.save_sub_total_file(zone)
        if num == 9:
            self.login_fc2()
            zone = "オーバーナイト2"
            self.get_main_total_file(zone)
            self.get_sub_total_file(zone)
            sakusesunikki_text = SakusesunikkiText(zone,CONFIG.sakusesunikki_sub_buy_result(zone),self.get_sub_result(zone),self.get_main_result(zone),self.sub_total,self.main_total)
            self.blog_post(sakusesunikki_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_main_total_file(zone)
            self.save_sub_total_file(zone)
