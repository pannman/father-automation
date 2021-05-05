from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.subarashiki_text_config import SubarashikiText
from .fc2 import Fc2
import datetime


class Subarashiki(Fc2):
    def login_id(self):
        return LOGIN.SUBARASHIKI_LOGIN['ID']

    def login_pass(self):
        return LOGIN.SUBARASHIKI_LOGIN['PASS']
    
    def return_will_hour(self,zone):
        if zone == "日中":
            return self.day_will_hour
        if zone == "前場":
            return self.before_will_hour
        if zone == "後場":
            return self.after_will_hour
        if zone == "ナイトセッション":
            return self.nightsession_will_hour
        if zone == "オーバーナイト":
            return self.overnight1_will_hour

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

    def get_main_result(self,zone):
        if CONFIG.subarashiki_main(zone) == "勝ち":
            self.main_total+= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "+" + CONFIG.nikkei_mini_result(zone)
        if CONFIG.subarashiki_main(zone) == "負け":
            self.main_total-= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "-" + CONFIG.nikkei_mini_result(zone)
        if CONFIG.subarashiki_main(zone) == "引き分け":
            self.main_total+= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "±" + CONFIG.nikkei_mini_result(zone)

    def get_total_file(self,zone):
        if zone == "日中":
            self.main_total = open('other_txt/subarashiki/subarashiki_day_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "前場":
            self.main_total = open('other_txt/subarashiki/subarashiki_before_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "後場":
            self.main_total = open('other_txt/subarashiki/subarashiki_after_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "ナイトセッション":
            self.main_total = open('other_txt/subarashiki/subarashiki_nightsession_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "オーバーナイト1":
            self.main_total = open('other_txt/subarashiki/subarashiki_overnight1_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)

    def save_total_file(self,zone):
        if zone == "日中":
            open('other_txt/subarashiki/subarashiki_day_main_total.txt', 'w').write(str(self.main_total))
        if zone == "前場":
            open('other_txt/subarashiki/subarashiki_before_main_total.txt', 'w').write(str(self.main_total))
        if zone == "後場":
            open('other_txt/subarashiki/subarashiki_after_main_total.txt', 'w').write(str(self.main_total))
        if zone == "ナイトセッション":
            open('other_txt/subarashiki/subarashiki_nightsession_main_total.txt', 'w').write(str(self.main_total))
        if zone == "オーバーナイト1":
            open('other_txt/subarashiki/subarashiki_overnight1_main_total.txt', 'w').write(str(self.main_total))
    
    def get_subarashiki_result_settlement_money(self,zone):
        if (CONFIG.subarashiki_main(zone) == "勝ち" and CONFIG.subarashiki_main_buy_result(zone) == "買い") or (CONFIG.subarashiki_main(zone) == "負け" and CONFIG.subarashiki_main_buy_result(zone) == "売り"):
            self.result_settlement_money = str(int(CONFIG.subarashiki_result_trade_money(zone)) + int(CONFIG.nikkei_result(zone)))
            return self.result_settlement_money
        if (CONFIG.subarashiki_main(zone) == "勝ち" and CONFIG.subarashiki_main_buy_result(zone) == "売り") or (CONFIG.subarashiki_main(zone) == "負け" and CONFIG.subarashiki_main_buy_result(zone) == "買い"):
            self.result_settlement_money = str(int(CONFIG.subarashiki_result_trade_money(zone)) - int(CONFIG.nikkei_result(zone)))
            return self.result_settlement_money
            
    def __init__(self,driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()  
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.day_will_hour = "9"
        self.before_will_hour = "9"
        self.after_will_hour = "12"
        self.nightsession_will_hour = "16"
        self.overnight1_will_hour = "16"

        self.day_will_minute = "00"
        self.before_will_minute = "05"
        self.after_will_minute = "35"
        self.nightsession_will_minute = "50"
        self.overnight1_will_minute = "55"

        self.will_second = "00"
    
    def automation(self,num):
        print("素晴らしき人生")
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zones = ["日中","前場","後場"]
            for zone in zones:
                print(zone)
                self.get_total_file(zone)
                subarashiki_text = SubarashikiText(zone,CONFIG.subarashiki_main_buy_result(zone),self.get_main_result(zone),self.main_total,CONFIG.subarashiki_result_trade_money(zone),self.get_subarashiki_result_settlement_money(zone))
                self.blog_post(subarashiki_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
                self.save_total_file(zone)

        if num == 5:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "ナイトセッション"
            print(zone)
            self.get_total_file(zone)
            subarashiki_text = SubarashikiText(zone,CONFIG.subarashiki_main_buy_result(zone),self.get_main_result(zone),self.main_total,CONFIG.subarashiki_result_trade_money(zone),self.get_subarashiki_result_settlement_money(zone))
            self.blog_post(subarashiki_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)
        if num == 9:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "オーバーナイト1"
            print(zone)
            self.get_total_file(zone)
            subarashiki_text = SubarashikiText(zone,CONFIG.subarashiki_main_buy_result(zone),self.get_main_result(zone),self.main_total,CONFIG.subarashiki_result_trade_money(zone),self.get_subarashiki_result_settlement_money(zone))
            self.blog_post(subarashiki_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)