from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.sararimanfx_text_config import SararimanfxText
from .fc2 import Fc2
from decimal import Decimal, ROUND_HALF_UP
import datetime


class Sararimanfx(Fc2):
    def login_id(self):
        return LOGIN.SARARIMANFX_LOGIN['ID']

    def login_pass(self):
        return LOGIN.SARARIMANFX_LOGIN['PASS']

    def get_category_num(self,zone):
        if zone == "シグナルA":
            self.category_num = 1
        if zone == "シグナルB":
            self.category_num = 3
        if zone == "シグナルC":
            self.category_num = 4

    
    def return_will_hour(self,zone):
        if zone == "シグナルA":
            return self.signalA_will_hour
        if zone == "シグナルB":
            return self.signalB_will_hour
        if zone == "シグナルC":
            return self.signalC_will_hour


    def return_will_minute(self,zone):
        if zone == "シグナルA":
            return self.signalA_will_minute
        if zone == "シグナルB":
            return self.signalB_will_minute
        if zone == "シグナルC":
            return self.signalC_will_minute


    def get_time(self,zone):
        if zone == "シグナルA":
            self.buy_time = "08:00"
            self.settlement_time = "15:30"
        if zone == "シグナルB":
            self.buy_time = "16:30"
            self.settlement_time = "20:00"
        if zone == "シグナルC":
            self.buy_time = "21:00"
            self.settlement_time = "y07:00"

    def get_total_file(self,zone):
        if zone == "シグナルA":
            self.main_total = open('other_txt/sararimanfx/sararimanfx_signalA_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(self.main_total)
        if zone == "シグナルB":
            self.main_total = open('other_txt/sararimanfx/sararimanfx_signalB_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(self.main_total)
        if zone == "シグナルC":
            self.main_total = open('other_txt/sararimanfx/sararimanfx_signalC_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(self.main_total)
    
    def get_other_total_file(self,zone):
        self.signalA_main_total = open('other_txt/sararimanfx/sararimanfx_signalA_main_total.txt', 'r').read()
        self.signalB_main_total = open('other_txt/sararimanfx/sararimanfx_signalB_main_total.txt', 'r').read()
        self.signalC_main_total = open('other_txt/sararimanfx/sararimanfx_signalC_main_total.txt', 'r').read()
        if zone == "シグナルA":
            self.signalA_main_total = self.main_total
        if zone == "シグナルB":
            self.signalB_main_total = self.main_total
        if zone == "シグナルC":
            self.signalC_main_total = self.main_total

    def get_main_sign(self,zone):
        self.zone_dollar = CONFIG.fx_zone_dollar(self.buy_time)
        if CONFIG.sararimanfx_main_buy_result(zone) == "売り":
            self.zone_settlement = float(Decimal(str(CONFIG.fx_zone_dollar(self.settlement_time)+0.002)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.main_sign = float(Decimal(str(self.zone_dollar - self.zone_settlement)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        if CONFIG.sararimanfx_main_buy_result(zone) == "買い":
            self.zone_dollar = float(Decimal(str(self.zone_dollar+0.002)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.zone_settlement = CONFIG.fx_zone_dollar(self.settlement_time)
            self.main_sign = float(Decimal(str(self.zone_settlement - self.zone_dollar)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        self.main_sign = "+" + str(self.main_sign) if self.main_sign > 0 else "±0" if self.main_sign == 0 else str(self.main_sign)

    def get_main_total(self):
        if self.main_sign == "±0":
            self.main_sign = "0"
        self.main_total = Decimal(str(self.main_total + float(self.main_sign))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±0" if self.main_total == 0 else str(self.main_total)

    
    
    def save_total_file(self,zone):
        if zone == "シグナルA":
            open('other_txt/sararimanfx/sararimanfx_signalA_main_total.txt', 'w').write(str(self.main_total))
        if zone == "シグナルB":
            open('other_txt/sararimanfx/sararimanfx_signalB_main_total.txt', 'w').write(str(self.main_total))
        if zone == "シグナルC":
            open('other_txt/sararimanfx/sararimanfx_signalC_main_total.txt', 'w').write(str(self.main_total))
            
    def __init__(self,driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()  
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.signalA_will_hour = "7"
        self.signalB_will_hour = "16"
        self.signalC_will_hour = "20"

        self.signalA_will_minute = "35"
        self.signalB_will_minute = "30"
        self.signalC_will_minute = "35"

        self.will_second = "00"


    
    def automation(self,num):
        print("サラリーマンの副業に最適なＦＸ投資")
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "シグナルA"
            print(zone)

            self.get_category_num(zone)

            self.get_time(zone)
            self.get_total_file(zone)
            self.get_main_sign(zone)

            self.get_main_total()
            self.get_other_total_file(zone)

            sararimanfx_text = SararimanfxText(zone,CONFIG.sararimanfx_main_buy_result(zone),self.main_sign,self.main_total,self.zone_dollar,self.zone_settlement,self.buy_time,self.settlement_time,self.signalA_main_total,self.signalB_main_total,self.signalC_main_total)
            self.blog_post(self.category_num,sararimanfx_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)

        if num == 9:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zones = ["シグナルB","シグナルC"]
            for zone in zones:
                print(zone)

                self.get_category_num(zone)
                
                self.get_time(zone)
                self.get_total_file(zone)
                self.get_main_sign(zone)

                self.get_main_total()
                self.get_other_total_file(zone)

                sararimanfx_text = SararimanfxText(zone,CONFIG.sararimanfx_main_buy_result(zone),self.main_sign,self.main_total,self.zone_dollar,self.zone_settlement,self.buy_time,self.settlement_time,self.signalA_main_total,self.signalB_main_total,self.signalC_main_total)
                self.blog_post(self.category_num,sararimanfx_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
                self.save_total_file(zone)