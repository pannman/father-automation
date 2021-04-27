from .. import all_config as CONFIG
import math


class InvestingText():
    def __init__(self,zone,buy,main_sign,main_total,win_total,lose_total,draw_total,all_win_total,all_lose_total,all_draw_total,all_main_total):
        self.zone = zone
        self.buy = buy
        self.main_sign = main_sign
        self.main_total = main_total
        self.win_total = win_total
        self.lose_total = lose_total
        self.draw_total = draw_total
        self.all_win_total = all_win_total
        self.all_lose_total = all_lose_total
        self.all_draw_total = all_draw_total
        self.all_main_total = all_main_total
        if self.zone == "前場":
            self.zone_name = "Ａ"
            self.zone_title = "" + self.zone_name + " 08:45 ～ 11:30 （売買サイン"
        if self.zone == "後場":
            self.zone_name = "Ｂ"
            self.zone_title = "" + self.zone_name + " 12:30 ～ 15:15 （売買サイン"
        if self.zone == "c":
            self.zone_name = "Ｃ"
            self.zone_title = "" + self.zone_name + " 16:30 ～ 20:00 （売買サイン"
        if self.zone == "d":
            self.zone_name = "Ｄ"
            self.zone_title = "" + self.zone_name + " 21:00 ～ 05:30 （売買サイン"
        print("メイン   "+main_sign+"   " + str(CONFIG.result_month()) + "月累計   " + main_total)
        print('メイン   ' + str(self.win_total) + '勝' + str(self.lose_total) +'敗'+ str(self.draw_total) + '分')
    def blog_title(self):
        return ""+ self.zone_title +"）"
    def blog_text(self):
        return  ""+ self.zone_title +"）\n\n"\
                "売買サインは配信させて頂きました。\n\n"\
                "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "の　" + self.zone_title + "結果）\n\n"\
                "" + self.buy + "で " + self.main_sign + "でした。\n\n"\
                "" + self.zone_name + "の" + str(CONFIG.result_month()) + "月累計は　" + self.main_total +"です。（" + str(self.win_total) +"勝" + str(self.lose_total) +"敗" + str(self.draw_total) +"分　勝率" + str(math.floor(self.win_total/(self.win_total+self.lose_total+self.draw_total)*100)) +"％）\n\n"\
                "" + str(CONFIG.result_month()) + "月のＡＢＣＤの累計合計結果 " + self.all_main_total + "です。（" + self.all_win_total +"勝" + self.all_lose_total +"敗" + self.all_draw_total +"分　勝率" + str(math.floor(int(self.all_win_total)/(int(self.all_win_total)+int(self.all_lose_total)+int(self.all_draw_total))*100)) +"％）"
