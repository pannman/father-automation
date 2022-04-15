from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.fxtecunikaruponndo_text_config import FxtecunikaruponndoText
from .fc2 import Fc2
from decimal import Decimal, ROUND_HALF_UP
import datetime


class Fxtecunikaruponndo(Fc2):
    def login_id(self):
        return LOGIN.FXTECUNIKARUPONNDO_LOGIN['ID']

    def login_pass(self):
        return LOGIN.FXTECUNIKARUPONNDO_LOGIN['PASS']

    def get_category_num(self, zone):
        if zone == "今日もがんばります！！ｂｙポンド":
            self.category_num = 5
        if zone == "次の予想も頑張ります！！byポンド":
            self.category_num = 6
        if zone == "ラストスパート！！ｂｙポンド":
            self.category_num = 4

    def return_will_hour(self, zone):
        if zone == "今日もがんばります！！ｂｙポンド":
            return self.fxtecunikaruponndo1_will_hour
        if zone == "次の予想も頑張ります！！byポンド":
            return self.fxtecunikaruponndo2_will_hour
        if zone == "ラストスパート！！ｂｙポンド":
            return self.fxtecunikaruponndo3_will_hour

    def return_will_minute(self, zone):
        if zone == "今日もがんばります！！ｂｙポンド":
            return self.fxtecunikaruponndo1_will_minute
        if zone == "次の予想も頑張ります！！byポンド":
            return self.fxtecunikaruponndo2_will_minute
        if zone == "ラストスパート！！ｂｙポンド":
            return self.fxtecunikaruponndo3_will_minute

    def get_time(self, zone):
        if zone == "今日もがんばります！！ｂｙポンド":
            self.buy_time = "09:00"
            self.settlement_time = "y08:30"
        if zone == "次の予想も頑張ります！！byポンド":
            self.buy_time = "16:00"
            self.settlement_time = "y15:30"
        if zone == "ラストスパート！！ｂｙポンド":
            self.buy_time = "22:00"
            self.settlement_time = "y08:30"

    def get_total_file(self, zone):
        if zone == "今日もがんばります！！ｂｙポンド":
            self.main_total = open(
                'other_txt/fxtecunikaruponndo/fxtecunikaruponndo_fxtecunikaruponndo1_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(
                self.main_total)
        if zone == "次の予想も頑張ります！！byポンド":
            self.main_total = open(
                'other_txt/fxtecunikaruponndo/fxtecunikaruponndo_fxtecunikaruponndo2_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(
                self.main_total)
        if zone == "ラストスパート！！ｂｙポンド":
            self.main_total = open(
                'other_txt/fxtecunikaruponndo/fxtecunikaruponndo_fxtecunikaruponndo3_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(
                self.main_total)

    def get_main_sign(self, zone):
        self.zone_lb = CONFIG.fx_zone_lb(self.buy_time)
        if CONFIG.fxtecunikaruponndo_main_buy_result(zone) == "売り":
            self.zone_settlement = float(Decimal(str(CONFIG.fx_zone_lb(
                self.settlement_time)+0.01)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.main_sign = float(Decimal(str(self.zone_lb - self.zone_settlement)
                                           ).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        if CONFIG.fxtecunikaruponndo_main_buy_result(zone) == "買い":
            self.zone_lb = float(Decimal(
                str(self.zone_lb+0.01)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.zone_settlement = CONFIG.fx_zone_lb(self.settlement_time)
            self.main_sign = float(Decimal(str(self.zone_settlement - self.zone_lb)
                                           ).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        self.main_sign = "+" + \
            str(self.main_sign) if self.main_sign > 0 else "±0" if self.main_sign == 0 else str(
                self.main_sign)

    def get_main_total(self):
        if self.main_sign == "±0":
            self.main_sign = "0"
        self.main_total = Decimal(str(self.main_total + float(self.main_sign))
                                  ).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        self.main_total = "+" + \
            str(self.main_total) if self.main_total > 0 else "±0" if self.main_total == 0 else str(
                self.main_total)

    def save_total_file(self, zone):
        if zone == "今日もがんばります！！ｂｙポンド":
            open('other_txt/fxtecunikaruponndo/fxtecunikaruponndo_fxtecunikaruponndo1_main_total.txt',
                 'w').write(str(self.main_total))
        if zone == "次の予想も頑張ります！！byポンド":
            open('other_txt/fxtecunikaruponndo/fxtecunikaruponndo_fxtecunikaruponndo2_main_total.txt',
                 'w').write(str(self.main_total))
        if zone == "ラストスパート！！ｂｙポンド":
            open('other_txt/fxtecunikaruponndo/fxtecunikaruponndo_fxtecunikaruponndo3_main_total.txt',
                 'w').write(str(self.main_total))

    def __init__(self, driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.fxtecunikaruponndo1_will_hour = "8"
        self.fxtecunikaruponndo2_will_hour = "15"
        self.fxtecunikaruponndo3_will_hour = "21"

        self.fxtecunikaruponndo1_will_minute = "50"
        self.fxtecunikaruponndo2_will_minute = "50"
        self.fxtecunikaruponndo3_will_minute = "50"

        self.will_second = "00"

    def automation(self, num):
        print("fxテクニカルポンド")
        if num == 1:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "今日もがんばります！！ｂｙポンド"
            print(zone)

            self.get_category_num(zone)

            self.get_time(zone)
            self.get_total_file(zone)
            self.get_main_sign(zone)

            self.get_main_total()

            fxtecunikaruponndo_text = FxtecunikaruponndoText(zone, CONFIG.fxtecunikaruponndo_main_buy_result(
                zone), self.main_sign, self.main_total, self.zone_lb, self.zone_settlement, self.buy_time, self.settlement_time)
            self.blog_post(self.category_num, fxtecunikaruponndo_text, zone,
                           self.will_year, self.will_month, self.will_day, self.will_second)
            self.save_total_file(zone)

        if num == 2:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "次の予想も頑張ります！！byポンド"
            print(zone)

            self.get_category_num(zone)

            self.get_time(zone)
            self.get_total_file(zone)
            self.get_main_sign(zone)

            self.get_main_total()

            fxtecunikaruponndo_text = FxtecunikaruponndoText(zone, CONFIG.fxtecunikaruponndo_main_buy_result(
                zone), self.main_sign, self.main_total, self.zone_lb, self.zone_settlement, self.buy_time, self.settlement_time)
            self.blog_post(self.category_num, fxtecunikaruponndo_text, zone,
                           self.will_year, self.will_month, self.will_day, self.will_second)
            self.save_total_file(zone)
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "ラストスパート！！ｂｙポンド"
            print(zone)

            self.get_category_num(zone)

            self.get_time(zone)
            self.get_total_file(zone)
            self.get_main_sign(zone)
            self.get_main_total()

            fxtecunikaruponndo_text = FxtecunikaruponndoText(zone, CONFIG.fxtecunikaruponndo_main_buy_result(
                zone), self.main_sign, self.main_total, self.zone_lb, self.zone_settlement, self.buy_time, self.settlement_time)
            self.blog_post(self.category_num, fxtecunikaruponndo_text, zone,
                           self.will_year, self.will_month, self.will_day, self.will_second)
            self.save_total_file(zone)
