from ..config import login_config as LOGIN
from ..config import all_config as CONFIG
from ..config.text.tradesisutemu_text_config import TradesisutemuText
from ..config.text.tradesisutemu_predict_text_config import TradesisutemuPredictText

from .fc2 import Fc2
import datetime


class Tradesisutemu(Fc2):
    def login_id(self):
        return LOGIN.TRADESISUTEMU_LOGIN['ID']

    def login_pass(self):
        return LOGIN.TRADESISUTEMU_LOGIN['PASS']

    def get_category_num(self, zone):
        if zone == "日中":
            self.category_num = 2
        if zone == "ナイトセッション":
            self.category_num = 3
        if zone == "オーバーナイト":
            self.category_num = 4

    def return_will_hour(self, zone):
        if zone == "日中":
            return self.day_will_hour
        if zone == "日中の予測情報":
            return self.day_predict_will_hour
        if zone == "ナイトセッション":
            return self.nightsession_will_hour
        if zone == "ナイトセッションの予測情報":
            return self.nightsession_predict_will_hour
        if zone == "オーバーナイト":
            return self.overnight_will_hour
        if zone == "オーバーナイトの予測情報":
            return self.overnight_predict_will_hour

    def return_will_minute(self, zone):
        if zone == "日中":
            return self.day_will_minute
        if zone == "日中の予測情報":
            return self.day_predict_will_minute
        if zone == "ナイトセッション":
            return self.nightsession_will_minute
        if zone == "ナイトセッションの予測情報":
            return self.nightsession_predict_will_minute
        if zone == "オーバーナイト":
            return self.overnight_will_minute
        if zone == "オーバーナイトの予測情報":
            return self.overnight_predict_will_minute

    def get_main_result(self, zone):
        if CONFIG.tradesisutemu_main(zone) == "勝ち":
            self.main_total += int(CONFIG.nikkei_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(
                self.main_total) if self.main_total == 0 else str(self.main_total)
            return "+" + CONFIG.nikkei_result(zone)
        if CONFIG.tradesisutemu_main(zone) == "負け":
            self.main_total -= int(CONFIG.nikkei_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(
                self.main_total) if self.main_total == 0 else str(self.main_total)
            return "-" + CONFIG.nikkei_result(zone)
        if CONFIG.tradesisutemu_main(zone) == "引き分け":
            self.main_total += int(CONFIG.nikkei_result(zone))
            self.main_total = "+" + str(self.main_total) if self.main_total > 0 else "±" + str(
                self.main_total) if self.main_total == 0 else str(self.main_total)
            return "±" + CONFIG.nikkei_result(zone)

    def get_all_main_total(self, zone):
        if zone == "日中":
            other_main_total = open(
                'other_txt/tradesisutemu/tradesisutemu_nightsession_main_total.txt', 'r').read()
            if other_main_total == "±0":
                other_main_total = "0"
            other_main_total_2 = open(
                'other_txt/tradesisutemu/tradesisutemu_overnight_main_total.txt', 'r').read()
            if other_main_total_2 == "±0":
                other_main_total_2 = "0"
            self.all_main_total = int(other_main_total) + int(self.main_total)+int(other_main_total_2)
            self.all_main_total = "+" + str(self.all_main_total) if self.all_main_total > 0 else "±" + str(
                self.all_main_total) if self.all_main_total == 0 else str(self.all_main_total)
            return self.all_main_total
        if zone == "ナイトセッション":
            other_main_total = open(
                'other_txt/tradesisutemu/tradesisutemu_day_main_total.txt', 'r').read()
            if other_main_total == "±0":
                other_main_total = "0"
            other_main_total_2 = open(
                'other_txt/tradesisutemu/tradesisutemu_overnight_main_total.txt', 'r').read()
            if other_main_total_2 == "±0":
                other_main_total_2 = "0"
            self.all_main_total = int(other_main_total) + int(self.main_total)+int(other_main_total_2)
            self.all_main_total = "+" + str(self.all_main_total) if self.all_main_total > 0 else "±" + str(
                self.all_main_total) if self.all_main_total == 0 else str(self.all_main_total)
            return self.all_main_total
        if zone == "オーバーナイト":
            other_main_total = open(
                'other_txt/tradesisutemu/tradesisutemu_nightsession_main_total.txt', 'r').read()
            if other_main_total == "±0":
                other_main_total = "0"
            other_main_total_2 = open(
                'other_txt/tradesisutemu/tradesisutemu_day_main_total.txt', 'r').read()
            if other_main_total_2 == "±0":
                other_main_total_2 = "0"
            self.all_main_total = int(other_main_total) + int(self.main_total)+int(other_main_total_2)
            self.all_main_total = "+" + str(self.all_main_total) if self.all_main_total > 0 else "±" + str(
                self.all_main_total) if self.all_main_total == 0 else str(self.all_main_total)
            return self.all_main_total

    def get_total_file(self, zone):
        if zone == "日中":
            self.main_total = open(
                'other_txt/tradesisutemu/tradesisutemu_day_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(
                self.main_total)
        if zone == "ナイトセッション":
            self.main_total = open(
                'other_txt/tradesisutemu/tradesisutemu_nightsession_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(
                self.main_total)
        if zone == "オーバーナイト":
            self.main_total = open(
                'other_txt/tradesisutemu/tradesisutemu_overnight_main_total.txt', 'r').read()
            self.main_total = 0 if self.main_total == "±0" else int(
                self.main_total)

    def save_total_file(self, zone):
        if zone == "日中":
            open('other_txt/tradesisutemu/tradesisutemu_day_main_total.txt',
                 'w').write(str(self.main_total))
        if zone == "ナイトセッション":
            open('other_txt/tradesisutemu/tradesisutemu_nightsession_main_total.txt',
                 'w').write(str(self.main_total))
        if zone == "オーバーナイト":
            open('other_txt/tradesisutemu/tradesisutemu_overnight_main_total.txt',
                 'w').write(str(self.main_total))

    def get_tradesisutemu_result_settlement_money(self, zone):
        if (CONFIG.tradesisutemu_main(zone) == "勝ち" and CONFIG.tradesisutemu_main_buy_result(zone) == "買い") or (CONFIG.tradesisutemu_main(zone) == "負け" and CONFIG.tradesisutemu_main_buy_result(zone) == "売り"):
            self.result_settlement_money = str(
                int(CONFIG.tradesisutemu_result_trade_money(zone)) + int(CONFIG.nikkei_result(zone)))
            return self.result_settlement_money
        if (CONFIG.tradesisutemu_main(zone) == "勝ち" and CONFIG.tradesisutemu_main_buy_result(zone) == "売り") or (CONFIG.tradesisutemu_main(zone) == "負け" and CONFIG.tradesisutemu_main_buy_result(zone) == "買い"):
            self.result_settlement_money = str(
                int(CONFIG.tradesisutemu_result_trade_money(zone)) - int(CONFIG.nikkei_result(zone)))
            return self.result_settlement_money
        else:
            self.result_settlement_money = str(
                int(CONFIG.tradesisutemu_result_trade_money(zone)))
            return self.result_settlement_money

    def __init__(self, driver):
        super().__init__(driver)

        self.will_year = CONFIG.reserve_year()
        self.will_month = CONFIG.reserve_month()
        self.will_day = CONFIG.reserve_day()

        self.day_will_hour = "15"
        self.nightsession_will_hour = "6"
        self.overnight_will_hour = "9"
        self.day_predict_will_hour = "8"
        self.nightsession_predict_will_hour = "16"
        self.overnight_predict_will_hour = "22"


        self.day_will_minute = "45"
        self.nightsession_will_minute = "50"
        self.overnight_will_minute = "45"
        self.day_predict_will_minute = "35"
        self.nightsession_predict_will_minute = "10"
        self.overnight_predict_will_minute = "10"


        self.will_second = "00"

    def automation(self, num):
        print("システムトレード")
        if num == 3:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "日中"
            print(zone)
            self.get_category_num(zone)
            self.get_total_file(zone)
            tradesisutemu_text = TradesisutemuText(zone, CONFIG.tradesisutemu_main_buy_result(zone), self.get_main_result(
                zone), self.main_total, CONFIG.tradesisutemu_result_trade_money(zone), self.get_tradesisutemu_result_settlement_money(zone), self.get_all_main_total(zone))
            self.blog_post(self.category_num, tradesisutemu_text, zone, self.will_year,
                           self.will_month, self.will_day, self.will_second)
            self.save_total_file(zone)

        if num == 5:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "ナイトセッション"
            print(zone)
            self.get_category_num(zone)
            self.get_total_file(zone)
            tradesisutemu_text = TradesisutemuText(zone, CONFIG.tradesisutemu_main_buy_result(zone), self.get_main_result(
                zone), self.main_total, CONFIG.tradesisutemu_result_trade_money(zone), self.get_tradesisutemu_result_settlement_money(zone), self.get_all_main_total(zone))
            self.blog_post(self.category_num, tradesisutemu_text, zone, self.will_year,
                           self.will_month, self.will_day, self.will_second)
            self.save_total_file(zone)
            
        if num == 9:
            print(str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()))
            self.login_fc2()
            zone = "オーバーナイト"
            print(zone)
            self.get_category_num(zone)
            self.get_total_file(zone)
            tradesisutemu_text = TradesisutemuText(zone, CONFIG.tradesisutemu_main_buy_result(zone), self.get_main_result(
                zone), self.main_total, CONFIG.tradesisutemu_result_trade_money(zone), self.get_tradesisutemu_result_settlement_money(zone), self.get_all_main_total(zone))
            self.blog_post(self.category_num, tradesisutemu_text, zone, self.will_year,
                           self.will_month, self.will_day, self.will_second)
            self.save_total_file(zone)
            
            zones = ["日中の予測情報", "ナイトセッションの予測情報", "オーバーナイトの予測情報"]
            times = ["8：30", "16：10", "22：00"]
            for i in range(3):
                tradesisutemu_predict_text = TradesisutemuPredictText(
                    zones[i], times[i])
                self.blog_post(0, tradesisutemu_predict_text, zones[i], self.will_year,
                               self.will_month, self.will_day, self.will_second)
