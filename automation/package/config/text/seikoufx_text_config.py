from .. import all_config as CONFIG

class SeikoufxText():
    def __init__(self, zone,zone_state,zone_state_euro,zone_state_lb, main_sign, main_sign_euro, main_sign_lb, main_total, main_total_euro, main_total_lb, zone_dollar, zone_euro, zone_lb, zone_settlement, zone_settlement_euro, zone_settlement_lb, buy_time, settlement_time, win_total,win_total_euro, win_total_lb,lose_total, lose_total_euro, lose_total_lb, draw_total, draw_total_euro, draw_total_lb):
        self.zone = zone
        self.buy = zone_state
        self.buy_euro = zone_state_euro
        self.buy_lb = zone_state_lb
        self.main_sign = main_sign
        self.main_sign_euro = main_sign_euro
        self.main_sign_lb = main_sign_lb
        self.main_total = main_total
        self.main_total_euro = main_total_euro
        self.main_total_lb = main_total_lb
        self.zone_dollar = zone_dollar
        self.zone_euro = zone_euro
        self.zone_lb = zone_lb
        self.zone_settlement = zone_settlement
        self.zone_settlement_euro = zone_settlement_euro
        self.zone_settlement_lb = zone_settlement_lb
        self.buy_time = buy_time
        self.settlement_time = settlement_time
        self.win_total = str(int(win_total))
        self.win_total_euro = str(int(win_total_euro))
        self.win_total_lb = str(int(win_total_lb))
        self.lose_total = str(int(lose_total))
        self.lose_total_euro = str(int(lose_total_euro))
        self.lose_total_lb = str(int(lose_total_lb))
        self.draw_total = str(int(draw_total))
        self.draw_total_euro = str(int(draw_total_euro))
        self.draw_total_lb = str(int(draw_total_lb))
        print(type(self.win_total))
        if self.settlement_time == "y09:00":
            self.settlement_time = "09：30"
        if self.main_sign == "0":
            self.main_sign = "±0"
        if self.buy == "買い":
            self.buy == "ASK"
        if self.buy == "売り":
            self.buy == "BID"

        if float(self.main_sign) == 0:
            self.mark = ""
        if float(self.main_sign) > 0:
            self.mark = "(^-^)/"
        if float(self.main_sign) < 0:
            self.mark = "(Ｔ＿Ｔ)"
        if float(self.main_sign_euro) == 0:
            self.mark_euro = ""
        if float(self.main_sign_euro) > 0:
            self.mark_euro = "(^-^)/"
        if float(self.main_sign_euro) < 0:
            self.mark_euro = "(Ｔ＿Ｔ)"
        if float(self.main_sign_lb) == 0:
            self.mark_lb = ""
        if float(self.main_sign_lb) > 0:
            self.mark_lb = "(^-^)/"
        if float(self.main_sign_lb) < 0:
            self.mark_lb = "(Ｔ＿Ｔ)"
        print("ドル")
        print(self.buy + "   "+str(self.zone_dollar)+"   決済    "+ str(self.zone_settlement) +"")
        print("メイン   " + self.main_sign+"    " + str(CONFIG.result_month()) + "月累計   " + self.main_total)
        print("ユーロ")
        print(self.buy_euro + "   "+str(self.zone_euro)+"   決済    "+ str(self.zone_settlement_euro) +"")
        print("メイン   " + self.main_sign_euro+"    " + str(CONFIG.result_month()) + "月累計   " + self.main_total_euro)
        print("ポンド")
        print(self.buy_lb + "   "+str(self.zone_lb)+"   決済    "+ str(self.zone_settlement_lb) +"")
        print("メイン   " + self.main_sign_lb+"    " + str(CONFIG.result_month()) + "月累計   " + self.main_total_lb)
    def blog_title(self):
        return "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) +"の結果"
    def blog_text(self):
        return  "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) +"の結果！　（"+self.zone+"　USD/JPY）\n\n\n"\
                ""+self.buy+"でした。"+self.mark+"\n\n\n"\
                ""+self.main_sign+"pips\n\n\n"\
                "" + str(CONFIG.result_month()) + "月累計　　"+self.main_total+"pips　 " + self.win_total +"勝"+self.lose_total+"敗"+self.draw_total+"分\n\n\n"\
                "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) +"の結果！　（"+self.zone+"　EUR/JPY）\n\n\n"\
                ""+self.buy_euro+"でした。"+self.mark_euro+"\n\n\n"\
                ""+self.main_sign_euro+"pips\n\n\n"\
                "" + str(CONFIG.result_month()) + "月累計　　"+self.main_total_euro+"pips　 " + self.win_total_euro + "勝"+self.lose_total_euro+"敗"+self.draw_total_euro+"分\n\n\n"\
                "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) +"の結果！　（"+self.zone+"　GBP/JPY）\n\n\n"\
                ""+self.buy_lb+"でした。"+self.mark_lb+"\n\n\n"\
                ""+self.main_sign_lb+"pips\n\n\n"\
                "" + str(CONFIG.result_month()) + "月累計　　"+self.main_total_lb+"pips　 " + self.win_total_lb + "勝"+self.lose_total_lb+"敗"+self.draw_total_lb+"分\n\n\n"\
                "本日はどうなりますか～\n\n\n"\
                "幸運を期待してます。(^-^)/\n\n\n"\
                "有料メール配信をご希望される方は下記よりお願いします。(^-^)/\n\n\n"\
                "　↓　↓　↓　↓\n\n\n"\
                '<a href="http://bridge8fx.blog.fc2.com/blog-entry-3.html" title="＊会員募集詳細＊ ">＊会員募集詳細＊ </a>\n\n\n'\
  
