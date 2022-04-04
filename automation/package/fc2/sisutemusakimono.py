from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.sisutemusakimono_text_config import SisutemusakimonoText
from .fc2 import Fc2
import datetime


class Sisutemusakimono(Fc2):
    def login_id(self):
        return LOGIN.SISUTEMUSAKIMONO_LOGIN['ID']

    def login_pass(self):
        return LOGIN.SISUTEMUSAKIMONO_LOGIN['PASS']

    def get_category_num(self, zone):
        if zone == "日中":
            self.category_num = 1
        if zone == "夜間":
            self.category_num = 1

    def return_will_hour(self, zone):
        if zone == "日中":
            return self.day_will_hour
        if zone == "夜間":
            return self.yakan_will_hour

    def return_will_minute(self, zone):
        if zone == "日中":
            return self.day_will_minute
        if zone == "夜間":
            return self.yakan_will_minute

    def get_time(self, zone):
        if zone == "日中":
            self.buy_time = "08:45"
            self.settlement_time = "15:15"
        if zone == "夜間":
            self.buy_time = "16:30"
            self.settlement_time = "y06:00"

    def get_main_sign_gold(self, zone):
        self.zone_gold = CONFIG.gold_sakimono(self.buy_time)
        if CONFIG.sisutemusakimono_main_buy_result_gold(zone) == "売り":

            self.zone_settlement_gold = int(
                str(CONFIG.gold_sakimono(self.settlement_time)))

            self.main_sign_gold = int(
                str(self.zone_gold - self.zone_settlement_gold))
        if CONFIG.sisutemusakimono_main_buy_result_gold(zone) == "買い":

            self.zone_gold = int(str(self.zone_gold))

            self.zone_settlement_gold = CONFIG.gold_sakimono(
                self.settlement_time)
            self.main_sign_gold = int(
                str(self.zone_settlement_gold - self.zone_gold))
        self.main_sign_gold = "+" + \
            str(self.main_sign_gold) if self.main_sign_gold > 0 else "±0" if self.main_sign_gold == 0 else str(
                self.main_sign_gold)

    def get_main_sign_platinum(self, zone):
        self.zone_platinum = CONFIG.platinum_sakimono(self.buy_time)
        if CONFIG.sisutemusakimono_main_buy_result_platinum(zone) == "売り":
            self.zone_settlement_platinum = int(
                str(CONFIG.platinum_sakimono(self.settlement_time)))
            self.main_sign_platinum = int(
                str(self.zone_platinum - self.zone_settlement_platinum))
        if CONFIG.sisutemusakimono_main_buy_result_platinum(zone) == "買い":
            self.zone_platinum = int(str(self.zone_platinum))
            self.zone_settlement_platinum = CONFIG.platinum_sakimono(
                self.settlement_time)
            self.main_sign_platinum = int(
                str(self.zone_settlement_platinum - self.zone_platinum))
        self.main_sign_platinum = "+" + \
            str(self.main_sign_platinum) if self.main_sign_platinum > 0 else "±0" if self.main_sign_platinum == 0 else str(
                self.main_sign_platinum)

    def get_main_total_gold(self):
        if self.main_sign_gold == "±0":
            self.main_sign_gold = "0"
        self.main_total_gold = self.main_total_gold + int(self.main_sign_gold)
        self.main_total_gold = "+" + \
            str(self.main_total_gold) if self.main_total_gold > 0 else "±0" if self.main_total_gold == 0 else str(
                self.main_total_gold)

    def get_main_total_platinum(self):
        if self.main_sign_platinum == "±0":
            self.main_sign_platinum = "0"
        self.main_total_platinum = self.main_total_platinum + \
            int(self.main_sign_platinum)
        self.main_total_platinum = "+" + \
            str(self.main_total_platinum) if self.main_total_platinum > 0 else "±0" if self.main_total_platinum == 0 else str(
                self.main_total_platinum)

    def get_total_platinum_file(self, zone):
        if zone == "日中":
            self.main_total_platinum = open(
                'other_txt/sisutemusakimono/sisutemusakimono_day_main_total_platinum.txt', 'r').read()
            self.main_total_platinum = 0 if self.main_total_platinum == "±0" else int(
                self.main_total_platinum)
        if zone == "夜間":
            self.main_total_platinum = open(
                'other_txt/sisutemusakimono/sisutemusakimono_yakan_main_total_platinum.txt', 'r').read()
            self.main_total_platinum = 0 if self.main_total_platinum == "±0" else int(
                self.main_total_platinum)

    def save_total_platinum_file(self, zone):
        if zone == "日中":
            open('other_txt/sisutemusakimono/sisutemusakimono_day_main_total_platinum.txt',
                 'w').write(str(self.main_total_platinum))
        if zone == "夜間":
            open('other_txt/sisutemusakimono/sisutemusakimono_yakan_main_total_platinum.txt',
                 'w').write(str(self.main_total_platinum))

    def get_total_gold_file(self, zone):
        if zone == "日中":
            self.main_total_gold = open(
                'other_txt/sisutemusakimono/sisutemusakimono_day_main_total_gold.txt', 'r').read()
            self.main_total_gold = 0 if self.main_total_gold == "±0" else int(
                self.main_total_gold)
        if zone == "夜間":
            self.main_total_gold = open(
                'other_txt/sisutemusakimono/sisutemusakimono_yakan_main_total_gold.txt', 'r').read()
            self.main_total_gold = 0 if self.main_total_gold == "±0" else int(
                self.main_total_gold)

    def save_total_gold_file(self, zone):
        if zone == "日中":
            open('other_txt/sisutemusakimono/sisutemusakimono_day_main_total_gold.txt',
                 'w').write(str(self.main_total_gold))
        if zone == "夜間":
            open('other_txt/sisutemusakimono/sisutemusakimono_yakan_main_total_gold.txt',
                 'w').write(str(self.main_total_gold))

    def __init__(self, driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.day_will_hour = "8"
        self.yakan_will_hour = "16"

        self.day_will_minute = "25"
        self.yakan_will_minute = "30"

        self.will_second = "00"

    def automation(self, num):
        print("システム先物")
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "日中"
            print(zone)
            self.get_time(zone)
            self.get_category_num(zone)
            self.get_total_gold_file(zone)
            self.get_total_platinum_file(zone)
            self.get_main_sign_gold(zone)

            self.get_main_sign_platinum(zone)
            self.get_main_total_gold()
            self.get_main_total_platinum()

            sisutemusakimono_text = SisutemusakimonoText(zone, CONFIG.sisutemusakimono_main_buy_result_gold(zone), CONFIG.sisutemusakimono_main_buy_result_platinum(zone), self.main_sign_gold, self.main_total_gold,
                                                     self.zone_gold, self.zone_settlement_gold, self.main_sign_platinum, self.main_total_platinum, self.zone_platinum, self.zone_settlement_platinum, self.buy_time, self.settlement_time)
            self.blog_post(self.category_num, sisutemusakimono_text, zone, self.will_year,
                           self.will_month, self.will_day, self.will_second)
            self.save_total_gold_file(zone)
            self.save_total_platinum_file(zone)

        if num == 5:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "夜間"
            print(zone)
            self.get_time(zone)
            self.get_category_num(zone)
            self.get_total_gold_file(zone)
            self.get_total_platinum_file(zone)
            self.get_main_sign_gold(zone)
            self.get_main_sign_platinum(zone)
            self.get_main_total_gold()
            self.get_main_total_platinum()
            sisutemusakimono_text = SisutemusakimonoText(zone, CONFIG.sisutemusakimono_main_buy_result_gold(zone), CONFIG.sisutemusakimono_main_buy_result_platinum(zone), self.main_sign_gold, self.main_total_gold,
                                                     self.zone_gold, self.zone_settlement_gold, self.main_sign_platinum, self.main_total_platinum, self.zone_platinum, self.zone_settlement_platinum, self.buy_time, self.settlement_time)
            self.blog_post(self.category_num, sisutemusakimono_text, zone, self.will_year,
                           self.will_month, self.will_day, self.will_second)
            self.save_total_gold_file(zone)
            self.save_total_platinum_file(zone)
