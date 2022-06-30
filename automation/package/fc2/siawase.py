from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.siawase_text_config import SiawaseText
from .fc2 import Fc2
import datetime


class Siawase(Fc2):
    def login_id(self):
        return LOGIN.SIAWASE_LOGIN['ID']

    def login_pass(self):
        return LOGIN.SIAWASE_LOGIN['PASS']

    def get_category_num(self, zone):
        if zone == "日中":
            self.category_num = 0
        if zone == "ナイトセッション":
            self.category_num = 0
        if zone == "オーバーナイト":
            self.category_num = 0

    def return_will_hour(self, zone):
        if zone == "日中":
            return self.day_will_hour
        if zone == "ナイトセッション":
            return self.nightsession_will_hour
        if zone == "オーバーナイト":
            return self.overnight_will_hour

    def return_will_minute(self, zone):
        if zone == "日中":
            return self.day_will_minute
        if zone == "ナイトセッション":
            return self.nightsession_will_minute
        if zone == "オーバーナイト":
            return self.overnight_will_minute

    def get_main_result(self, zone):
        if CONFIG.siawase_main(zone) == "勝ち":
            self.main_total += int(CONFIG.nikkei_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(
                self.main_total) if self.main_total == 0 else str(self.main_total)
            return "+" + CONFIG.nikkei_result(zone)
        if CONFIG.siawase_main(zone) == "負け":
            self.main_total -= int(CONFIG.nikkei_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(
                self.main_total) if self.main_total == 0 else str(self.main_total)
            return "-" + CONFIG.nikkei_result(zone)
        if CONFIG.siawase_main(zone) == "引き分け":
            self.main_total += int(CONFIG.nikkei_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(
                self.main_total) if self.main_total == 0 else str(self.main_total)
            return "±" + CONFIG.nikkei_result(zone)

    def get_main_total_file(self, zone):
        if zone == "日中":
            self.main_total = open(
                'other_txt/siawase/siawase_day_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(
                self.main_total)
        if zone == "ナイトセッション":
            self.main_total = open(
                'other_txt/siawase/siawase_nightsession_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(
                self.main_total)
        if zone == "オーバーナイト":
            self.main_total = open(
                'other_txt/siawase/siawase_overnight_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(
                self.main_total)

    def save_main_total_file(self, zone):
        if zone == "日中":
            open('other_txt/siawase/siawase_day_main_total.txt',
                 'w').write(str(self.main_total))
        if zone == "ナイトセッション":
            open('other_txt/siawase/siawase_nightsession_main_total.txt',
                 'w').write(str(self.main_total))
        if zone == "オーバーナイト":
            open('other_txt/siawase/siawase_overnight_main_total.txt',
                 'w').write(str(self.main_total))
    
    def get_siawase_result_settlement_money(self, zone):
        if (CONFIG.siawase_main(zone) == "勝ち" and CONFIG.siawase_main_buy_result(zone) == "買い") or (CONFIG.siawase_main(zone) == "負け" and CONFIG.siawase_main_buy_result(zone) == "売り"):
            self.result_settlement_money = str(
                int(CONFIG.siawase_result_trade_money(zone)) + int(CONFIG.nikkei_result(zone)))
            return self.result_settlement_money
        if (CONFIG.siawase_main(zone) == "勝ち" and CONFIG.siawase_main_buy_result(zone) == "売り") or (CONFIG.siawase_main(zone) == "負け" and CONFIG.siawase_main_buy_result(zone) == "買い"):
            self.result_settlement_money = str(
                int(CONFIG.siawase_result_trade_money(zone)) - int(CONFIG.nikkei_result(zone)))
            return self.result_settlement_money
        else:
            self.result_settlement_money = str(
                int(CONFIG.siawase_result_trade_money(zone)))
            return self.result_settlement_money

    def __init__(self, driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.day_will_hour = "7"
        self.nightsession_will_hour = "15"
        self.overnight_will_hour = "22"

        self.day_will_minute = "55"
        self.nightsession_will_minute = "55"
        self.overnight_will_minute = "55"

        self.will_second = "00"

    def automation(self, num):
        print("幸せな人生")
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "日中"
            print(zone)
            self.get_category_num(zone)
            self.get_main_total_file(zone)
            siawase_text = SiawaseText(zone, CONFIG.siawase_main_buy_result(zone), self.get_main_result(zone), self.main_total, CONFIG.siawase_result_trade_money(zone), self.get_siawase_result_settlement_money(zone),CONFIG.siawase_main(zone))
            self.blog_post(self.category_num, siawase_text, zone,
                           self.will_year, self.will_month, self.will_day, self.will_second)
            self.save_main_total_file(zone)
        if num == 5:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "ナイトセッション"
            print(zone)
            self.get_category_num(zone)
            self.get_main_total_file(zone)
            siawase_text = SiawaseText(zone, CONFIG.siawase_main_buy_result(zone), self.get_main_result(
                zone), self.main_total, CONFIG.siawase_result_trade_money(zone), self.get_siawase_result_settlement_money(zone), CONFIG.siawase_main(zone))

            self.blog_post(self.category_num, siawase_text, zone,
                           self.will_year, self.will_month, self.will_day, self.will_second)
            self.save_main_total_file(zone)
        if num == 9:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "オーバーナイト"
            print(zone)
            self.get_category_num(zone)
            self.get_main_total_file(zone)
            siawase_text = SiawaseText(zone, CONFIG.siawase_main_buy_result(zone), self.get_main_result(
                zone), self.main_total, CONFIG.siawase_result_trade_money(zone), self.get_siawase_result_settlement_money(zone), CONFIG.siawase_main(zone))


            self.blog_post(self.category_num, siawase_text, zone,
                           self.will_year, self.will_month, self.will_day, self.will_second)
            self.save_main_total_file(zone)
