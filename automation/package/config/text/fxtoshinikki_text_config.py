from .. import all_config as CONFIG

class FxtoshinikkiText():
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
        print(self.buy + "   "+str(self.zone_dollar)+"   決済    "+ str(self.zone_settlement) +"")
        print("メイン   " + self.main_sign+"    " + str(CONFIG.result_month()) + "月累計   " + self.main_total)
    def blog_title(self):
        return "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) +"　投資結果"
    def blog_text(self):
        return  "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "投資結果 \n\n"\
                "通貨・・ドル円\n"\
                "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "　"+self.buy_time +"成行きで"+self.buy +"\n"\
                ""+ str(self.zone_dollar)+" \n\n"\
                "" + str(CONFIG.reserve_month()) + "/" + str(CONFIG.reserve_day()) + "　"+self.settlement_time +"成行き決済\n"\
                ""+ str(self.zone_settlement)+" \n\n"\
                "結果　　"+self.main_sign +"pips\n\n"\
                "" + str(CONFIG.result_month()) + "月累計 " +self.main_total +"pips\n\n"\
                '<a href="//fx.blogmura.com/fxsignal/ranking.html"><img src="//fx.blogmura.com/fxsignal/img/fxsignal88_31.gif" width="88" height="31" border="0" alt="にほんブログ村 為替ブログ FX 売買シグナル配信へ" /></a><br /><a href="//fx.blogmura.com/fxsignal/ranking.html"></a>'
