from .. import all_config as CONFIG

class MiraienotyousennfxText():
    def __init__(self,zone,buy,main_sign,main_total,zone_dollar,zone_settlement,buy_time,settlement_time,all_main_total):
        self.zone = zone
        self.buy = buy
        self.main_sign = main_sign
        self.main_total = main_total
        self.zone_dollar = zone_dollar
        self.zone_settlement = zone_settlement
        self.buy_time = buy_time
        self.settlement_time = settlement_time
        self.all_main_total = all_main_total
        if self.settlement_time == "y09:00":
            self.settlement_time = "09：00"
        if self.main_sign == "0":
            self.main_sign = "±0"
        if self.buy == "買い":
            self.settlement_buy = "売り"
        if self.buy == "売り":
            self.settlement_buy = "買い"
        print(self.buy + "   "+str(self.zone_dollar)+"   決済    "+ str(self.zone_settlement) +"")
        print("メイン   " + self.main_sign+"    " + str(CONFIG.result_month()) + "月累計   " + self.main_total)
    def blog_title(self):
        return "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) +"　("+self.zone +"）"
    def blog_text(self):
        return  "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) +"　("+self.zone +"）の結果です。\n\n"\
                "" + self.buy_time + "("+ self.buy + ")　" + str(self.zone_dollar) +"　→　"+ self.settlement_time +"（決済）　"+ str(self.zone_settlement)+"\n\n"\
                "" + self.main_sign + "pips\n\n"\
                "" + str(CONFIG.result_month())+"月 ("+ self.zone + ")累計損益 " + self.main_total+"pips\n"\
                "" + str(CONFIG.result_month())+"月 （09：00→21：00・21：00→09：00）累計損益 " + self.all_main_total+"pips"
               