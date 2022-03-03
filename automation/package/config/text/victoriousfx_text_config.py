from .. import all_config as CONFIG


class VictoriousfxText():
    def __init__(self, zone, zone_state, zone_state_euro, zone_state_lb, main_sign, main_sign_euro, main_sign_lb, main_total_1, main_total_euro_1, main_total_lb_1, main_total_2, main_total_euro_2, main_total_lb_2, main_total_3, main_total_euro_3, main_total_lb_3, zone_dollar, zone_euro, zone_lb, zone_settlement, zone_settlement_euro, zone_settlement_lb, buy_time, settlement_time):
        self.zone = zone
        self.buy = zone_state
        self.buy_euro = zone_state_euro
        self.buy_lb = zone_state_lb
        self.main_sign = main_sign
        self.main_sign_euro = main_sign_euro
        self.main_sign_lb = main_sign_lb
        self.main_total_1 = str(main_total_1)
        self.main_total_euro_1 = str(main_total_euro_1)
        self.main_total_lb_1=str(main_total_lb_1)
        self.main_total_2 = str(main_total_2)
        self.main_total_euro_2 = str(main_total_euro_2)
        self.main_total_lb_2 = str(main_total_lb_2)
        self.main_total_3 = str(main_total_3)
        self.main_total_euro_3 = str(main_total_euro_3)
        self.main_total_lb_3 = str(main_total_lb_3)
        self.zone_dollar = zone_dollar
        self.zone_euro = zone_euro
        self.zone_lb = zone_lb
        self.zone_settlement = zone_settlement
        self.zone_settlement_euro = zone_settlement_euro
        self.zone_settlement_lb = zone_settlement_lb
        self.buy_time = buy_time
        self.settlement_time = settlement_time

        if self.settlement_time == "y05:30":
            self.settlement_time = "05：30"
        if self.main_sign == "0":
            self.main_sign = "±0"
            
        print(self.main_sign+self.main_total_2)

        print("ドル")
        print(self.buy + "   "+str(self.zone_dollar) +
              "   決済    " + str(self.zone_settlement) + "")
        print("メイン   " + self.main_sign+"    " +
              str(CONFIG.result_month()) + "月累計5：30→9：00   " + self.main_total_1 + "9：00→16：30   " + self.main_total_2 + "16：30→5：30   " + self.main_total_3)
        print("ユーロ")
        print(self.buy_euro + "   "+str(self.zone_euro) +
              "   決済    " + str(self.zone_settlement_euro) + "")
        print("メイン   " + self.main_sign_euro+"    " +
              str(CONFIG.result_month()) + "月累計5：30→9：00   " + self.main_total_euro_1 + "9：00→16：30   " + self.main_total_euro_2 + "16：30→5：30   " + self.main_total_lb_2)
        print("ポンド")
        print(self.buy_lb + "   "+str(self.zone_lb) +
              "   決済    " + str(self.zone_settlement_lb) + "")
        print("メイン   " + self.main_sign_lb+"    " +
              str(CONFIG.result_month()) + "月累計5：30→9：00   " + self.main_total_lb_1 + "9：00→16：30   " + self.main_total_euro_3 + "16：30→5：30   " + self.main_total_lb_3)

    def blog_title(self):
        return ""+self.zone+"　結果"

    def blog_text(self):
        return ""+self.zone+"　結果\n\n"\
            "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "　"+self.zone+"　の有料配信は"+self.buy+"でした。\n\n"\
            ""+self.zone+" ドル/円結果\n\n"\
            ""+self.main_sign+"pips\n\n"\
            ""+str(CONFIG.result_month())+"月度累計　ドル/円結果\n\n"\
            "9：00→16：30 "+self.main_total_3+"pips　\n\n"\
            "16：30→5：30 "+self.main_total_1+"pips　\n\n"\
            "5：30→9：00 "+self.main_total_2+"pips　\n\n\n\n\n\n"\
            ""+self.zone+"　結果\n\n"\
            "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "　"+self.zone+"　の有料配信は"+self.buy+"でした。\n\n"\
            ""+self.zone+" ユーロ/円結果\n\n"\
            ""+self.main_sign_euro+"pips\n\n"\
            ""+str(CONFIG.result_month())+"月度累計　ユーロ/円結果\n\n"\
            "9：00→16：30 "+self.main_total_euro_3+"pips　\n\n"\
            "16：30→5：30 "+self.main_total_euro_1+"pips　\n\n"\
            "5：30→9：00 "+self.main_total_euro_2+"pips　\n\n\n\n\n\n"\
            ""+self.zone+"　結果\n\n"\
            "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "　"+self.zone+"　の有料配信は"+self.buy+"でした。\n\n"\
            ""+self.zone+" ポンド/円結果\n\n"\
            ""+self.main_sign_lb+"pips\n\n"\
            ""+str(CONFIG.result_month())+"月度累計　ポンド/円結果\n\n"\
            "9：00→16：30 "+self.main_total_lb_3+"pips　\n\n"\
            "16：30→5：30 "+self.main_total_lb_1+"pips　\n\n"\
            "5：30→9：00 "+self.main_total_lb_2+"pips　\n\n\n\n"\
            '有料配信の申込みはこちら　⇒　⇒　　<a href="http: // victorioustradefx.blog.fc2.com/blog-entry-2.html" title="申込み入り口">申込み入り口</a>'


