from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.habatakefx_text_config import HabatakefxText
from .fc2 import Fc2
from decimal import Decimal, ROUND_HALF_UP
import datetime


class Habatakefx(Fc2):
    def login_id(self):
        return LOGIN.HABATAKEFX_LOGIN['ID']

    def login_pass(self):
        return LOGIN.HABATAKEFX_LOGIN['PASS']

    def get_category_num(self, zone):
        if zone == "09：00→21：00":
            self.category_num = 0
        if zone == "21：00→09：00":
            self.category_num = 0

    def return_will_hour(self, zone):
        if zone == "09：00→21：00":
            return self.habatakefx1_will_hour
        if zone == "21：00→09：00":
            return self.habatakefx2_will_hour

    def return_will_minute(self, zone):
        if zone == "09：00→21：00":
            return self.habatakefx1_will_minute
        if zone == "21：00→09：00":
            return self.habatakefx2_will_minute

    def get_time(self, zone):
        if zone == "09：00→21：00":
            self.buy_time = "09:00"
            self.settlement_time = "21:00"
        if zone == "21：00→09：00":
            self.buy_time = "21:00"
            self.settlement_time = "y09:00"

    def get_total_file(self, zone):
        if zone == "09：00→21：00":
            self.main_total = open(
                'other_txt/habatakefx/habatakefx_habatakefx1_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(
                self.main_total)
            self.main_total_euro = open(
                'other_txt/habatakefx/habatakefx_habatakefx1_main_total_euro.txt', 'r').read()
            self.main_total_euro = 0 if self.main_total_euro == "±0" else float(
                self.main_total_euro)
            self.main_total_lb = open(
                'other_txt/habatakefx/habatakefx_habatakefx1_main_total_lb.txt', 'r').read()
            self.main_total_lb = 0 if self.main_total_lb == "±0" else float(
                self.main_total_lb)
        if zone == "21：00→09：00":
            self.main_total = open(
                'other_txt/habatakefx/habatakefx_habatakefx2_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(
                self.main_total)

            self.main_total_euro = open(
                'other_txt/habatakefx/habatakefx_habatakefx2_main_total_euro.txt', 'r').read()
            self.main_total_euro = 0 if self.main_total_euro == "±0" else float(
                self.main_total_euro)
 

            self.main_total_lb = open(
                'other_txt/habatakefx/habatakefx_habatakefx2_main_total_lb.txt', 'r').read()
            self.main_total_lb = 0 if self.main_total_lb == "±0" else float(
                self.main_total_lb)


    def get_main_sign(self, zone):
        self.zone_dollar = CONFIG.fx_zone_dollar(self.buy_time)
        self.zone_euro = CONFIG.fx_zone_euro(self.buy_time)
        self.zone_lb = CONFIG.fx_zone_lb(self.buy_time)
        self.zone_state, self.zone_state_euro, self.zone_state_lb = CONFIG.habatakefx_main_buy_result(
            zone)
        print(self.zone_dollar,self.zone_euro,self.zone_lb,self.zone_state, self.zone_state_euro, self.zone_state_lb)
        if self.zone_state == "売り":
            #ポンドユーロごとに売りか買い換えているのかan毎回一緒、ASKは買いBID売り、ポンドは0.01ユーロは0．005計算方法
            self.zone_settlement = float(Decimal(str(CONFIG.fx_zone_dollar(
                self.settlement_time)+0.002)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.main_sign = float(Decimal(str(self.zone_dollar - self.zone_settlement)
                                           ).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        if self.zone_state == "買い":
            self.zone_dollar = float(Decimal(
                str(self.zone_dollar+0.002)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.zone_settlement = CONFIG.fx_zone_dollar(self.settlement_time)
            self.main_sign = float(Decimal(str(self.zone_settlement - self.zone_dollar)
                                           ).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
            print(111)

        if self.zone_state_euro == "売り":

            #ポンドユーロごとに売りか買い換えているのかan毎回一緒、ASKは買いBID売り、ポンドは0.01ユーロは0．005計算方法
            self.zone_settlement_euro = float(Decimal(str(CONFIG.fx_zone_euro(
                self.settlement_time)+0.005)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.main_sign_euro = float(Decimal(str(
                self.zone_euro - self.zone_settlement_euro)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        if self.zone_state_euro == "買い":
            self.zone_euro = float(Decimal(
                str(self.zone_euro+0.005)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.zone_settlement_euro = CONFIG.fx_zone_euro(
                self.settlement_time)
            print(self.settlement_time)
            print(self.zone_settlement_euro)
            self.main_sign_euro = float(Decimal(str(
                self.zone_settlement_euro - self.zone_euro)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
            print(111)

        if self.zone_state_lb == "売り":
            #ポンドユーロごとに売りか買い換えているのかan毎回一緒、ASKは買いBID売り、ポンドは0.01ユーロは0．005計算方法
            self.zone_settlement_lb = float(Decimal(str(CONFIG.fx_zone_lb(
                self.settlement_time)+0.01)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.main_sign_lb = float(Decimal(str(
                self.zone_lb - self.zone_settlement_lb)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        if self.zone_state_lb == "買い":
            self.zone_lb = float(Decimal(
                str(self.zone_lb+0.01)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.zone_settlement_lb = CONFIG.fx_zone_lb(self.settlement_time)
            self.main_sign_lb = float(Decimal(str(
                self.zone_settlement_lb - self.zone_lb)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
            print(111)
        self.main_sign = "+" + \
            str(self.main_sign) if self.main_sign > 0 else "±0" if self.main_sign == 0 else str(
                self.main_sign)
        self.main_sign_euro = "+" + \
            str(self.main_sign_euro) if self.main_sign_euro > 0 else "±0" if self.main_sign_euro == 0 else str(
                self.main_sign_euro)
        self.main_sign_lb = "+" + \
            str(self.main_sign_lb) if self.main_sign_lb > 0 else "±0" if self.main_sign_lb == 0 else str(
                self.main_sign_lb)

    def get_main_total(self):
        if self.main_sign == "±0":
            self.main_sign = "0"
        self.main_total = Decimal(str(self.main_total + float(self.main_sign))
                                  ).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        self.main_total = "+" + \
            str(self.main_total) if self.main_total > 0 else "±0" if self.main_total == 0 else str(
                self.main_total)

    def get_main_total_euro(self):
        if self.main_sign_euro == "±0":
            self.main_sign_euro = "0"
        self.main_total_euro = Decimal(str(self.main_total_euro + float(
            self.main_sign_euro))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        self.main_total_euro = "+" + \
            str(self.main_total_euro) if self.main_total_euro > 0 else "±0" if self.main_total_euro == 0 else str(
                self.main_total_euro)

    def get_main_total_lb(self):
        if self.main_sign_lb == "±0":
            self.main_sign_lb = "0"
        self.main_total_lb = Decimal(str(self.main_total_lb + float(
            self.main_sign_lb))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        self.main_total_lb = "+" + \
            str(self.main_total_lb) if self.main_total_lb > 0 else "±0" if self.main_total_lb == 0 else str(
                self.main_total_lb)



    def save_total_file(self, zone):
        if zone == "09：00→21：00":
            open('other_txt/habatakefx/habatakefx_habatakefx1_main_total.txt',
                 'w').write(str(self.main_total))
            open('other_txt/habatakefx/habatakefx_habatakefx1_main_total_euro.txt',
                 'w').write(str(self.main_total_euro))
            open('other_txt/habatakefx/habatakefx_habatakefx1_main_total_lb.txt',
                 'w').write(str(self.main_total_lb))
        if zone == "21：00→09：00":
            open('other_txt/habatakefx/habatakefx_habatakefx2_main_total.txt',
                 'w').write(str(self.main_total))
            open('other_txt/habatakefx/habatakefx_habatakefx2_main_total_euro.txt',
                 'w').write(str(self.main_total_euro))
            open('other_txt/habatakefx/habatakefx_habatakefx2_main_total_lb.txt',
                 'w').write(str(self.main_total_lb))
    
    def __init__(self, driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.habatakefx1_will_hour = "7"
        self.habatakefx2_will_hour = "20"

        self.habatakefx1_will_minute = "15"
        self.habatakefx2_will_minute = "45"

        self.will_second = "00"

    def automation(self, num):
        print("はばたけfx")
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "09：00→21：00"
            print(zone)

            self.get_category_num(zone)
            print(zone)
            self.get_time(zone)
            print(zone)
            self.get_total_file(zone)
            print(zone)
            self.get_main_sign(zone)
            print(zone)

            self.get_main_total()
            self.get_main_total_euro()
            self.get_main_total_lb()
            # self.get_all_main_total(zone)


            habatakefx_text = HabatakefxText(zone, self.zone_state, self.zone_state_euro, self.zone_state_lb, self.main_sign, self.main_sign_euro, self.main_sign_lb, self.main_total, self.main_total_euro, self.main_total_lb, self.zone_dollar, self.zone_euro, self.zone_lb, self.zone_settlement,
                                         self.zone_settlement_euro, self.zone_settlement_lb, self.buy_time, self.settlement_time)
            self.blog_post(self.category_num, habatakefx_text, zone,
                           self.will_year, self.will_month, self.will_day, self.will_second)
            self.save_total_file(zone)

        if num == 9:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "21：00→09：00"
            print(zone)

            self.get_category_num(zone)

            self.get_time(zone)
            self.get_total_file(zone)
            self.get_main_sign(zone)

            self.get_main_total()
            self.get_main_total_euro()
            self.get_main_total_lb()
            # self.get_all_main_total(zone)


            habatakefx_text = HabatakefxText(zone, self.zone_state, self.zone_state_euro, self.zone_state_lb, self.main_sign, self.main_sign_euro, self.main_sign_lb, self.main_total, self.main_total_euro, self.main_total_lb, self.zone_dollar, self.zone_euro, self.zone_lb, self.zone_settlement,
                                         self.zone_settlement_euro, self.zone_settlement_lb, self.buy_time, self.settlement_time)
            self.blog_post(self.category_num, habatakefx_text, zone,
                           self.will_year, self.will_month, self.will_day, self.will_second)
            self.save_total_file(zone)


#実行からあああああああああああああ
