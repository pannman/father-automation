from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.kyoifx_text_config import KyoifxText
from .fc2 import Fc2
from decimal import Decimal, ROUND_HALF_UP
import datetime


class Kyoifx(Fc2):
    def login_id(self):
        return LOGIN.KYOIFX_LOGIN['ID']

    def login_pass(self):
        return LOGIN.KYOIFX_LOGIN['PASS']
    
    def get_category_num(self,zone):
        if zone == "パターン1":
            self.category_num = 1
        if zone == "パターン2":
            self.category_num = 2
        if zone == "パターン3":
            self.category_num = 3
    
    
    def return_will_hour(self,zone):
        if zone == "パターン1":
            return self.pattern1_will_hour
        if zone == "パターン2":
            return self.pattern2_will_hour
        if zone == "パターン3":
            return self.pattern3_will_hour


    def return_will_minute(self,zone):
        if zone == "パターン1":
            return self.pattern1_will_minute
        if zone == "パターン2":
            return self.pattern2_will_minute
        if zone == "パターン3":
            return self.pattern3_will_minute


    def get_time(self,zone):
        if zone == "パターン1":
            self.buy_time = "09:00"
            self.settlement_time = "15:00"
        if zone == "パターン2":
            self.buy_time = "16:00"
            self.settlement_time = "20:00"
        if zone == "パターン3":
            self.buy_time = "21:00"
            self.settlement_time = "y07:00"

    def get_total_file(self,zone):
        if zone == "パターン1":
            self.main_total = open('other_txt/kyoifx/kyoifx_pattern1_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(self.main_total)
        if zone == "パターン2":
            self.main_total = open('other_txt/kyoifx/kyoifx_pattern2_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(self.main_total)
        if zone == "パターン3":
            self.main_total = open('other_txt/kyoifx/kyoifx_pattern3_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(self.main_total)

    def get_main_sign(self,zone):
        self.zone_dollar = CONFIG.fx_zone_dollar(self.buy_time)
        if CONFIG.kyoifx_main_buy_result(zone) == "売り":
            self.zone_settlement = float(Decimal(str(CONFIG.fx_zone_dollar(self.settlement_time)+0.002)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.main_sign = float(Decimal(str(self.zone_dollar - self.zone_settlement)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        if CONFIG.kyoifx_main_buy_result(zone) == "買い":
            self.zone_dollar = float(Decimal(str(self.zone_dollar+0.002)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.zone_settlement = CONFIG.fx_zone_dollar(self.settlement_time)
            self.main_sign = float(Decimal(str(self.zone_settlement - self.zone_dollar)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        self.main_sign = "+" + str(self.main_sign) if self.main_sign > 0 else "±0" if self.main_sign == 0 else str(self.main_sign)

    def get_main_total(self):
        if self.main_sign == "±0":
            self.main_sign = "0"
        self.main_total = Decimal(str(self.main_total + float(self.main_sign))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±0" if self.main_total == 0 else str(self.main_total)

    def get_all_main_total(self,zone):
        if self.main_total == "±0":
            self.main_total = "0"
        if zone == "パターン1":
            pattern2_main_total = open('other_txt/kyoifx/kyoifx_pattern2_main_total.txt', 'r').read()
            pattern3_main_total = open('other_txt/kyoifx/kyoifx_pattern3_main_total.txt', 'r').read()
            self.all_main_total = float(Decimal(float(self.main_total) + float(pattern2_main_total) + float(pattern3_main_total)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
        if zone == "パターン2":
            pattern1_main_total = open('other_txt/kyoifx/kyoifx_pattern1_main_total.txt', 'r').read()
            pattern3_main_total = open('other_txt/kyoifx/kyoifx_pattern3_main_total.txt', 'r').read()
            self.all_main_total = float(Decimal(float(self.main_total) + float(pattern1_main_total) + float(pattern3_main_total)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
        if zone == "パターン3":
            pattern1_main_total = open('other_txt/kyoifx/kyoifx_pattern1_main_total.txt', 'r').read()
            pattern2_main_total = open('other_txt/kyoifx/kyoifx_pattern2_main_total.txt', 'r').read()
            self.all_main_total = float(Decimal(float(self.main_total) + float(pattern1_main_total) + float(pattern2_main_total)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
        self.all_main_total = "+" + str(self.all_main_total) if self.all_main_total > 0 else "±0" if self.all_main_total == 0 else str(self.all_main_total)
    
    def save_total_file(self,zone):
        if zone == "パターン1":
            open('other_txt/kyoifx/kyoifx_pattern1_main_total.txt', 'w').write(str(self.main_total))
        if zone == "パターン2":
            open('other_txt/kyoifx/kyoifx_pattern2_main_total.txt', 'w').write(str(self.main_total))
        if zone == "パターン3":
            open('other_txt/kyoifx/kyoifx_pattern3_main_total.txt', 'w').write(str(self.main_total))
            
    def __init__(self,driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()  
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.pattern1_will_hour = "8"
        self.pattern2_will_hour = "15"
        self.pattern3_will_hour = "20"

        self.pattern1_will_minute = "55"
        self.pattern2_will_minute = "55"
        self.pattern3_will_minute = "55"

        self.will_second = "00"


    
    def automation(self,num):
        print("脅威のFXトレード")
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "パターン1"
            print(zone)
            
            self.get_category_num(zone)

            self.get_time(zone)
            self.get_total_file(zone)
            self.get_main_sign(zone)

            self.get_main_total()
            self.get_all_main_total(zone)

            kyoifx_text = KyoifxText(zone,CONFIG.kyoifx_main_buy_result(zone),self.main_sign,self.main_total,self.zone_dollar,self.zone_settlement,self.buy_time,self.settlement_time,self.all_main_total)
            self.blog_post(self.category_num,kyoifx_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)

        if num == 9:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zones = ["パターン2","パターン3"]
            for zone in zones:
                print(zone)

                self.get_category_num(zone)

                self.get_time(zone)
                self.get_total_file(zone)
                self.get_main_sign(zone)

                self.get_main_total()
                self.get_all_main_total(zone)

                kyoifx_text = KyoifxText(zone,CONFIG.kyoifx_main_buy_result(zone),self.main_sign,self.main_total,self.zone_dollar,self.zone_settlement,self.buy_time,self.settlement_time,self.all_main_total)
                self.blog_post(self.category_num,kyoifx_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
                self.save_total_file(zone)