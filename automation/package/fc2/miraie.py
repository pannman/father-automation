from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.miraie_text_config import MiraieText
from .fc2 import Fc2
import datetime


class Miraie(Fc2):
    def login_id(self):
        return LOGIN.MIRAIE_LOGIN['ID']

    def login_pass(self):
        return LOGIN.MIRAIE_LOGIN['PASS']
    
    def return_will_hour(self,zone):
        if zone == "日中":
            return self.day_will_hour
        if zone == "ナイトセッション":
            return self.nightsession_will_hour

    def return_will_minute(self,zone):
        if zone == "日中":
            return self.day_will_minute
        if zone == "ナイトセッション":
            return self.nightsession_will_minute

    def get_main_result(self,zone):
        if CONFIG.miraie_main(zone) == "勝ち":
            self.main_total+= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "+" + CONFIG.nikkei_mini_result(zone)
        if CONFIG.miraie_main(zone) == "負け":
            self.main_total-= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "-" + CONFIG.nikkei_mini_result(zone)
        if CONFIG.miraie_main(zone) == "引き分け":
            self.main_total+= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "±" + CONFIG.nikkei_mini_result(zone)
    
    def get_all_main_total(self,zone):
        if zone == "日中":
            other_main_total = open('other_txt/miraie/miraie_nightsession_main_total.txt', 'r').read()
            self.all_main_total = int(other_main_total) + int(self.main_total)
            self.all_main_total = "+" + str(self.all_main_total) if self.all_main_total > 0 else "±" + str(self.all_main_total) if self.all_main_total == 0 else str(self.all_main_total)
            return self.all_main_total
        if zone == "ナイトセッション":
            other_main_total = open('other_txt/miraie/miraie_day_main_total.txt', 'r').read()
            self.all_main_total = int(other_main_total) + int(self.main_total)
            self.all_main_total = "+" + str(self.all_main_total) if self.all_main_total > 0 else "±" + str(self.all_main_total) if self.all_main_total == 0 else str(self.all_main_total)
            return self.all_main_total

    def get_total_file(self,zone):
        if zone == "日中":
            self.main_total = open('other_txt/miraie/miraie_day_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "ナイトセッション":
            self.main_total = open('other_txt/miraie/miraie_nightsession_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)

    def save_total_file(self,zone):
        if zone == "日中":
            open('other_txt/miraie/miraie_day_main_total.txt', 'w').write(str(self.main_total))
        if zone == "ナイトセッション":
            open('other_txt/miraie/miraie_nightsession_main_total.txt', 'w').write(str(self.main_total))
        
    def get_miraie_result_settlement_money(self,zone):
        if (CONFIG.miraie_main(zone) == "勝ち" and CONFIG.miraie_main_buy_result(zone) == "買い") or (CONFIG.miraie_main(zone) == "負け" and CONFIG.miraie_main_buy_result(zone) == "売り"):
            self.result_settlement_money = str(int(CONFIG.miraie_result_trade_money(zone)) + int(CONFIG.nikkei_result(zone)))
            return self.result_settlement_money
        if (CONFIG.miraie_main(zone) == "負け" and CONFIG.miraie_main_buy_result(zone) == "売り") or (CONFIG.miraie_main(zone) == "勝ち" and CONFIG.miraie_main_buy_result(zone) == "買い"):
            self.result_settlement_money = str(int(CONFIG.miraie_result_trade_money(zone)) - int(CONFIG.nikkei_result(zone)))
            return self.result_settlement_money
            
    def __init__(self,driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()  
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.day_will_hour = "8"
        self.nightsession_will_hour = "16"

        self.day_will_minute = "35"
        self.nightsession_will_minute = "45"

        self.will_second = "00"
    
    def automation(self,num):
        print("未来への挑戦")
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "日中"
            print(zone)
            self.get_total_file(zone)
            miraie_text = MiraieText(zone,CONFIG.miraie_main_buy_result(zone),self.get_main_result(zone),self.main_total,CONFIG.miraie_result_trade_money(zone),self.get_miraie_result_settlement_money(zone),self.get_all_main_total(zone))
            self.blog_post(miraie_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)

        if num == 5:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "ナイトセッション"
            print(zone)
            self.get_total_file(zone)
            miraie_text = MiraieText(zone,CONFIG.miraie_main_buy_result(zone),self.get_main_result(zone),self.main_total,CONFIG.miraie_result_trade_money(zone),self.get_miraie_result_settlement_money(zone),self.get_all_main_total(zone))
            self.blog_post(miraie_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)