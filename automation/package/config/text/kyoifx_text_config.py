from .. import all_config as CONFIG

class KyoifxText():
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
        if self.settlement_time == "y07:00":
            self.settlement_time = "翌営業日07：00"
        if self.main_sign == "0":
            self.main_sign = "±0"
        print(self.buy + "   "+str(self.zone_dollar)+"   決済    "+ str(self.zone_settlement) +"")
        print("メイン   " + self.main_sign+"    " + str(CONFIG.result_month()) + "月累計   " + self.main_total)
    def blog_title(self):
        if self.zone == "パターン1":
            self.zone_name = "パターン①"
        if self.zone == "パターン2":
            self.zone_name = "パターン②"
        if self.zone == "パターン3":
            self.zone_name = "パターン③"
        return "本日の" + self.zone
    def blog_text(self):
        return  "本日の"+self.zone_name+"の売買サイン【"+self.buy_time +"（成行売買）　⇒　"+self.settlement_time+"（成行返済）】\n\n"\
                "当会員様へ配信さて頂きました。\n\n"\
                "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "の" + self.zone_name + "の売買結果（"+self.buy_time +"　⇒　翌営業日"+self.settlement_time+"）\n\n"\
                "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "の"+self.buy_time +"に成行きで"+self.buy+"でした。\n"\
                ""+self.buy_time +"（"+self.buy+"）"+str(self.zone_dollar)+"円（USD/JPY)\n\n"\
                "↓　↓\n\n"\
                "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "の"+self.settlement_time+"に成行きで決済しました。\n"\
                ""+self.settlement_time+"（成行返済）"+str(self.zone_settlement) +"円（USD/JPY)\n\n"\
                "結果 "+self.main_sign +"pips\n\n"\
                "" + str(CONFIG.result_month()) + "月" + self.zone_name + "トータル結果 "+self.main_total +"pips\n\n"\
                "" + str(CONFIG.result_month()) + "月パターン①②③トータル結果 "+self.all_main_total +"pips"

