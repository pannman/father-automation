from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.victorious_text_config import VictoriousText
from .fc2 import Fc2
import datetime

class Victorious(Fc2):
    def login_id(self):
        return LOGIN.VICTORIOUS_LOGIN['ID']

    def login_pass(self):
        return LOGIN.VICTORIOUS_LOGIN['PASS']
    
    def get_category_num(self,zone):
        if zone == "日中":
            self.category_num = 0
        if zone == "夜間立会":
            self.category_num = 0
        if zone == "夜間立会引け":
            self.category_num = 0
    
    def return_will_hour(self,zone):
        if zone == "日中":
            return self.day_will_hour
        if zone == "夜間立会":
            return self.yakanrikkai_will_hour
        if zone == "夜間立会引け":
            return self.yakanrikkaihike_will_hour
    
    def return_will_minute(self,zone):
        if zone == "日中":
            return self.day_will_minute
        if zone == "夜間立会":
            return self.yakanrikkai_will_minute
        if zone == "夜間立会引け":
            return self.yakanrikkaihike_will_minute

    def get_main_result(self,zone):
        zone_i = "日中"
        if zone == "夜間立会":
            zone_i = "ナイトセッション"
        if zone == "夜間立会引け":
            zone_i = "オーバーナイト2"
        if CONFIG.victorious_main(zone) == "勝ち":
            self.main_total += int(CONFIG.nikkei_result(zone_i))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "+" + CONFIG.nikkei_result(zone_i)
        if CONFIG.victorious_main(zone) == "負け":
            self.main_total -= int(CONFIG.nikkei_result(zone_i))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "-" + CONFIG.nikkei_result(zone_i)
        if CONFIG.victorious_main(zone) == "引き分け":
            self.main_total += int(CONFIG.nikkei_result(zone_i))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(self.main_total) if self.main_total == 0 else str(self.main_total)
            return "±" + CONFIG.nikkei_result(zone_i)

    def get_main_total_file(self,zone):
        if zone == "日中":
            self.main_total = open('other_txt/victorious/victorious_day_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
            self.main_total_2 = open('other_txt/victorious/victorious_yakanrikkai_main_total.txt', 'r').read()
            self.main_total_2 = 0 if self.main_total == "±0" else int(self.main_total)
            self.main_total_3 = open('other_txt/victorious/victorious_yakanrikkaihike_main_total.txt', 'r').read()
            self.main_total_3 = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "夜間立会":
            self.main_total = open('other_txt/victorious/victorious_yakanrikkai_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
            self.main_total_1 = open('other_txt/victorious/victorious_day_main_total.txt', 'r').read()
            self.main_total_1 = 0 if self.main_total == "±0" else int(self.main_total)
            self.main_total_3 = open('other_txt/victorious/victorious_yakanrikkaihike_main_total.txt', 'r').read()
            self.main_total_3 = 0 if self.main_total == "±0" else int(self.main_total)
        if zone == "夜間立会引け":
            self.main_total = open('other_txt/victorious/victorious_yakanrikkaihike_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(self.main_total)
            self.main_total_1 = open('other_txt/victorious/victorious_day_main_total.txt', 'r').read()
            self.main_total_1 = 0 if self.main_total == "±0" else int(self.main_total)
            self.main_total_2 = open('other_txt/victorious/victorious_yakanrikkai_main_total.txt', 'r').read()
            self.main_total_2 = 0 if self.main_total == "±0" else int(self.main_total)
    
    def save_main_total_file(self,zone):
        if zone == "日中":
            open('other_txt/victorious/victorious_day_main_total.txt', 'w').write(str(self.main_total))
        if zone == "夜間立会":
            open('other_txt/victorious/victorious_yakanrikkai_main_total.txt', 'w').write(str(self.main_total))
        if zone == "夜間立会引け":
            open('other_txt/victorious/victorious_yakanrikkaihike_main_total.txt', 'w').write(str(self.main_total))

    def __init__(self,driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()  
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.day_will_hour = "15"
        self.yakanrikkai_will_hour = "06"
        self.yakanrikkaihike_will_hour = "09"

        self.day_will_minute = "45"
        self.yakanrikkai_will_minute = "45"
        self.yakanrikkaihike_will_minute = "45"

        self.will_second = "00"
    
    def automation(self,num):
        print("ビクトリアストレード")
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "日中"
            print(zone)
            self.get_category_num(zone)
            self.get_main_total_file(zone)
            victorious_text = VictoriousText(zone, CONFIG.victorious_main_buy_result(zone),  self.get_main_result(zone), self.main_total,self.main_total_2,self.main_total_3)
            self.blog_post(self.category_num,victorious_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_main_total_file(zone)
        if num == 5:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "夜間立会"
            print(zone)
            self.get_category_num(zone)
            self.get_main_total_file(zone)
            victorious_text = VictoriousText(zone, CONFIG.victorious_main_buy_result(zone),  self.get_main_result(zone), self.main_total_1,self.main_total,self.main_total_3)
            self.blog_post(self.category_num,victorious_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_main_total_file(zone)
        if num == 9:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "夜間立会引け"
            print(zone)
            self.get_category_num(zone)
            self.get_main_total_file(zone)
            victorious_text = VictoriousText(zone, CONFIG.victorious_main_buy_result(zone),  self.get_main_result(zone), self.main_total_1,self.main_total_2,self.main_total)
            self.blog_post(self.category_num,victorious_text,zone,self.will_year,self.will_month,self.will_day,self.will_second)
            self.save_main_total_file(zone)
