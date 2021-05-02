from .. import all_config as CONFIG

class OkumanText():
    def __init__(self,zone,buy,main_sign,day_main_total,nightsession_main_total,overnight2_main_total,total_profit,day_main_sign,day_buy):
        self.zone = zone
        self.buy = buy
        self.main_sign = main_sign
        self.day_main_total = day_main_total
        self.nightsession_main_total = nightsession_main_total
        self.overnight2_main_total = overnight2_main_total
        self.total_profit = total_profit
        self.day_main_sign = day_main_sign
        self.day_buy = day_buy
        if self.zone == "日中":
            self.main_total = day_main_total
        if self.zone == "ナイトセッション":
            self.main_total = nightsession_main_total
        if self.zone == "オーバーナイト2":
            self.main_total = overnight2_main_total
        print("メイン   "+main_sign+"   " + str(CONFIG.result_month()) + "月累計   " + self.main_total)
        print("ブログ公開後トータル損益   "+"{:,}".format(self.total_profit))
    def blog_title(self):
        if self.zone == "日中":
            self.zone_name = "日中"
        if self.zone == "ナイトセッション":
            self.zone_name = "夕場"
        if self.zone == "オーバーナイト2":
            self.zone_name = "オーバーナイト"
        return "" + str(CONFIG.result_month()) + "月" + str(CONFIG.result_day()) + "日" + self.zone_name + "結果"
    def blog_text(self):
        if self.zone == "日中":
            return  "" + str(CONFIG.result_month()) + "月" + str(CONFIG.result_day()) + "日結果\n\n"\
                    ""+self.zone_name+"　" + self.main_sign + "（" + self.day_buy + "）\n\n"\
                    "" + str(CONFIG.result_month()) + "月トータル損益\n\n"\
                    "日中　計" + self.day_main_total + "\n\n"\
                    "夕場　計" + self.nightsession_main_total + "   オーバーナイト　計" + self.overnight2_main_total + "\n\n"\
                    "ブログ公開後トータル損益   "+ "{:,}".format(self.total_profit) +"円\n\n"\
                    "（ラージ1枚、手数料692円、元金100万円、2010年10月18日より)"
        else:
            return  "" + str(CONFIG.result_month()) + "月" + str(CONFIG.result_day()) + "日結果\n\n"\
                    "日中　" + self.day_main_sign + "（" + self.buy + "）\n\n"\
                    ""+self.zone_name+"　" + self.main_sign + "（" + self.day_buy + "）\n\n"\
                    "" + str(CONFIG.result_month()) + "月トータル損益\n\n"\
                    "日中　計" + self.day_main_total + "\n\n"\
                    "夕場　計" + self.nightsession_main_total + "   オーバーナイト　計" + self.overnight2_main_total + "\n\n"\
                    "ブログ公開後トータル損益   "+ "{:,}".format(self.total_profit) +"円\n\n"\
                    "（ラージ1枚、手数料692円、元金100万円、2010年10月18日より)"

