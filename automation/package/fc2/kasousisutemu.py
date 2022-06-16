from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.kasousisutemu_text_config import KasousisutemuText
from .fc2 import Fc2
from decimal import Decimal, ROUND_HALF_UP
import datetime


class Kasousisutemu(Fc2):
    def login_id(self):
        return LOGIN.KASOUSISUTEMU_LOGIN['ID']

    def login_pass(self):
        return LOGIN.KASOUSISUTEMU_LOGIN['PASS']

    def get_category_num(self,zone):
        if zone == "9：00　→　21：00":
            self.category_num = 0
        if zone == "21：00　→　09：00":
            self.category_num = 0
    
    def return_will_hour(self,zone):
        if zone == "9：00　→　21：00":
            return self.kasousisutemu1_will_hour
        if zone == "21：00　→　09：00":
            return self.kasousisutemu2_will_hour


    def return_will_minute(self,zone):
        if zone == "9：00　→　21：00":
            return self.kasousisutemu1_will_minute
        if zone == "21：00　→　09：00":
            return self.kasousisutemu2_will_minute


    def get_time(self,zone):
        if zone == "9：00　→　21：00":
            self.buy_time = "09:00"
            self.settlement_time = "21:00"
        if zone == "21：00　→　09：00":
            self.buy_time = "21:00"
            self.settlement_time = "y09:00"

    def get_total_file(self,zone):
        if zone == "9：00　→　21：00":
            self.main_total = open('other_txt/kasousisutemu/kasousisutemu_kasousisutemu1_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "21：00　→　09：00":
            self.main_total = open('other_txt/kasousisutemu/kasousisutemu_kasousisutemu2_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)

    def get_main_sign(self,zone):
        self.zone_bit = CONFIG.kasou_bit_en(self.buy_time)
        if CONFIG.kasousisutemu_main_buy_result(zone) == "売り":
            self.zone_settlement = int(CONFIG.kasou_bit_en(self.settlement_time))
            self.main_sign = self.zone_bit - self.zone_settlement
        if CONFIG.kasousisutemu_main_buy_result(zone) == "買い":
            self.zone_bit = int(self.zone_bit)
            self.zone_settlement = CONFIG.kasou_bit_en(self.settlement_time)
            self.main_sign = self.zone_settlement - self.zone_bit
        self.main_sign = "+" + str(self.main_sign) if self.main_sign > 0 else "±0" if self.main_sign == 0 else str(self.main_sign)

    def get_main_total(self):
        if self.main_sign == "±0":
            self.main_sign = "0"
        self.main_total = self.main_total + int(self.main_sign)
        self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±0" if self.main_total == 0 else str(self.main_total)

    def get_all_main_total(self,zone):
        if self.main_total == "±0":
            self.main_total = "0"
        if zone == "9：00　→　21：00":
            kasousisutemu2_main_total = open('other_txt/kasousisutemu/kasousisutemu_kasousisutemu2_main_total.txt', 'r').read()
            self.all_main_total = int(self.main_total) + int(kasousisutemu2_main_total)
        if zone == "21：00　→　09：00":
            kasousisutemu1_main_total = open('other_txt/kasousisutemu/kasousisutemu_kasousisutemu1_main_total.txt', 'r').read()
            self.all_main_total = int(self.main_total) + int(kasousisutemu1_main_total)
        self.all_main_total = "+" + str(self.all_main_total) if self.all_main_total > 0 else "±0" if self.all_main_total == 0 else str(self.all_main_total)
    
    def save_total_file(self,zone):
        if zone == "9：00　→　21：00":
            open('other_txt/kasousisutemu/kasousisutemu_kasousisutemu1_main_total.txt', 'w').write(str(self.main_total))
        if zone == "21：00　→　09：00":
            open('other_txt/kasousisutemu/kasousisutemu_kasousisutemu2_main_total.txt', 'w').write(str(self.main_total))
            
    def __init__(self,driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()  
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.kasousisutemu1_will_hour = "7"
        self.kasousisutemu2_will_hour = "20"

        self.kasousisutemu1_will_minute = "45"
        self.kasousisutemu2_will_minute = "15"

        self.will_second = "00"


    
    def automation(self,num):
        print("仮想システム")
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "9：00　→　21：00"
            print(zone)
            self.get_category_num(zone)

            self.get_time(zone)
            self.get_total_file(zone)
            self.get_main_sign(zone)

            self.get_main_total()
            self.get_all_main_total(zone)

            kasousisutemu_text = KasousisutemuText(zone,CONFIG.kasousisutemu_main_buy_result(zone),self.main_sign,self.main_total,self.zone_bit,self.zone_settlement,self.buy_time,self.settlement_time)
            self.blog_post(self.category_num,kasousisutemu_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)

        if num == 9:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "21：00　→　09：00"
            print(zone)

            self.get_category_num(zone)

            self.get_time(zone)
            self.get_total_file(zone)
            self.get_main_sign(zone)

            self.get_main_total()
            self.get_all_main_total(zone)

            kasousisutemu_text = KasousisutemuText(zone,CONFIG.kasousisutemu_main_buy_result(zone),self.main_sign,self.main_total,self.zone_bit,self.zone_settlement,self.buy_time,self.settlement_time)
            self.blog_post(self.category_num,kasousisutemu_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)