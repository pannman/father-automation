from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.okuman_text_config import OkumanText
from .fc2 import Fc2
import datetime

class Okuman(Fc2):
    def login_id(self):
        return LOGIN.OKUMAN_LOGIN['ID']

    def login_pass(self):
        return LOGIN.OKUMAN_LOGIN['PASS']

    def get_category_num(self,zone):
        if zone == "日中":
            self.category_num = 0
        if zone == "ナイトセッション":
            self.category_num = 0
        if zone == "オーバーナイト2":
            self.category_num = 0
    
    def return_will_hour(self,zone):
        if zone == "日中":
            return self.day_will_hour
        if zone == "ナイトセッション":
            return self.nightsession_will_hour
        if zone == "オーバーナイト2":
            return self.overnight2_will_hour
    
    def return_will_minute(self,zone):
        if zone == "日中":
            return self.day_will_minute
        if zone == "ナイトセッション":
            return self.nightsession_will_minute
        if zone == "オーバーナイト2":
            return self.overnight2_will_minute

    def get_main_result(self,zone):
        if CONFIG.okuman_main(zone) == "勝ち":
            self.main_total+= int(CONFIG.nikkei_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "+" + CONFIG.nikkei_result(zone)
        if CONFIG.okuman_main(zone) == "負け":
            self.main_total-= int(CONFIG.nikkei_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "-" + CONFIG.nikkei_result(zone)
        if CONFIG.okuman_main(zone) == "引き分け":
            self.main_total+= int(CONFIG.nikkei_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "±" + CONFIG.nikkei_result(zone)

    def get_main_total_file(self,zone):
        if zone == "日中":
            self.main_total = open('other_txt/okuman/okuman_day_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "ナイトセッション":
            self.main_total = open('other_txt/okuman/okuman_nightsession_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "オーバーナイト2":
            self.main_total = open('other_txt/okuman/okuman_overnight2_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
    
    def save_main_total_file(self,zone):
        if zone == "日中":
            open('other_txt/okuman/okuman_day_main_total.txt', 'w').write(str(self.main_total))
        if zone == "ナイトセッション":
            open('other_txt/okuman/okuman_nightsession_main_total.txt', 'w').write(str(self.main_total))
        if zone == "オーバーナイト2":
            open('other_txt/okuman/okuman_overnight2_main_total.txt', 'w').write(str(self.main_total))
        
    def get_other_main_total(self,zone):
        if zone == "日中":
            main_total = open('other_txt/okuman/okuman_day_main_total.txt', 'r').read()
        if zone == "ナイトセッション":
            main_total = open('other_txt/okuman/okuman_nightsession_main_total.txt', 'r').read()
        if zone == "オーバーナイト2":
            main_total = open('other_txt/okuman/okuman_overnight2_main_total.txt', 'r').read()
        main_total = 0 if main_total == "±0" else int(main_total)
        main_total = "+" + str(main_total) if main_total > 0 else "±" + str(main_total) if main_total == 0 else str(main_total)
        return main_total

    def get_total_profit(self,zone):
        if CONFIG.okuman_main(zone) == "勝ち":
            self.total_profit = open('other_txt/okuman/okuman_total_profit.txt', 'r').read()
            self.total_profit = int(self.total_profit) + (int(CONFIG.nikkei_result(zone))*1000) - 692
        if CONFIG.okuman_main(zone) == "負け":
            self.total_profit = open('other_txt/okuman/okuman_total_profit.txt', 'r').read()
            self.total_profit = int(self.total_profit) - (int(CONFIG.nikkei_result(zone))*1000) - 692
        if CONFIG.okuman_main(zone) == "引き分け":
            self.total_profit = open('other_txt/okuman/okuman_total_profit.txt', 'r').read()
            self.total_profit = int(self.total_profit) + (int(CONFIG.nikkei_result(zone))*1000) - 692
    
    def day_main_sign(self):
        zone = "日中"
        if CONFIG.okuman_main(zone) == "勝ち":
            return "+" + CONFIG.nikkei_result(zone)
        if CONFIG.okuman_main(zone) == "負け":
            return "-" + CONFIG.nikkei_result(zone)
        if CONFIG.okuman_main(zone) == "引き分け":
            return "±" + CONFIG.nikkei_result(zone)

    def nightsession_main_sign(self):
        zone = "ナイトセッション"
        if CONFIG.okuman_main(zone) == "勝ち":
            return "+" + CONFIG.nikkei_result(zone)
        if CONFIG.okuman_main(zone) == "負け":
            return "-" + CONFIG.nikkei_result(zone)
        if CONFIG.okuman_main(zone) == "引き分け":
            return "±" + CONFIG.nikkei_result(zone)
    
    def save_total_profit(self):
        open('other_txt/okuman/okuman_total_profit.txt', 'w').write(str(self.total_profit))

    def __init__(self,driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()  
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.day_will_hour = "8"
        self.nightsession_will_hour = "14"
        self.overnight2_will_hour = "19"

        self.day_will_minute = "45"
        self.nightsession_will_minute = "45"
        self.overnight2_will_minute = "50"

        self.will_second = "00"
    
    def automation(self,num):
        print("億万長者")
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "日中"
            print(zone)
            self.get_category_num(zone)
            self.get_main_total_file(zone)
            self.get_total_profit(zone)
            okuman_text = OkumanText(zone,CONFIG.okuman_main_buy_result(zone),self.get_main_result(zone),self.main_total,self.get_other_main_total("ナイトセッション"),self.get_other_main_total("オーバーナイト2"),self.total_profit,self.day_main_sign(),CONFIG.okuman_main_buy_result("日中"),self.nightsession_main_sign(),CONFIG.okuman_main_buy_result("ナイトセッション"))
            self.blog_post(self.category_num,okuman_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_main_total_file(zone)
            self.save_total_profit()
        if num == 5:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "ナイトセッション"
            print(zone)
            self.get_category_num(zone)
            self.get_main_total_file(zone)
            self.get_total_profit(zone)
            okuman_text = OkumanText(zone,CONFIG.okuman_main_buy_result(zone),self.get_main_result(zone),self.get_other_main_total("日中"),self.main_total,self.get_other_main_total("オーバーナイト2"),self.total_profit,self.day_main_sign(),CONFIG.okuman_main_buy_result("日中"),self.nightsession_main_sign(),CONFIG.okuman_main_buy_result("ナイトセッション"))
            self.blog_post(self.category_num,okuman_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_main_total_file(zone)
            self.save_total_profit()
        if num == 9:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "オーバーナイト2"
            print(zone)
            self.get_category_num(zone)
            self.get_main_total_file(zone)
            self.get_total_profit(zone)
            okuman_text = OkumanText(zone,CONFIG.okuman_main_buy_result(zone),self.get_main_result(zone),self.get_other_main_total("日中"),self.get_other_main_total("ナイトセッション"),self.main_total,self.total_profit,self.day_main_sign(),CONFIG.okuman_main_buy_result("日中"),self.nightsession_main_sign(),CONFIG.okuman_main_buy_result("ナイトセッション"))
            self.blog_post(self.category_num,okuman_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_main_total_file(zone)
            self.save_total_profit()
