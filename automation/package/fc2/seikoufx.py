from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.seikoufx_text_config import SeikoufxText
from .fc2 import Fc2
from decimal import Decimal, ROUND_HALF_UP
import datetime


class Seikoufx(Fc2):
    def login_id(self):
        return LOGIN.SEIKOUFX_LOGIN['ID']

    def login_pass(self):
        return LOGIN.SEIKOUFX_LOGIN['PASS']

    def get_category_num(self,zone):
        if zone == "09:00成行き売買→16：30成行き決済":
            self.category_num = 0
        if zone == "16:30成行き売買→09：00成行き決済":
            self.category_num = 0
    
    def return_will_hour(self,zone):
        if zone == "09:00成行き売買→16：30成行き決済":
            return self.seikoufx1_will_hour
        if zone == "16:30成行き売買→09：00成行き決済":
            return self.seikoufx2_will_hour


    def return_will_minute(self,zone):
        if zone == "09:00成行き売買→16：30成行き決済":
            return self.seikoufx1_will_minute
        if zone == "16:30成行き売買→09：00成行き決済":
            return self.seikoufx2_will_minute
            


    def get_time(self,zone):
        if zone == "09:00成行き売買→16：30成行き決済":
            self.buy_time = "09:00"
            self.settlement_time = "16:30"
        if zone == "16:30成行き売買→09：00成行き決済":
            self.buy_time = "16:30"
            self.settlement_time = "y09:00"

    def get_total_file(self,zone):
        if zone == "09:00成行き売買→16：30成行き決済":
            self.main_total = open('other_txt/seikoufx/seikoufx_seikoufx1_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(self.main_total)
            self.win_total = open('other_txt/seikoufx/seikoufx_seikoufx1_win_total.txt', 'r').read()
            self.win_total = 0 if self.win_total == "±0" else float(self.win_total)
            self.lose_total = open('other_txt/seikoufx/seikoufx_seikoufx1_lose_total.txt', 'r').read()
            self.lose_total = 0 if self.lose_total == "±0" else float(self.lose_total)
            self.draw_total = open('other_txt/seikoufx/seikoufx_seikoufx1_draw_total.txt', 'r').read()
            self.draw_total = 0 if self.draw_total == "±0" else float(self.draw_total)

            self.main_total_euro = open('other_txt/seikoufx/seikoufx_seikoufx1_main_total_euro.txt', 'r').read()
            self.main_total_euro = 0 if self.main_total_euro == "±0" else float(self.main_total_euro)
            self.win_total_euro = open('other_txt/seikoufx/seikoufx_seikoufx1_win_total_euro.txt', 'r').read()
            self.win_total_euro = 0 if self.win_total_euro == "±0" else float(self.win_total_euro)
            self.lose_total_euro = open('other_txt/seikoufx/seikoufx_seikoufx1_lose_total_euro.txt', 'r').read()
            self.lose_total_euro = 0 if self.lose_total_euro == "±0" else float(self.lose_total_euro)
            self.draw_total_euro = open('other_txt/seikoufx/seikoufx_seikoufx1_draw_total_euro.txt', 'r').read()
            self.draw_total_euro = 0 if self.draw_total_euro == "±0" else float(self.draw_total_euro)

            self.main_total_lb = open('other_txt/seikoufx/seikoufx_seikoufx1_main_total_lb.txt', 'r').read()
            self.main_total_lb = 0 if self.main_total_lb == "±0" else float(self.main_total_lb)
            self.win_total_lb = open('other_txt/seikoufx/seikoufx_seikoufx1_win_total_lb.txt', 'r').read()
            self.win_total_lb = 0 if self.win_total_lb == "±0" else float(self.win_total_lb)
            self.lose_total_lb = open('other_txt/seikoufx/seikoufx_seikoufx1_lose_total_lb.txt', 'r').read()
            self.lose_total_lb = 0 if self.lose_total_lb == "±0" else float(self.lose_total_lb)
            self.draw_total_lb = open('other_txt/seikoufx/seikoufx_seikoufx1_draw_total_lb.txt', 'r').read()
            self.draw_total_lb = 0 if self.draw_total_lb == "±0" else float(self.draw_total_lb)
        if zone == "16:30成行き売買→09：00成行き決済":
            self.main_total = open('other_txt/seikoufx/seikoufx_seikoufx2_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else float(self.main_total)
            self.win_total = open('other_txt/seikoufx/seikoufx_seikoufx2_win_total.txt', 'r').read()
            self.win_total = 0 if self.win_total == "±0" else float(self.win_total)
            self.lose_total = open('other_txt/seikoufx/seikoufx_seikoufx2_lose_total.txt', 'r').read()
            self.lose_total = 0 if self.lose_total == "±0" else float(self.lose_total)
            self.draw_total = open('other_txt/seikoufx/seikoufx_seikoufx2_draw_total.txt', 'r').read()
            self.draw_total = 0 if self.draw_total == "±0" else float(self.draw_total)

            self.main_total_euro = open('other_txt/seikoufx/seikoufx_seikoufx2_main_total_euro.txt', 'r').read()
            self.main_total_euro = 0 if self.main_total_euro == "±0" else float(self.main_total_euro)
            self.win_total_euro = open('other_txt/seikoufx/seikoufx_seikoufx2_win_total_euro.txt', 'r').read()
            self.win_total_euro = 0 if self.win_total_euro == "±0" else float(self.win_total_euro)
            self.lose_total_euro = open('other_txt/seikoufx/seikoufx_seikoufx2_lose_total_euro.txt', 'r').read()
            self.lose_total_euro = 0 if self.lose_total_euro == "±0" else float(self.lose_total_euro)
            self.draw_total_euro = open('other_txt/seikoufx/seikoufx_seikoufx2_draw_total_euro.txt', 'r').read()
            self.draw_total_euro = 0 if self.draw_total_euro == "±0" else float(self.draw_total_euro)

            self.main_total_lb = open('other_txt/seikoufx/seikoufx_seikoufx2_main_total_lb.txt', 'r').read()
            self.main_total_lb = 0 if self.main_total_lb == "±0" else float(self.main_total_lb)
            self.win_total_lb = open('other_txt/seikoufx/seikoufx_seikoufx2_win_total_lb.txt', 'r').read()
            self.win_total_lb = 0 if self.win_total_lb == "±0" else float(self.win_total_lb)
            self.lose_total_lb = open('other_txt/seikoufx/seikoufx_seikoufx2_lose_total_lb.txt', 'r').read()
            self.lose_total_lb = 0 if self.lose_total_lb == "±0" else float(self.lose_total_lb)
            self.draw_total_lb = open('other_txt/seikoufx/seikoufx_seikoufx2_draw_total_lb.txt', 'r').read()
            self.draw_total_lb = 0 if self.draw_total_lb == "±0" else float(self.draw_total_lb)

    def get_main_sign(self,zone):
        self.zone_dollar = CONFIG.fx_zone_dollar(self.buy_time)
        self.zone_euro = CONFIG.fx_zone_euro(self.buy_time)
        self.zone_lb = CONFIG.fx_zone_lb(self.buy_time)
        self.zone_state,self.zone_state_euro,self.zone_state_lb  = CONFIG.seikoufx_main_buy_result(zone)
        if self.zone_state == "売り":
            #ポンドユーロごとに売りか買い換えているのかan毎回一緒、ASKは買いBID売り、ポンドは0.01ユーロは0．005計算方法
            self.zone_settlement = float(Decimal(str(CONFIG.fx_zone_dollar(self.settlement_time)+0.002)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.main_sign = float(Decimal(str(self.zone_dollar - self.zone_settlement)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        if self.zone_state == "買い":
            self.zone_dollar = float(Decimal(str(self.zone_dollar+0.002)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.zone_settlement = CONFIG.fx_zone_dollar(self.settlement_time)
            self.main_sign = float(Decimal(str(self.zone_settlement - self.zone_dollar)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        
        if self.zone_state_euro == "売り":

            #ポンドユーロごとに売りか買い換えているのかan毎回一緒、ASKは買いBID売り、ポンドは0.01ユーロは0．005計算方法
            self.zone_settlement_euro = float(Decimal(str(CONFIG.fx_zone_euro(self.settlement_time)+0.005)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.main_sign_euro = float(Decimal(str(self.zone_euro - self.zone_settlement_euro)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        if self.zone_state_euro == "買い":
            self.zone_euro = float(Decimal(str(self.zone_euro+0.005)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.zone_settlement_euro = CONFIG.fx_zone_euro(self.settlement_time)
            self.main_sign_euro = float(Decimal(str(self.zone_settlement_euro - self.zone_euro)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100

        if self.zone_state_lb == "売り":
            #ポンドユーロごとに売りか買い換えているのかan毎回一緒、ASKは買いBID売り、ポンドは0.01ユーロは0．005計算方法
            self.zone_settlement_lb = float(Decimal(str(CONFIG.fx_zone_lb(self.settlement_time)+0.01)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.main_sign_lb = float(Decimal(str(self.zone_lb - self.zone_settlement_lb)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        if self.zone_state_lb == "買い":
            self.zone_lb = float(Decimal(str(self.zone_lb+0.01)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            self.zone_settlement_lb = CONFIG.fx_zone_lb(self.settlement_time)
            self.main_sign_lb = float(Decimal(str(self.zone_settlement_lb - self.zone_lb)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))*100
        self.main_sign = "+" + str(self.main_sign) if self.main_sign > 0 else "±0" if self.main_sign == 0 else str(self.main_sign)
        self.main_sign_euro = "+" + str(self.main_sign_euro) if self.main_sign_euro > 0 else "±0" if self.main_sign_euro == 0 else str(self.main_sign_euro)
        self.main_sign_lb = "+" + str(self.main_sign_lb) if self.main_sign_lb > 0 else "±0" if self.main_sign_lb == 0 else str(self.main_sign_lb)

    def get_main_total(self):
        if self.main_sign == "±0":
            self.main_sign = "0"
        self.main_total = Decimal(str(self.main_total + float(self.main_sign))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±0" if self.main_total == 0 else str(self.main_total)

    def get_main_total_euro(self):
        if self.main_sign_euro == "±0":
            self.main_sign_euro = "0"
        self.main_total_euro = Decimal(str(self.main_total_euro + float(self.main_sign_euro))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        self.main_total_euro = "+" + str(self.main_total_euro) if self.main_total_euro > 0 else "±0" if self.main_total_euro == 0 else str(self.main_total_euro)

    def get_main_total_lb(self):
        if self.main_sign_lb == "±0":
            self.main_sign_lb = "0"
        self.main_total_lb = Decimal(str(self.main_total_lb + float(self.main_sign_lb))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        self.main_total_lb = "+" + str(self.main_total_lb) if self.main_total_lb > 0 else "±0" if self.main_total_lb == 0 else str(self.main_total_lb)

    def count_win_or_lose_total(self):
        if float(self.main_sign) > 0:
            self.win_total+=1
        if float(self.main_sign) < 0:
            self.lose_total += 1
        if float(self.main_sign) == 0:
            self.draw_total +=1
        if float(self.main_sign_euro) > 0:
            self.win_total_euro += 1
        if float(self.main_sign_euro) < 0:
            self.lose_total_euro += 1
        if float(self.main_sign_euro) == 0:
            self.draw_total_euro += 1
        if float(self.main_sign_lb) > 0:
            self.win_total_lb += 1
        if float(self.main_sign_lb) < 0:
            self.lose_total_lb += 1
        if float(self.main_sign_lb) == 0:
            self.draw_total_lb += 1

    # def get_all_main_total(self,zone):
    #     if self.main_total == "±0":
    #         self.main_total = "0"
    #     if zone == "09:00成行き売買→16：30成行き決済":
    #         seikoufx2_main_total = open('other_txt/seikoufx/seikoufx_seikoufx2_main_total.txt', 'r').read()
    #         self.all_main_total = float(Decimal(float(self.main_total) + float(seikoufx2_main_total)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
    #     if zone == "16:30成行き売買→09：00成行き決済":
    #         seikoufx1_main_total = open('other_txt/seikoufx/seikoufx_seikoufx1_main_total.txt', 'r').read()
    #         self.all_main_total = float(Decimal(float(self.main_total) + float(seikoufx1_main_total)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
    #     self.all_main_total = "+" + str(self.all_main_total) if self.all_main_total > 0 else "±0" if self.all_main_total == 0 else str(self.all_main_total)

    # def get_all_main_total_euro(self,zone):
    #     if self.main_total_euro == "±0":
    #         self.main_total_euro = "0"
    #     if zone == "09:00成行き売買→16：30成行き決済":
    #         seikoufx2_main_total_euro = open('other_txt/seikoufx/seikoufx_seikoufx2_main_total_euro.txt', 'r').read()
    #         self.all_main_total_euro = float(Decimal(float(self.main_total_euro) + float(seikoufx2_main_total_euro)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
    #     if zone == "16:30成行き売買→09：00成行き決済":
    #         seikoufx1_main_total_euro = open('other_txt/seikoufx/seikoufx_seikoufx1_main_total_euro.txt', 'r').read()
    #         self.all_main_total_euro = float(Decimal(float(self.main_total_euro) + float(seikoufx1_main_total_euro)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
    #     self.all_main_total_euro = "+" + str(self.all_main_total_euro) if self.all_main_total_euro > 0 else "±0" if self.all_main_total_euro == 0 else str(self.all_main_total_euro)
    
    # def get_all_main_total_lb(self,zone):
    #     if self.main_total_lb == "±0":
    #         self.main_total_lb = "0"
    #     if zone == "09:00成行き売買→16：30成行き決済":
    #         seikoufx2_main_total_lb = open('other_txt/seikoufx/seikoufx_seikoufx2_main_total_lb.txt', 'r').read()
    #         self.all_main_total_lb = float(Decimal(float(self.main_total_lb) + float(seikoufx2_main_total_lb)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
    #     if zone == "16:30成行き売買→09：00成行き決済":
    #         seikoufx1_main_total_lb = open('other_txt/seikoufx/seikoufx_seikoufx1_main_total_lb.txt', 'r').read()
    #         self.all_main_total_lb = float(Decimal(float(self.main_total_lb) + float(seikoufx1_main_total_lb)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
    #     self.all_main_total_lb = "+" + str(self.all_main_total_lb) if self.all_main_total_lb > 0 else "±0" if self.all_main_total_lb == 0 else str(self.all_main_total_lb)
    
    def save_total_file(self,zone):
        if zone == "09:00成行き売買→16：30成行き決済":
            open('other_txt/seikoufx/seikoufx_seikoufx1_main_total.txt', 'w').write(str(self.main_total))
            open('other_txt/seikoufx/seikoufx_seikoufx1_main_total_euro.txt', 'w').write(str(self.main_total_euro))
            open('other_txt/seikoufx/seikoufx_seikoufx1_main_total_lb.txt', 'w').write(str(self.main_total_lb))
            open('other_txt/seikoufx/seikoufx_seikoufx1_win_total.txt', 'w').write(str(self.win_total))
            open('other_txt/seikoufx/seikoufx_seikoufx1_win_total_euro.txt', 'w').write(str(self.win_total_euro))
            open('other_txt/seikoufx/seikoufx_seikoufx1_win_total_lb.txt', 'w').write(str(self.win_total_lb))
            open('other_txt/seikoufx/seikoufx_seikoufx1_lose_total.txt', 'w').write(str(self.lose_total))
            open('other_txt/seikoufx/seikoufx_seikoufx1_lose_total_euro.txt', 'w').write(str(self.lose_total_euro))
            open('other_txt/seikoufx/seikoufx_seikoufx1_lose_total_lb.txt', 'w').write(str(self.lose_total_lb))
            open('other_txt/seikoufx/seikoufx_seikoufx1_draw_total.txt', 'w').write(str(self.draw_total))
            open('other_txt/seikoufx/seikoufx_seikoufx1_draw_total_euro.txt', 'w').write(str(self.draw_total_euro))
            open('other_txt/seikoufx/seikoufx_seikoufx1_draw_total_lb.txt', 'w').write(str(self.draw_total_lb))
        if zone == "16:30成行き売買→09：00成行き決済":
            open('other_txt/seikoufx/seikoufx_seikoufx2_main_total.txt', 'w').write(str(self.main_total))
            open('other_txt/seikoufx/seikoufx_seikoufx2_main_total_euro.txt', 'w').write(str(self.main_total_euro))
            open('other_txt/seikoufx/seikoufx_seikoufx2_main_total_lb.txt', 'w').write(str(self.main_total_lb))
            open('other_txt/seikoufx/seikoufx_seikoufx2_win_total.txt', 'w').write(str(self.win_total))
            open('other_txt/seikoufx/seikoufx_seikoufx2_win_total_euro.txt', 'w').write(str(self.win_total_euro))
            open('other_txt/seikoufx/seikoufx_seikoufx2_win_total_lb.txt', 'w').write(str(self.win_total_lb))
            open('other_txt/seikoufx/seikoufx_seikoufx2_lose_total.txt', 'w').write(str(self.lose_total))
            open('other_txt/seikoufx/seikoufx_seikoufx2_lose_total_euro.txt', 'w').write(str(self.lose_total_euro))
            open('other_txt/seikoufx/seikoufx_seikoufx2_lose_total_lb.txt', 'w').write(str(self.lose_total_lb))
            open('other_txt/seikoufx/seikoufx_seikoufx2_draw_total.txt', 'w').write(str(self.draw_total))
            open('other_txt/seikoufx/seikoufx_seikoufx2_draw_total_euro.txt', 'w').write(str(self.draw_total_euro))
            open('other_txt/seikoufx/seikoufx_seikoufx2_draw_total_lb.txt', 'w').write(str(self.draw_total_lb))


    def __init__(self,driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()  
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.seikoufx1_will_hour = "7"
        self.seikoufx2_will_hour = "16"

        self.seikoufx1_will_minute = "55"
        self.seikoufx2_will_minute = "45"

        self.will_second = "00"


    
    def automation(self,num):
        print("成功fx")
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "09:00成行き売買→16：30成行き決済"
            print(zone)

            self.get_category_num(zone)

            self.get_time(zone)
            self.get_total_file(zone)
            self.get_main_sign(zone)

            self.get_main_total()
            self.get_main_total_euro()
            self.get_main_total_lb()
            # self.get_all_main_total(zone)

            self.count_win_or_lose_total()

            seikoufx_text = SeikoufxText(zone,self.zone_state,self.zone_state_euro,self.zone_state_lb,self.main_sign,self.main_sign_euro,self.main_sign_lb,self.main_total,self.main_total_euro,self.main_total_lb,self.zone_dollar,self.zone_euro,self.zone_lb,self.zone_settlement,self.zone_settlement_euro,self.zone_settlement_lb,self.buy_time,self.settlement_time,self.win_total,self.win_total_euro,self.win_total_lb,self.lose_total,self.lose_total_euro,self.lose_total_lb,self.draw_total,self.draw_total_euro,self.draw_total_lb)
            self.blog_post(self.category_num,seikoufx_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)

        if num == 9:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "16:30成行き売買→09：00成行き決済"
            print(zone)

            self.get_category_num(zone)

            self.get_time(zone)
            self.get_total_file(zone)
            self.get_main_sign(zone)


            self.get_main_total()
            self.get_main_total_euro()
            self.get_main_total_lb()
            # self.get_all_main_total(zone)

            self.count_win_or_lose_total()

            seikoufx_text = SeikoufxText(zone,self.zone_state,self.zone_state_euro,self.zone_state_lb,self.main_sign,self.main_sign_euro,self.main_sign_lb,self.main_total,self.main_total_euro,self.main_total_lb,self.zone_dollar,self.zone_euro,self.zone_lb,self.zone_settlement,self.zone_settlement_euro,self.zone_settlement_lb,self.buy_time,self.settlement_time,self.win_total,self.win_total_euro,self.win_total_lb,self.lose_total,self.lose_total_euro,self.lose_total_lb,self.draw_total,self.draw_total_euro,self.draw_total_lb)
            self.blog_post(self.category_num,seikoufx_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)


#実行からあああああああああああああ
