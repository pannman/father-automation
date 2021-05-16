from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.fxtoshinikki_text_config import FxtoshinikkiText
from .fc2 import Fc2
from decimal import Decimal, ROUND_HALF_UP
import datetime


class Fxtoshinikki(Fc2):
    def login_id(self):
        return LOGIN.FXTOSHINIKKI_LOGIN['ID']

    def login_pass(self):
        return LOGIN.FXTOSHINIKKI_LOGIN['PASS']

    def get_category_num(self,zone):
        if zone == "FX投資日記1":
            self.category_num = 0
        if zone == "FX投資日記2":
            self.category_num = 0
    
    def return_will_hour(self,zone):
        if zone == "FX投資日記1":
            return self.fxtoshinikki1_will_hour
        if zone == "FX投資日記2":
            return self.fxtoshinikki2_will_hour


    def return_will_minute(self,zone):
        if zone == "FX投資日記1":
            return self.fxtoshinikki1_will_minute
        if zone == "FX投資日記2":
            return self.fxtoshinikki2_will_minute


    def get_time(self,zone):
        if zone == "FX投資日記1":
            self.buy_time = "09:00"
            self.settlement_time = "16:30"
        if zone == "FX投資日記2":
            self.buy_time = "16:30"
            self.settlement_time = "y09:00"

    def get_total_file(self,zone):
        if zone == "FX投資日記1":
            self.main_total = open('other_txt/fxtoshinikki/fxtoshinikki_fxtoshinikki1_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(self.main_total)
        if zone == "FX投資日記2":
            self.main_total = open('other_txt/fxtoshinikki/fxtoshinikki_fxtoshinikki2_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(self.main_total)

    def get_main_sign(self,zone):
        self.zone_dollar = CONFIG.fx_zone_dollar(self.buy_time)
        if CONFIG.fxtoshinikki_main_buy_result(zone) == "売り":
            self.zone_settlement = float(Decimal(str(CONFIG.fx_zone_dollar(self.settlement_time)+0.002)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
        if CONFIG.fxtoshinikki_main_buy_result(zone) == "買い":
            self.zone_dollar = float(Decimal(str(self.zone_dollar+0.02)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
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
        if zone == "FX投資日記1":
            fxtoshinikki2_main_total = open('other_txt/fxtoshinikki/fxtoshinikki_fxtoshinikki2_main_total.txt', 'r').read()
            self.all_main_total = float(Decimal(float(self.main_total) + float(fxtoshinikki2_main_total)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
        if zone == "FX投資日記2":
            fxtoshinikki1_main_total = open('other_txt/fxtoshinikki/fxtoshinikki_fxtoshinikki1_main_total.txt', 'r').read()
            self.all_main_total = float(Decimal(float(self.main_total) + float(fxtoshinikki1_main_total)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
        self.all_main_total = "+" + str(self.all_main_total) if self.all_main_total > 0 else "±0" if self.all_main_total == 0 else str(self.all_main_total)
    
    def save_total_file(self,zone):
        if zone == "FX投資日記1":
            open('other_txt/fxtoshinikki/fxtoshinikki_fxtoshinikki1_main_total.txt', 'w').write(str(self.main_total))
        if zone == "FX投資日記2":
            open('other_txt/fxtoshinikki/fxtoshinikki_fxtoshinikki2_main_total.txt', 'w').write(str(self.main_total))
            
    def __init__(self,driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()  
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.fxtoshinikki1_will_hour = "7"
        self.fxtoshinikki2_will_hour = "16"

        self.fxtoshinikki1_will_minute = "05"
        self.fxtoshinikki2_will_minute = "05"

        self.will_second = "00"


    
    def automation(self,num):
        print("FX投資日記")
        if num == 5:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "FX投資日記1"
            print(zone)

            self.get_category_num(zone)

            self.get_time(zone)
            self.get_total_file(zone)
            self.get_main_sign(zone)

            self.get_main_total()
            self.get_all_main_total(zone)

            fxtoshinikki_text = FxtoshinikkiText(zone,CONFIG.fxtoshinikki_main_buy_result(zone),self.main_sign,self.main_total,self.zone_dollar,self.zone_settlement,self.buy_time,self.settlement_time)
            self.blog_post(self.category_num,fxtoshinikki_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)

        if num == 9:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "FX投資日記2"
            print(zone)

            self.get_category_num(zone)

            self.get_time(zone)
            self.get_total_file(zone)
            self.get_main_sign(zone)

            self.get_main_total()
            self.get_all_main_total(zone)

            fxtoshinikki_text = FxtoshinikkiText(zone,CONFIG.fxtoshinikki_main_buy_result(zone),self.main_sign,self.main_total,self.zone_dollar,self.zone_settlement,self.buy_time,self.settlement_time)
            self.blog_post(self.category_num,fxtoshinikki_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)