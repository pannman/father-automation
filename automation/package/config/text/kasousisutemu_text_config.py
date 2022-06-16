from .. import all_config as CONFIG


class KasousisutemuText():
    def __init__(self, zone, buy, main_sign, main_total, zone_bit, zone_settlement, buy_time, settlement_time):
        self.zone = zone
        self.buy = buy
        self.main_sign = main_sign
        self.main_total = main_total
        self.zone_bit = zone_bit
        self.zone_settlement = zone_settlement
        self.buy_time = buy_time
        self.settlement_time = settlement_time
        if self.settlement_time == "y09:00":
            self.settlement_time = "09：30"
        if self.main_sign == "0":
            self.main_sign = "±0"
        if self.buy == "買い":
            self.settlement_buy = "売り"
        if self.buy == "売り":
            self.settlement_buy = "買い"
        self.t_day = "" + str(CONFIG.result_month()) +  "/" + str(CONFIG.result_day()) + ""
        self.y_day = "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + ""
        if self.zone == "21：00　→　09：00":
            self.y_day = "" + str(CONFIG.y_result_month()) +  "/" + str(CONFIG.y_result_day()) + ""
        print(self.buy + "   "+str(self.zone_bit) +
              "   決済    " + str(self.zone_settlement) + "")
        print("メイン   " + self.main_sign+"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total)

    def blog_title(self):
        return "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "　"+self.zone+"　の結果"

    def blog_text(self):
        return "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "　"+self.zone+"　の結果\n\n"\
            "(BTC/JPY)\n"\
            ""+self.t_day+"　  "+self.buy_time+"（成行き売り）\n"\
            "" + "{:,}".format(self.zone_bit) + "\n\n"\
            ""+self.y_day+"　  "+self.settlement_time+"（成行き売り）\n"\
            "" + "{:,}".format(self.zone_settlement) + "\n\n"\
            "結果　　"+self.main_sign + "　(BTC/JPY)pips　\n\n"\
            ""+str(CONFIG.result_month()) + "月累計　" + self.main_total + "(BTC/JPY)\n\n"\
            " ＊成行き売買の為、若干の誤差が生じます。"
