from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.fxtecunikaruyuro_text_config import FxtecunikaruyuroText
from .fc2 import Fc2
from decimal import Decimal, ROUND_HALF_UP
import datetime


class Fxtecunikaruyuro(Fc2):
    def login_id(self):
        return LOGIN.FXTECUNIKARUYURO_LOGIN['ID']

    def login_pass(self):
        return LOGIN.FXTECUNIKARUYURO_LOGIN['PASS']

    def get_category_num(self, zone):
        if zone == "今日もがんばります！！ｂｙユーロ":
            self.category_num = 8
        if zone == "次の予想も頑張ります！！byユーロ":
            self.category_num = 9
        if zone == "ラストスパート！！ｂｙユーロ":
            self.category_num = 4

    def return_will_hour(self, zone):
        if zone == "今日もがんばります！！ｂｙユーロ":
            return self.fxtecunikaruyuro1_will_hour
        if zone == "次の予想も頑張ります！！byユーロ":
            return self.fxtecunikaruyuro2_will_hour
        if zone == "ラストスパート！！ｂｙユーロ":
            return self.fxtecunikaruyuro3_will_hour

    def return_will_minute(self, zone):
        if zone == "今日もがんばります！！ｂｙユーロ":
            return self.fxtecunikaruyuro1_will_minute
        if zone == "次の予想も頑張ります！！byユーロ":
            return self.fxtecunikaruyuro2_will_minute
        if zone == "ラストスパート！！ｂｙユーロ":
            return self.fxtecunikaruyuro3_will_minute

    def get_time(self, zone):
        if zone == "今日もがんばります！！ｂｙユーロ":
            self.buy_time = "09:00"
            self.settlement_time = "y08:30"
        if zone == "次の予想も頑張ります！！byユーロ":
            self.buy_time = "16:00"
            self.settlement_time = "y15:30"
        if zone == "ラストスパート！！ｂｙユーロ":
            self.buy_time = "22:00"
            self.settlement_time = "y08:30"

    def get_total_file(self, zone):
        if zone == "今日もがんばります！！ｂｙユーロ":
            self.main_total = open(
                'other_txt/fxtecunikaruyuro/fxtecunikaruyuro_fxtecunikaruyuro1_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(
                self.main_total)
        if zone == "次の予想も頑張ります！！byユーロ":
            self.main_total = open(
                'other_txt/fxtecunikaruyuro/fxtecunikaruyuro_fxtecunikaruyuro2_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(
                self.main_total)
        if zone == "ラストスパート！！ｂｙユーロ":
            self.main_total = open(
                'other_txt/fxtecunikaruyuro/fxtecunikaruyuro_fxtecunikaruyuro3_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(
                self.main_total)

    def get_main_sign(self, zone):
        self.zone_euro = CONFIG.fx_zone_euro(self.buy_time)
        if CONFIG.fxtecunikaruyuro_main_buy_result(zone) == "売り":
            self.zone_settlement = float(Decimal(str(CONFIG.fx_zone_euro(
                self.settlement_time)+0.005)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.main_sign = float(Decimal(str(self.zone_euro - self.zone_settlement)
                                           ).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        if CONFIG.fxtecunikaruyuro_main_buy_result(zone) == "買い":
            self.zone_euro = float(Decimal(
                str(self.zone_euro+0.005)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.zone_settlement = CONFIG.fx_zone_euro(self.settlement_time)
            self.main_sign = float(Decimal(str(self.zone_settlement - self.zone_euro)
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
        if zone == "今日もがんばります！！ｂｙユーロ":
            open('other_txt/fxtecunikaruyuro/fxtecunikaruyuro_fxtecunikaruyuro1_main_total.txt',
                 'w').write(str(self.main_total))
        if zone == "次の予想も頑張ります！！byユーロ":
            open('other_txt/fxtecunikaruyuro/fxtecunikaruyuro_fxtecunikaruyuro2_main_total.txt',
                 'w').write(str(self.main_total))
        if zone == "ラストスパート！！ｂｙユーロ":
            open('other_txt/fxtecunikaruyuro/fxtecunikaruyuro_fxtecunikaruyuro3_main_total.txt',
                 'w').write(str(self.main_total))

    def __init__(self, driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.fxtecunikaruyuro1_will_hour = "8"
        self.fxtecunikaruyuro2_will_hour = "15"
        self.fxtecunikaruyuro3_will_hour = "21"

        self.fxtecunikaruyuro1_will_minute = "45"
        self.fxtecunikaruyuro2_will_minute = "45"
        self.fxtecunikaruyuro3_will_minute = "45"

        self.will_second = "00"

    def automation(self, num):
        print("fxテクニカルユーロ")
        if num == 1:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "今日もがんばります！！ｂｙユーロ"
            print(zone)

            self.get_category_num(zone)

            self.get_time(zone)
            self.get_total_file(zone)
            self.get_main_sign(zone)

            self.get_main_total()

            fxtecunikaruyuro_text = FxtecunikaruyuroText(zone, CONFIG.fxtecunikaruyuro_main_buy_result(
                zone), self.main_sign, self.main_total, self.zone_euro, self.zone_settlement, self.buy_time, self.settlement_time)
            self.blog_post(self.category_num, fxtecunikaruyuro_text, zone,
                           self.will_year, self.will_month, self.will_day, self.will_second)
            self.save_total_file(zone)

        if num == 2:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "次の予想も頑張ります！！byユーロ"
            print(zone)

            self.get_category_num(zone)

            self.get_time(zone)
            self.get_total_file(zone)
            self.get_main_sign(zone)

            self.get_main_total()

            fxtecunikaruyuro_text = FxtecunikaruyuroText(zone, CONFIG.fxtecunikaruyuro_main_buy_result(
                zone), self.main_sign, self.main_total, self.zone_euro, self.zone_settlement, self.buy_time, self.settlement_time)
            self.blog_post(self.category_num, fxtecunikaruyuro_text, zone,
                           self.will_year, self.will_month, self.will_day, self.will_second)
            self.save_total_file(zone)
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "ラストスパート！！ｂｙユーロ"
            print(zone)

            self.get_category_num(zone)

            self.get_time(zone)
            self.get_total_file(zone)
            self.get_main_sign(zone)
            self.get_main_total()

            fxtecunikaruyuro_text = FxtecunikaruyuroText(zone, CONFIG.fxtecunikaruyuro_main_buy_result(
                zone), self.main_sign, self.main_total, self.zone_euro, self.zone_settlement, self.buy_time, self.settlement_time)
            self.blog_post(self.category_num, fxtecunikaruyuro_text, zone,
                           self.will_year, self.will_month, self.will_day, self.will_second)
            self.save_total_file(zone)
