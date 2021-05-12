from .. import all_config as CONFIG

class OkumanfxText():
    def __init__(self,zone,buy,main_sign,main_total,zone_dollar,zone_settlement,buy_time,settlement_time):
        self.zone = zone
        self.buy = buy
        self.main_sign = main_sign
        self.main_total = main_total
        self.zone_dollar = zone_dollar
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
        print(self.buy + "   "+str(self.zone_dollar)+"   決済    "+ str(self.zone_settlement) +"")
        print("メイン   " + self.main_sign+"    " + str(CONFIG.result_month()) + "月累計   " + self.main_total)
    def blog_title(self):
        return "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) +"　"+self.zone
    def blog_text(self):
        return  "ドル/円\n\n"\
                "" + self.zone+ "\n"\
                "成行き"+self.buy +"売買　"+str(self.zone_dollar) +"\n\n"\
                "成行き"+self.settlement_buy +"売買　"+str(self.zone_settlement)  +"\n\n"\
                "結果　　"+self.main_sign +"pips　" + str(CONFIG.result_month()) + "月累計" +self.main_total +"pips"
