from .. import all_config as CONFIG


class YugafxText():
    def __init__(self, zone1, zone_state1, zone_state_euro1, zone_state_lb1, zone_state_euro_dol1, zone_state_lb_dol1, main_sign1, main_sign_euro1, main_sign_lb1, main_sign_euro_dol1, main_sign_lb_dol1, main_total1, main_total_euro1, main_total_lb1, main_total_euro_dol1, main_total_lb_dol1, zone_dollar1, zone_euro1, zone_lb1, zone_euro_dol1, zone_lb_dol1, zone_settlement1, zone_settlement_euro1, zone_settlement_lb1, zone_settlement_euro_dol1, zone_settlement_lb_dol1, buy_time1, settlement_time1, zone2, zone_state2, zone_state_euro2, zone_state_lb2, zone_state_euro_dol2, zone_state_lb_dol2, main_sign2, main_sign_euro2, main_sign_lb2, main_sign_euro_dol2, main_sign_lb_dol2, main_total2, main_total_euro2, main_total_lb2, main_total_euro_dol2, main_total_lb_dol2, zone_dollar2, zone_euro2, zone_lb2, zone_euro_dol2, zone_lb_dol2, zone_settlement2, zone_settlement_euro2, zone_settlement_lb2, zone_settlement_euro_dol2, zone_settlement_lb_dol2, buy_time2, settlement_time2):
        self.zone1 = zone1
        self.buy1 = zone_state1
        self.buy_euro1 = zone_state_euro1
        self.buy_lb1 = zone_state_lb1
        self.buy_euro_dol1 = zone_state_euro_dol1
        self.buy_lb_dol1 = zone_state_lb_dol1
        self.main_sign1 = main_sign1
        self.main_sign_euro1 = main_sign_euro1
        self.main_sign_lb1 = main_sign_lb1
        self.main_sign_euro_dol1 = main_sign_euro_dol1
        self.main_sign_lb_dol1 = main_sign_lb_dol1
        self.main_total1 = main_total1
        self.main_total_euro1 = main_total_euro1
        self.main_total_lb1 = main_total_lb1
        self.main_total_euro_dol1 = main_total_euro_dol1
        self.main_total_lb_dol1 = main_total_lb_dol1
        self.zone_dollar1 = zone_dollar1
        self.zone_euro1 = zone_euro1
        self.zone_lb1 = zone_lb1
        self.zone_euro_dol1 = zone_euro_dol1
        self.zone_lb_dol1 = zone_lb_dol1
        self.zone_settlement1 = zone_settlement1
        self.zone_settlement_euro1 = zone_settlement_euro1
        self.zone_settlement_lb1 = zone_settlement_lb1
        self.zone_settlement_euro_dol1 = zone_settlement_euro_dol1
        self.zone_settlement_lb_dol1 = zone_settlement_lb_dol1
        self.buy_time1 = buy_time1
        self.settlement_time1 = settlement_time1

        self.zone2 = zone2
        self.buy2 = zone_state2
        self.buy_euro2 = zone_state_euro2
        self.buy_lb2 = zone_state_lb2
        self.buy_euro_dol2 = zone_state_euro_dol2
        self.buy_lb_dol2 = zone_state_lb_dol2
        self.main_sign2 = main_sign2
        self.main_sign_euro2 = main_sign_euro2
        self.main_sign_lb2 = main_sign_lb2
        self.main_sign_euro_dol2 = main_sign_euro_dol2
        self.main_sign_lb_dol2 = main_sign_lb_dol2
        self.main_total2 = main_total2
        self.main_total_euro2 = main_total_euro2
        self.main_total_lb2 = main_total_lb2
        self.main_total_euro_dol2 = main_total_euro_dol2
        self.main_total_lb_dol2 = main_total_lb_dol2
        self.zone_dollar2 = zone_dollar2
        self.zone_euro2 = zone_euro2
        self.zone_lb2 = zone_lb2
        self.zone_euro_dol2 = zone_euro_dol2
        self.zone_lb_dol2 = zone_lb_dol2
        self.zone_settlement2 = zone_settlement2
        self.zone_settlement_euro2 = zone_settlement_euro2
        self.zone_settlement_lb2 = zone_settlement_lb2
        self.zone_settlement_euro_dol2 = zone_settlement_euro_dol2
        self.zone_settlement_lb_dol2 = zone_settlement_lb_dol2
        self.buy_time2 = buy_time2
        self.settlement_time2 = settlement_time2

        if self.settlement_time2 == "y07:30":
            self.settlement_time2 = "07：30"
        if self.main_sign1 == "0":
            self.main_sign1 = "±0"
        if self.main_sign2 == "0":
            self.main_sign2 = "±0"

        print(zone1)
        print("ドル")
        print(self.buy1 + "   "+str(self.zone_dollar1) +
              "   決済    " + str(self.zone_settlement1) + "")
        print("メイン   " + self.main_sign1+"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total1)
        print("ユーロ")
        print(self.buy_euro1 + "   "+str(self.zone_euro1) +
              "   決済    " + str(self.zone_settlement_euro1) + "")
        print("メイン   " + self.main_sign_euro1+"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total_euro1)
        print("ポンド")
        print(self.buy_lb1 + "   "+str(self.zone_lb1) +
              "   決済    " + str(self.zone_settlement_lb1) + "")
        print("メイン   " + self.main_sign_lb1+"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total_lb1)
        print("ユーロ/ドル")
        print(self.buy_euro_dol1 + "   "+str(self.zone_euro_dol1) +
              "   決済    " + str(self.zone_settlement_euro_dol1) + "")
        print("メイン   " + self.main_sign_euro_dol1+"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total_euro_dol1)
        print("ポンド/ドル")
        print(self.buy_lb_dol1 + "   "+str(self.zone_lb_dol1) +
              "   決済    " + str(self.zone_settlement_lb_dol1) + "")
        print("メイン   " + self.main_sign_lb_dol1+"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total_lb_dol1)

        print(zone2)
        print("ドル")
        print(self.buy2 + "   "+str(self.zone_dollar2) +
              "   決済    " + str(self.zone_settlement2) + "")
        print("メイン   " + self.main_sign2+"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total2)
        print("ユーロ")
        print(self.buy_euro2 + "   "+str(self.zone_euro2) +
              "   決済    " + str(self.zone_settlement_euro2) + "")
        print("メイン   " + self.main_sign_euro2+"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total_euro2)
        print("ポンド")
        print(self.buy_lb2 + "   "+str(self.zone_lb2) +
              "   決済    " + str(self.zone_settlement_lb2) + "")
        print("メイン   " + self.main_sign_lb2+"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total_lb2)
        print("ユーロ/ドル")
        print(self.buy_euro_dol2 + "   "+str(self.zone_euro_dol2) +
              "   決済    " + str(self.zone_settlement_euro_dol2) + "")
        print("メイン   " + self.main_sign_euro_dol2+"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total_euro_dol2)
        print("ポンド/ドル")
        print(self.buy_lb_dol2 + "   "+str(self.zone_lb_dol2) +
              "   決済    " + str(self.zone_settlement_lb_dol2) + "")
        print("メイン   " + self.main_sign_lb_dol2+"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total_lb_dol2)

    def blog_title(self):
        return "投資結果 (" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "　08：00～20：00　・20: 30～　" + str(CONFIG.y_result_month()) + "/" + str(CONFIG.y_result_day()) +"　07：30)"

    def blog_text(self):
        return "投資結果 (" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "　08：00～20：00　・20: 30～　" + str(CONFIG.y_result_month()) + "/" + str(CONFIG.y_result_day()) + "　07：30)\n\n\n"\
            " 取引通貨＊USD/JPY＊\n\n"\
            "08：00（成行売買）～20：00（成行決済）\n"\
            ""+self.buy1+" "+ self.main_sign1+"pips　        今月合計　"+ self.main_total1 +"pips\n\n"\
            "20：30（成行売買）～07：30（成行決済)\n"\
            ""+self.buy2+" " + self.main_sign2 + "pips　          今月合計 　 " + self.main_total2 + "pips\n\n\n"\
            " 取引通貨＊EUR/JPY＊\n\n"\
            "08：00（成行売買）～20：00（成行決済）\n"\
            ""+self.buy_euro1+" " + self.main_sign_euro1+"pips　        今月合計　" + self.main_total_euro1 + "pips\n\n"\
            "20：30（成行売買）～07：30（成行決済)\n"\
            ""+self.buy_euro2+" " + self.main_sign_euro2 + "pips　          今月合計 　 " + self.main_total_euro2 + "pips\n\n\n"\
            " 取引通貨＊GBP/JPY＊\n\n"\
            "08：00（成行売買）～20：00（成行決済）\n"\
            ""+self.buy_lb1+" " + self.main_sign_lb1+"pips　        今月合計　" + self.main_total_lb1 + "pips\n\n"\
            "20：30（成行売買）～07：30（成行決済)\n"\
            ""+self.buy_lb2+" " + self.main_sign_lb2 + "pips　          今月合計 　 " + self.main_total_lb2 + "pips\n\n\n"\
            " 取引通貨＊EUR/USD＊\n\n"\
            "08：00（成行売買）～20：00（成行決済）\n"\
            ""+self.buy_euro_dol1+" " + self.main_sign_euro_dol1+"pips　        今月合計　" + self.main_total_euro_dol1 + "pips\n\n"\
            "20：30（成行売買）～07：30（成行決済)\n"\
            ""+self.buy_euro_dol2+" " + self.main_sign_euro_dol2 + "pips　          今月合計 　 " + self.main_total_euro_dol2 + "pips\n\n\n"\
            " 取引通貨＊GBP/USD＊\n\n"\
            "08：00（成行売買）～20：00（成行決済）\n"\
            ""+self.buy_lb_dol1+" " + self.main_sign_lb_dol1+"pips　        今月合計　" + self.main_total_lb_dol1 + "pips\n\n"\
            "20：30（成行売買）～07：30（成行決済)\n"\
            ""+self.buy_lb_dol2+" " + self.main_sign_lb_dol2 + "pips　          今月合計 　 " + self.main_total_lb_dol2 + "pips\n\n\n"\
            "他の優秀なＦＸブログサイトはこちら"\
            "↓　↓　↓\n"\
            '<a href = "http://fx.blogmura.com/fxsignal/" > にほんブログ村 FX 売買シグナル配信 </a >\n'\
            '<a href = "http://ranking.kuruten.jp/rankin.php" title = "くる天 ブログランキング" target = "_blank" > くる天 人気ブログランキング </a >'
