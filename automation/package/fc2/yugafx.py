from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.yugafx_text_config import YugafxText
from .fc2 import Fc2
from decimal import Decimal, ROUND_HALF_UP
import datetime

# 朝９時

class Yugafx(Fc2):
    def login_id(self):
        return LOGIN.YUGAFX_LOGIN['ID']

    def login_pass(self):
        return LOGIN.YUGAFX_LOGIN['PASS']

    def get_category_num(self):
        self.category_num = 0

    def return_will_hour(self,zone):
        return self.yugafx_will_hour

    def return_will_minute(self,zone):
        return self.yugafx_will_minute

    def get_time(self, zone):
        if zone == "08：00（成行売買）～20：00（成行決済）":
            self.buy_time = "09:00"
            self.settlement_time = "16:30"
        if zone == "20：30（成行売買）～07：30（成行決済）":
            self.buy_time = "16:30"
            self.settlement_time = "y09:00"

    def get_total_file(self, zone):
        if zone == "08：00（成行売買）～20：00（成行決済）":
            self.main_total = open(
                'other_txt/yugafx/yugafx_yugafx1_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(
                self.main_total)
            self.main_total_euro = open(
                'other_txt/yugafx/yugafx_yugafx1_main_total_euro.txt', 'r').read()
            self.main_total_euro = 0 if self.main_total_euro == "±0" else float(
                self.main_total_euro)
            self.main_total_lb = open(
                'other_txt/yugafx/yugafx_yugafx1_main_total_lb.txt', 'r').read()
            self.main_total_lb = 0 if self.main_total_lb == "±0" else float(
                self.main_total_lb)
            self.main_total_euro_dol = open(
                'other_txt/yugafx/yugafx_yugafx1_main_total_euro_dol.txt', 'r').read()
            self.main_total_euro_dol = 0 if self.main_total_euro_dol == "±0" else float(
                self.main_total_euro_dol)
            self.main_total_lb_dol = open(
                'other_txt/yugafx/yugafx_yugafx1_main_total_lb_dol.txt', 'r').read()
            self.main_total_lb_dol = 0 if self.main_total_lb_dol == "±0" else float(
                self.main_total_lb_dol)
        if zone == "20：30（成行売買）～07：30（成行決済）":
            self.main_total = open(
                'other_txt/yugafx/yugafx_yugafx2_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(
                self.main_total)

            self.main_total_euro = open(
                'other_txt/yugafx/yugafx_yugafx2_main_total_euro.txt', 'r').read()
            self.main_total_euro = 0 if self.main_total_euro == "±0" else float(
                self.main_total_euro)

            self.main_total_lb = open(
                'other_txt/yugafx/yugafx_yugafx2_main_total_lb.txt', 'r').read()
            self.main_total_lb = 0 if self.main_total_lb == "±0" else float(
                self.main_total_lb)

            self.main_total_euro_dol = open(
                'other_txt/yugafx/yugafx_yugafx1_main_total_euro_dol.txt', 'r').read()
            self.main_total_euro_dol = 0 if self.main_total_euro_dol == "±0" else float(
                self.main_total_euro_dol)

            self.main_total_lb_dol = open(
                'other_txt/yugafx/yugafx_yugafx1_main_total_lb_dol.txt', 'r').read()
            self.main_total_lb_dol = 0 if self.main_total_lb_dol == "±0" else float(
                self.main_total_lb_dol)

    def get_main_sign(self, zone):
        self.zone_dollar = CONFIG.fx_zone_dollar(self.buy_time)
        self.zone_euro = CONFIG.fx_zone_euro(self.buy_time)
        self.zone_lb = CONFIG.fx_zone_lb(self.buy_time)
        self.zone_euro_dol = CONFIG.fx_zone_euro_dol(self.buy_time)
        self.zone_lb_dol = CONFIG.fx_zone_lb_dol(self.buy_time)
        self.zone_state, self.zone_state_euro, self.zone_state_lb, self.zone_state_euro_dol, self.zone_state_lb_dol = CONFIG.yugafx_main_buy_result(
            zone)
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

        if self.zone_state_euro == "売り":
            self.zone_settlement_euro = float(Decimal(str(CONFIG.fx_zone_euro(
                self.settlement_time)+0.005)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.main_sign_euro = float(Decimal(str(
                self.zone_euro - self.zone_settlement_euro)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        if self.zone_state_euro == "買い":
            self.zone_euro = float(Decimal(
                str(self.zone_euro+0.005)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.zone_settlement_euro = CONFIG.fx_zone_euro(
                self.settlement_time)
            self.main_sign_euro = float(Decimal(str(
                self.zone_settlement_euro - self.zone_euro)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100

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

        if self.zone_state_euro_dol == "売り":
            self.zone_settlement_euro_dol = float(Decimal(str(CONFIG.fx_zone_euro_dol(
                self.settlement_time)+0.004)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.main_sign_euro_dol = float(Decimal(str(
                self.zone_euro_dol - self.zone_settlement_euro_dol)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        if self.zone_state_euro_dol == "買い":
            self.zone_euro_dol = float(Decimal(
                str(self.zone_euro_dol+0.004)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.zone_settlement_euro_dol = CONFIG.fx_zone_euro_dol(
                self.settlement_time)
            self.main_sign_euro_dol = float(Decimal(str(
                self.zone_settlement_euro_dol - self.zone_euro_dol)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100

        if self.zone_state_lb_dol == "売り":
            self.zone_settlement_lb_dol = float(Decimal(str(CONFIG.fx_zone_lb_dol(
                self.settlement_time)+0.01)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.main_sign_lb_dol = float(Decimal(str(
                self.zone_lb_dol - self.zone_settlement_lb_dol)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        if self.zone_state_lb_dol == "買い":
            self.zone_lb_dol = float(Decimal(
                str(self.zone_lb_dol+0.01)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.zone_settlement_lb_dol = CONFIG.fx_zone_lb_dol(self.settlement_time)
            self.main_sign_lb_dol = float(Decimal(str(
                self.zone_settlement_lb_dol - self.zone_lb_dol)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100

        self.main_sign = "+" + \
            str(self.main_sign) if self.main_sign > 0 else "±0" if self.main_sign == 0 else str(
                self.main_sign)
        self.main_sign_euro = "+" + \
            str(self.main_sign_euro) if self.main_sign_euro > 0 else "±0" if self.main_sign_euro == 0 else str(
                self.main_sign_euro)
        self.main_sign_lb = "+" + \
            str(self.main_sign_lb) if self.main_sign_lb > 0 else "±0" if self.main_sign_lb == 0 else str(
                self.main_sign_lb)
        self.main_sign_euro_dol = "+" + \
            str(self.main_sign_euro_dol) if self.main_sign_euro_dol > 0 else "±0" if self.main_sign_euro_dol == 0 else str(
                self.main_sign_euro_dol)
        self.main_sign_lb_dol = "+" + \
            str(self.main_sign_lb_dol) if self.main_sign_lb_dol > 0 else "±0" if self.main_sign_lb_dol == 0 else str(
                self.main_sign_lb_dol)

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

    def get_main_total_euro_dol(self):
        if self.main_sign_euro_dol == "±0":
            self.main_sign_euro_dol = "0"
        self.main_total_euro_dol = Decimal(str(self.main_total_euro_dol + float(
            self.main_sign_euro_dol))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        self.main_total_euro_dol = "+" + \
            str(self.main_total_euro_dol) if self.main_total_euro_dol > 0 else "±0" if self.main_total_euro_dol == 0 else str(
                self.main_total_euro_dol)
    
    def get_main_total_lb_dol(self):
        if self.main_sign_lb_dol == "±0":
            self.main_sign_lb_dol = "0"
        self.main_total_lb_dol = Decimal(str(self.main_total_lb_dol + float(
            self.main_sign_lb_dol))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        self.main_total_lb_dol = "+" + \
            str(self.main_total_lb_dol) if self.main_total_lb_dol > 0 else "±0" if self.main_total_lb_dol == 0 else str(
                self.main_total_lb_dol)
        

    def save_total_file(self, zone):
        if zone == "08：00（成行売買）～20：00（成行決済）":
            open('other_txt/yugafx/yugafx_yugafx1_main_total.txt',
                 'w').write(str(self.main_total1))
            open('other_txt/yugafx/yugafx_yugafx1_main_total_euro.txt',
                 'w').write(str(self.main_total_euro1))
            open('other_txt/yugafx/yugafx_yugafx1_main_total_lb.txt',
                 'w').write(str(self.main_total_lb1))
            open('other_txt/yugafx/yugafx_yugafx1_main_total_euro_dol.txt',
                 'w').write(str(self.main_total_euro_dol1))
            open('other_txt/yugafx/yugafx_yugafx1_main_total_lb_dol.txt',
                 'w').write(str(self.main_total_lb_dol1))
        if zone == "20：30（成行売買）～07：30（成行決済）":
            open('other_txt/yugafx/yugafx_yugafx2_main_total.txt',
                 'w').write(str(self.main_total2))
            open('other_txt/yugafx/yugafx_yugafx2_main_total_euro.txt',
                 'w').write(str(self.main_total_euro2))
            open('other_txt/yugafx/yugafx_yugafx2_main_total_lb.txt',
                 'w').write(str(self.main_total_lb2))
            open('other_txt/yugafx/yugafx_yugafx2_main_total_euro_dol.txt',
                 'w').write(str(self.main_total_euro_dol2))
            open('other_txt/yugafx/yugafx_yugafx2_main_total_lb_dol.txt',
                 'w').write(str(self.main_total_lb_dol2))


    def __init__(self, driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.yugafx_will_hour = "7"

        self.yugafx_will_minute = "15"

        self.will_second = "00"

    def automation(self):
        print("ゆうがfx")
        print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
        self.login_fc2()
        zone1 = "08：00（成行売買）～20：00（成行決済）"
        print(zone1)

        self.get_category_num()

        self.get_time(zone1)
        self.get_total_file(zone1)
        self.get_main_sign(zone1)

        self.get_main_total()
        self.get_main_total_euro()
        self.get_main_total_lb()
        self.get_main_total_euro_dol()
        self.get_main_total_lb_dol()
        # self.get_all_main_total(zone1)

        self.zone_state1  = self.zone_state
        self.zone_state_euro1 = self.zone_state_euro
        self.zone_state_lb1 = self.zone_state_lb
        self.zone_state_euro_dol1 = self.zone_state_euro_dol
        self.zone_state_lb_dol1 = self.zone_state_lb_dol
        self.main_sign1 = self.main_sign
        self.main_sign_euro1 = self.main_sign_euro
        self.main_sign_lb1 = self.main_sign_lb
        self.main_sign_euro_dol1 = self.main_sign_euro_dol
        self.main_sign_lb_dol1 = self.main_sign_lb_dol
        self.main_total1 = self.main_total
        self.main_total_euro1 = self.main_total_euro
        self.main_total_lb1 = self.main_total_lb
        self.main_total_euro_dol1 = self.main_total_euro_dol
        self.main_total_lb_dol1 = self.main_total_lb_dol
        self.zone_dollar1 = self.zone_dollar
        self.zone_euro1 = self.zone_euro
        self.zone_lb1 = self.zone_lb
        self.zone_euro_dol1 = self.zone_euro_dol
        self.zone_lb_dol1 = self.zone_lb_dol
        self.zone_settlement1 = self.zone_settlement
        self.zone_settlement_euro1 = self.zone_settlement_euro
        self.zone_settlement_lb1 = self.zone_settlement_lb
        self.zone_settlement_euro_dol1 = self.zone_settlement_euro_dol
        self.zone_settlement_lb_dol1 = self.zone_settlement_lb_dol
        self.buy_time1 = self.buy_time
        self.settlement_time1 = self.settlement_time

        zone2 = "20：30（成行売買）～07：30（成行決済）"
        print(zone2)

        self.get_category_num()
        self.get_time(zone2)
        self.get_total_file(zone2)
        self.get_main_sign(zone2)
        self.get_main_total()
        self.get_main_total_euro()
        self.get_main_total_lb()
        self.get_main_total_euro_dol()
        self.get_main_total_lb_dol()

        self.zone_state2 = self.zone_state
        self.zone_state_euro2 = self.zone_state_euro
        self.zone_state_lb2 = self.zone_state_lb
        self.zone_state_euro_dol2 = self.zone_state_euro_dol
        self.zone_state_lb_dol2 = self.zone_state_lb_dol
        self.main_sign2 = self.main_sign
        self.main_sign_euro2 = self.main_sign_euro
        self.main_sign_lb2 = self.main_sign_lb
        self.main_sign_euro_dol2 = self.main_sign_euro_dol
        self.main_sign_lb_dol2 = self.main_sign_lb_dol
        self.main_total2 = self.main_total
        self.main_total_euro2 = self.main_total_euro
        self.main_total_lb2 = self.main_total_lb
        self.main_total_euro_dol2 = self.main_total_euro_dol
        self.main_total_lb_dol2 = self.main_total_lb_dol
        self.zone_dollar2 = self.zone_dollar
        self.zone_euro2 = self.zone_euro
        self.zone_lb2 = self.zone_lb
        self.zone_euro_dol2 = self.zone_euro_dol
        self.zone_lb_dol2 = self.zone_lb_dol
        self.zone_settlement2 = self.zone_settlement
        self.zone_settlement_euro2 = self.zone_settlement_euro
        self.zone_settlement_lb2 = self.zone_settlement_lb
        self.zone_settlement_euro_dol2 = self.zone_settlement_euro_dol
        self.zone_settlement_lb_dol2 = self.zone_settlement_lb_dol
        self.buy_time2 = self.buy_time
        self.settlement_time2 = self.settlement_time
        
        yugafx_text = YugafxText(zone1, self.zone_state1, self.zone_state_euro1, self.zone_state_lb1, self.zone_state_euro_dol1, self.zone_state_lb_dol1, self.main_sign1, self.main_sign_euro1, self.main_sign_lb1, self.main_sign_euro_dol1, self.main_sign_lb_dol1, self.main_total1, self.main_total_euro1, self.main_total_lb1, self.main_total_euro_dol1, self.main_total_lb_dol1, self.zone_dollar1, self.zone_euro1, self.zone_lb1, self.zone_euro_dol1, self.zone_lb_dol1, self.zone_settlement1,
                                    self.zone_settlement_euro1, self.zone_settlement_lb1, self.zone_settlement_euro_dol1, self.zone_settlement_lb_dol1, self.buy_time1, self.settlement_time1, zone2, self.zone_state2, self.zone_state_euro2, self.zone_state_lb2, self.zone_state_euro_dol2, self.zone_state_lb_dol2, self.main_sign2, self.main_sign_euro2, self.main_sign_lb2, self.main_sign_euro_dol2, self.main_sign_lb_dol2, self.main_total2, self.main_total_euro2, self.main_total_lb2, self.main_total_euro_dol2, self.main_total_lb_dol2, self.zone_dollar2, self.zone_euro2, self.zone_lb2, self.zone_euro_dol2, self.zone_lb_dol2, self.zone_settlement2,
                                    self.zone_settlement_euro2, self.zone_settlement_lb2, self.zone_settlement_euro_dol2, self.zone_settlement_lb_dol2, self.buy_time2, self.settlement_time2)
        self.blog_post(self.category_num, yugafx_text, zone1,
                        self.will_year, self.will_month, self.will_day, self.will_second)

        self.save_total_file(zone1)
        self.save_total_file(zone2)

    


