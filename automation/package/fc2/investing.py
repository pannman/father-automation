from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.investing_text_config import InvestingText
from .fc2 import Fc2
import datetime


class Investing(Fc2):
    def login_id(self):
        return LOGIN.INVESTING_LOGIN['ID']

    def login_pass(self):
        return LOGIN.INVESTING_LOGIN['PASS']
    
    def return_will_hour(self,zone):
        if zone == "前場":
            return self.before_will_hour
        if zone == "後場":
            return self.after_will_hour
        if zone == "c":
            return self.c_will_hour
        if zone == "d":
            return self.d_will_hour

    def return_will_minute(self,zone):
        if zone == "前場":
            return self.before_will_minute
        if zone == "後場":
            return self.after_will_minute
        if zone == "c":
            return self.c_will_minute
        if zone == "d":
            return self.d_will_minute

    def get_main_result(self,zone):
        if CONFIG.investing_main(zone) == "勝ち":
            self.main_total+= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "+" + CONFIG.nikkei_mini_result(zone)
        if CONFIG.investing_main(zone) == "負け":
            self.main_total-= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "-" + CONFIG.nikkei_mini_result(zone)
        if CONFIG.investing_main(zone) == "引き分け":
            self.main_total+= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "±" + CONFIG.nikkei_mini_result(zone)
    
    def count_win_or_lose_total(self,zone):
        if CONFIG.investing_main(zone) == "勝ち":
            self.win_total+=1
        if CONFIG.investing_main(zone) == "負け":
            self.lose_total+=1
        if CONFIG.investing_main(zone) == "引き分け":
            self.draw_total+=1

    def get_total_file(self,zone):
        if zone == "前場":
            self.main_total = open('other_txt/investing/investing_before_main_total.txt', 'r').read()
            self.win_total = int(open('other_txt/investing/investing_before_win_total.txt', 'r').read())
            self.lose_total = int(open('other_txt/investing/investing_before_lose_total.txt', 'r').read())
            self.draw_total = int(open('other_txt/investing/investing_before_draw_total.txt', 'r').read())
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "後場":
            self.main_total = open('other_txt/investing/investing_after_main_total.txt', 'r').read()
            self.win_total = int(open('other_txt/investing/investing_after_win_total.txt', 'r').read())
            self.lose_total = int(open('other_txt/investing/investing_after_lose_total.txt', 'r').read())
            self.draw_total = int(open('other_txt/investing/investing_after_draw_total.txt', 'r').read())
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "c":
            self.main_total = open('other_txt/investing/investing_c_main_total.txt', 'r').read()
            self.win_total = int(open('other_txt/investing/investing_c_win_total.txt', 'r').read())
            self.lose_total = int(open('other_txt/investing/investing_c_lose_total.txt', 'r').read())
            self.draw_total = int(open('other_txt/investing/investing_c_draw_total.txt', 'r').read())
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "d":
            self.main_total = open('other_txt/investing/investing_d_main_total.txt', 'r').read()
            self.win_total = int(open('other_txt/investing/investing_d_win_total.txt', 'r').read())
            self.lose_total = int(open('other_txt/investing/investing_d_lose_total.txt', 'r').read())
            self.draw_total = int(open('other_txt/investing/investing_d_draw_total.txt', 'r').read())
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)

    def save_total_file(self,zone):
        if zone == "前場":
            open('other_txt/investing/investing_before_main_total.txt', 'w').write(str(self.main_total))
            open('other_txt/investing/investing_before_win_total.txt', 'w').write(str(self.win_total))
            open('other_txt/investing/investing_before_lose_total.txt', 'w').write(str(self.lose_total))
            open('other_txt/investing/investing_before_draw_total.txt', 'w').write(str(self.draw_total))
        if zone == "後場":
            open('other_txt/investing/investing_after_main_total.txt', 'w').write(str(self.main_total))
            open('other_txt/investing/investing_after_win_total.txt', 'w').write(str(self.win_total))
            open('other_txt/investing/investing_after_lose_total.txt', 'w').write(str(self.lose_total))
            open('other_txt/investing/investing_after_draw_total.txt', 'w').write(str(self.draw_total))
        if zone == "c":
            open('other_txt/investing/investing_c_main_total.txt', 'w').write(str(self.main_total))
            open('other_txt/investing/investing_c_win_total.txt', 'w').write(str(self.win_total))
            open('other_txt/investing/investing_c_lose_total.txt', 'w').write(str(self.lose_total))
            open('other_txt/investing/investing_c_draw_total.txt', 'w').write(str(self.draw_total))
        if zone == "d":
            open('other_txt/investing/investing_d_main_total.txt', 'w').write(str(self.main_total))
            open('other_txt/investing/investing_d_win_total.txt', 'w').write(str(self.win_total))
            open('other_txt/investing/investing_d_lose_total.txt', 'w').write(str(self.lose_total))
            open('other_txt/investing/investing_d_draw_total.txt', 'w').write(str(self.draw_total))
        
    def set_all_total_win(self):
        a_win_total = int(open('other_txt/investing/investing_before_win_total.txt', 'r').read())
        b_win_total = int(open('other_txt/investing/investing_after_win_total.txt', 'r').read())
        c_win_total = int(open('other_txt/investing/investing_c_win_total.txt', 'r').read())
        d_win_total = int(open('other_txt/investing/investing_d_win_total.txt', 'r').read())
        self.all_win_total = str(a_win_total + b_win_total + c_win_total + d_win_total)

    def set_all_total_lose(self):
        a_lose_total = int(open('other_txt/investing/investing_before_lose_total.txt', 'r').read())
        b_lose_total = int(open('other_txt/investing/investing_after_lose_total.txt', 'r').read())
        c_lose_total = int(open('other_txt/investing/investing_c_lose_total.txt', 'r').read())
        d_lose_total = int(open('other_txt/investing/investing_d_lose_total.txt', 'r').read())
        self.all_lose_total = str(a_lose_total + b_lose_total + c_lose_total + d_lose_total)
    
    def set_all_total_draw(self):
        a_draw_total = int(open('other_txt/investing/investing_before_draw_total.txt', 'r').read())
        b_draw_total = int(open('other_txt/investing/investing_after_draw_total.txt', 'r').read())
        c_draw_total = int(open('other_txt/investing/investing_c_draw_total.txt', 'r').read())
        d_draw_total = int(open('other_txt/investing/investing_d_draw_total.txt', 'r').read())
        self.all_draw_total = str(a_draw_total + b_draw_total + c_draw_total + d_draw_total)

    def set_all_main_total(self):
        if self.zone == "前場":
            b_main_total = int(open('other_txt/investing/investing_after_main_total.txt', 'r').read())
            c_main_total = int(open('other_txt/investing/investing_c_main_total.txt', 'r').read())
            d_main_total = int(open('other_txt/investing/investing_d_main_total.txt', 'r').read())
            self.all_main_total = str(int(self.main_total) + b_main_total + c_main_total + d_main_total)
            if int(self.all_main_total) > 0:
                self.all_main_total = "+" + self.all_main_total
            return self.all_main_total
        if self.zone == "後場":
            a_main_total = int(open('other_txt/investing/investing_before_main_total.txt', 'r').read())
            c_main_total = int(open('other_txt/investing/investing_c_main_total.txt', 'r').read())
            d_main_total = int(open('other_txt/investing/investing_d_main_total.txt', 'r').read())
            self.all_main_total = str(a_main_total + int(self.main_total) + c_main_total + d_main_total)
            if int(self.all_main_total) > 0:
                self.all_main_total = "+" + self.all_main_total
            return self.all_main_total
        if self.zone == "c":
            a_main_total = int(open('other_txt/investing/investing_before_main_total.txt', 'r').read())
            b_main_total = int(open('other_txt/investing/investing_after_main_total.txt', 'r').read())
            d_main_total = int(open('other_txt/investing/investing_d_main_total.txt', 'r').read())
            self.all_main_total = str(a_main_total +  b_main_total + int(self.main_total) + d_main_total)
            if int(self.all_main_total) > 0:
                self.all_main_total = "+" + self.all_main_total
            return self.all_main_total
        if self.zone == "d":
            a_main_total = int(open('other_txt/investing/investing_before_main_total.txt', 'r').read())
            b_main_total = int(open('other_txt/investing/investing_after_main_total.txt', 'r').read())
            c_main_total = int(open('other_txt/investing/investing_c_main_total.txt', 'r').read())
            self.all_main_total = str(a_main_total + b_main_total + c_main_total + int(self.main_total) )
            if int(self.all_main_total) > 0:
                self.all_main_total = "+" + self.all_main_total
            return self.all_main_total
        
    def __init__(self,driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()  
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.before_will_hour = "7"
        self.after_will_hour = "12"
        self.c_will_hour = "15"
        self.d_will_hour = "20"

        self.before_will_minute = "35"
        self.after_will_minute = "20"
        self.c_will_minute = "35"
        self.d_will_minute = "30"

        self.will_second = "00"
    
    def automation(self,num):
        print("日経225先物mini投資法")
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zones = ["前場","後場"]
            for zone in zones:
                print(zone)
                self.zone = zone
                self.set_all_total_win()
                self.set_all_total_lose()
                self.set_all_total_draw()
                self.get_total_file(zone)
                self.count_win_or_lose_total(zone)
                investing_text = InvestingText(zone,CONFIG.investing_main_buy_result(zone),self.get_main_result(zone),self.main_total,self.win_total,self.lose_total,self.draw_total,self.all_win_total,self.all_lose_total,self.all_draw_total,self.set_all_main_total())
                self.blog_post(investing_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
                self.save_total_file(zone)
        if num == 5:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zones = ["c","d"]
            for zone in zones:
                print(zone)
                self.zone = zone
                self.set_all_total_win()
                self.set_all_total_lose()
                self.set_all_total_draw()
                self.get_total_file(zone)
                self.set_all_main_total()
                self.count_win_or_lose_total(zone)
                investing_text = InvestingText(zone,CONFIG.investing_main_buy_result(zone),self.get_main_result(zone),self.main_total,self.win_total,self.lose_total,self.draw_total,self.all_win_total,self.all_lose_total,self.all_draw_total,self.set_all_main_total())
                self.blog_post(investing_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
                self.save_total_file(zone)
