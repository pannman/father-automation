from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.yumewogenzituni_text_config import YumewogenzituniText
from .fc2 import Fc2
import datetime


class Yumewogenzituni(Fc2):
    def login_id(self):
        return LOGIN.YUMEWOGENZITUNI_LOGIN['ID']

    def login_pass(self):
        return LOGIN.YUMEWOGENZITUNI_LOGIN['PASS']
    
    def return_will_hour(self,zone):
        if zone == "日中":
            return self.day_will_hour
        if zone == "前場":
            return self.before_will_hour
        if zone == "後場":
            return self.after_will_hour
        if zone == "ナイトセッション":
            return self.nightsession_will_hour
        if zone == "オーバーナイト2":
            return self.overnight2_will_hour

    def return_will_minute(self,zone):
        if zone == "日中":
            return self.day_will_minute
        if zone == "前場":
            return self.before_will_minute
        if zone == "後場":
            return self.after_will_minute
        if zone == "ナイトセッション":
            return self.nightsession_will_minute
        if zone == "オーバーナイト2":
            return self.overnight2_will_minute

    def get_main_result(self,zone):
        if CONFIG.yumewogenzituni_main(zone) == "勝ち":
            self.main_total+= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "+" + CONFIG.nikkei_mini_result(zone)
        if CONFIG.yumewogenzituni_main(zone) == "負け":
            self.main_total-= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "-" + CONFIG.nikkei_mini_result(zone)
        if CONFIG.yumewogenzituni_main(zone) == "引き分け":
            self.main_total+= int(CONFIG.nikkei_mini_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "±" + CONFIG.nikkei_mini_result(zone)
    
    def count_win_or_lose_total(self,zone):
        if CONFIG.yumewogenzituni_main(zone) == "勝ち":
            self.win_total+=1
        if CONFIG.yumewogenzituni_main(zone) == "負け":
            self.lose_total+=1
        if CONFIG.yumewogenzituni_main(zone) == "引き分け":
            self.draw_total+=1

    def get_total_file(self,zone):
        if zone == "日中":
            self.main_total = open('other_txt/yumewogenzituni/yumewogenzituni_day_main_total.txt', 'r').read()
            self.win_total = int(open('other_txt/yumewogenzituni/yumewogenzituni_day_win_total.txt', 'r').read())
            self.lose_total = int(open('other_txt/yumewogenzituni/yumewogenzituni_day_lose_total.txt', 'r').read())
            self.draw_total = int(open('other_txt/yumewogenzituni/yumewogenzituni_day_draw_total.txt', 'r').read())
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "前場":
            self.main_total = open('other_txt/yumewogenzituni/yumewogenzituni_before_main_total.txt', 'r').read()
            self.win_total = int(open('other_txt/yumewogenzituni/yumewogenzituni_before_win_total.txt', 'r').read())
            self.lose_total = int(open('other_txt/yumewogenzituni/yumewogenzituni_before_lose_total.txt', 'r').read())
            self.draw_total = int(open('other_txt/yumewogenzituni/yumewogenzituni_before_draw_total.txt', 'r').read())
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "後場":
            self.main_total = open('other_txt/yumewogenzituni/yumewogenzituni_after_main_total.txt', 'r').read()
            self.win_total = int(open('other_txt/yumewogenzituni/yumewogenzituni_after_win_total.txt', 'r').read())
            self.lose_total = int(open('other_txt/yumewogenzituni/yumewogenzituni_after_lose_total.txt', 'r').read())
            self.draw_total = int(open('other_txt/yumewogenzituni/yumewogenzituni_after_draw_total.txt', 'r').read())
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "ナイトセッション":
            self.main_total = open('other_txt/yumewogenzituni/yumewogenzituni_nightsession_main_total.txt', 'r').read()
            self.win_total = int(open('other_txt/yumewogenzituni/yumewogenzituni_nightsession_win_total.txt', 'r').read())
            self.lose_total = int(open('other_txt/yumewogenzituni/yumewogenzituni_nightsession_lose_total.txt', 'r').read())
            self.draw_total = int(open('other_txt/yumewogenzituni/yumewogenzituni_nightsession_draw_total.txt', 'r').read())
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "オーバーナイト2":
            self.main_total = open('other_txt/yumewogenzituni/yumewogenzituni_overnight2_main_total.txt', 'r').read()
            self.win_total = int(open('other_txt/yumewogenzituni/yumewogenzituni_overnight2_win_total.txt', 'r').read())
            self.lose_total = int(open('other_txt/yumewogenzituni/yumewogenzituni_overnight2_lose_total.txt', 'r').read())
            self.draw_total = int(open('other_txt/yumewogenzituni/yumewogenzituni_overnight2_draw_total.txt', 'r').read())
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
        if datetime.datetime.now().day == 1:
            self.main_total = 0
            self.win_total = 0
            self.main_total = 0
            self.lose_total = 0

    def save_total_file(self,zone):
        if zone == "日中":
            open('other_txt/yumewogenzituni/yumewogenzituni_day_main_total.txt', 'w').write(str(self.main_total))
            open('other_txt/yumewogenzituni/yumewogenzituni_day_win_total.txt', 'w').write(str(self.win_total))
            open('other_txt/yumewogenzituni/yumewogenzituni_day_lose_total.txt', 'w').write(str(self.lose_total))
            open('other_txt/yumewogenzituni/yumewogenzituni_day_draw_total.txt', 'w').write(str(self.draw_total))
        if zone == "前場":
            open('other_txt/yumewogenzituni/yumewogenzituni_before_main_total.txt', 'w').write(str(self.main_total))
            open('other_txt/yumewogenzituni/yumewogenzituni_before_win_total.txt', 'w').write(str(self.win_total))
            open('other_txt/yumewogenzituni/yumewogenzituni_before_lose_total.txt', 'w').write(str(self.lose_total))
            open('other_txt/yumewogenzituni/yumewogenzituni_before_draw_total.txt', 'w').write(str(self.draw_total))
        if zone == "後場":
            open('other_txt/yumewogenzituni/yumewogenzituni_after_main_total.txt', 'w').write(str(self.main_total))
            open('other_txt/yumewogenzituni/yumewogenzituni_after_win_total.txt', 'w').write(str(self.win_total))
            open('other_txt/yumewogenzituni/yumewogenzituni_after_lose_total.txt', 'w').write(str(self.lose_total))
            open('other_txt/yumewogenzituni/yumewogenzituni_after_draw_total.txt', 'w').write(str(self.draw_total))
        if zone == "ナイトセッション":
            open('other_txt/yumewogenzituni/yumewogenzituni_nightsession_main_total.txt', 'w').write(str(self.main_total))
            open('other_txt/yumewogenzituni/yumewogenzituni_nightsession_win_total.txt', 'w').write(str(self.win_total))
            open('other_txt/yumewogenzituni/yumewogenzituni_nightsession_lose_total.txt', 'w').write(str(self.lose_total))
            open('other_txt/yumewogenzituni/yumewogenzituni_nightsession_draw_total.txt', 'w').write(str(self.draw_total))
        if zone == "オーバーナイト":
            open('other_txt/yumewogenzituni/yumewogenzituni_overnight_main_total.txt', 'w').write(str(self.main_total))
            open('other_txt/yumewogenzituni/yumewogenzituni_overnight_win_total.txt', 'w').write(str(self.win_total))
            open('other_txt/yumewogenzituni/yumewogenzituni_overnight_lose_total.txt', 'w').write(str(self.lose_total))
            open('other_txt/yumewogenzituni/yumewogenzituni_overnight_draw_total.txt', 'w').write(str(self.draw_total))

    def __init__(self,driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()  
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.day_will_hour = "7"
        self.before_will_hour = "7"
        self.after_will_hour = "12"
        self.nightsession_will_hour = "14"
        # self.overnight2_will_hour = 

        self.day_will_minute = "00"
        self.before_will_minute = "05"
        self.after_will_minute = "15"
        self.nightsession_will_minute = "30"
        # self.overnight2_will_minute =

        self.will_second = "00"
    
    def automation(self,num):
        if num == 3:
            self.login_fc2()
            zones = ["日中","前場","後場"]
            for zone in zones:
                self.get_total_file(zone)
                self.count_win_or_lose_total(zone)
                yumewogenzituni_text = YumewogenzituniText(zone,CONFIG.yumewogenzituni_main_buy_result(zone),self.get_main_result(zone),self.main_total,self.win_total,self.lose_total,self.draw_total)
                self.blog_post(yumewogenzituni_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
                self.save_total_file(zone)
        if num == 5:
            self.login_fc2()
            zone = "ナイトセッション"
            self.get_total_file(zone)
            self.count_win_or_lose_total(zone)
            yumewogenzituni_text = YumewogenzituniText(zone,CONFIG.yumewogenzituni_main_buy_result(zone),self.get_main_result(zone),self.main_total,self.win_total,self.lose_total,self.draw_total)
            self.blog_post(yumewogenzituni_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)
        if num == 9:
            self.login_fc2()
            zone = "オーバーナイト2"
            self.get_total_file(zone)
            self.count_win_or_lose_total(zone)
            yumewogenzituni_text = YumewogenzituniText(zone,CONFIG.yumewogenzituni_main_buy_result(zone),self.get_main_result(zone),self.main_total,self.win_total,self.lose_total,self.draw_total)
            self.blog_post(yumewogenzituni_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_total_file(zone)