from .. import all_config as CONFIG

class SararimanfxText():
    def __init__(self,zone,buy,main_sign,main_total,zone_dollar,zone_settlement,buy_time,settlement_time,signalA_main_total,signalB_main_total,signalC_main_total):
        self.zone = zone
        self.buy = buy
        self.main_sign = main_sign
        self.main_total = main_total
        self.zone_dollar = zone_dollar
        self.zone_settlement = zone_settlement
        self.buy_time = buy_time
        self.settlement_time = settlement_time
        self.signalA_main_total = signalA_main_total
        self.signalB_main_total = signalB_main_total
        self.signalC_main_total = signalC_main_total
        if self.zone == "シグナルA":
            self.info_time = "7：30"
            self.zone_name = "A"
        if self.zone == "シグナルB":
            self.info_time = "16：10"
            self.zone_name = "B"
        if self.zone == "シグナルC":
            self.info_time = "20：10"
            self.zone_name = "C"
        if self.settlement_time == "y07:00":
            self.settlement_time = "07:00"
        if self.main_sign == "0":
            self.main_sign = "±0"
        print(self.buy + "   "+str(self.zone_dollar)+"   決済    "+ str(self.zone_settlement) +"")
        print("メイン   " + self.main_sign+"    " + str(CONFIG.result_month()) + "月累計   " + self.main_total)
    def blog_title(self):
        return "今日の" + self.zone
    def blog_text(self):
        return  "今日の"+self.zone+"（"+self.buy_time +"~"+self.settlement_time+"）サイン\n\n"\
                "有料配信"+self.zone_name+"のシグナルは今日の"+self.info_time +"に配信済です。 \n\n"\
                "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "の" + self.zone + "の結果\n"\
                "(" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "　"+self.buy_time +"）\n"\
                "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "の"+self.zone +"の結果は　"+str(self.zone_dollar)+"(USD/JPY)で"+self.buy+"でした。\n\n"\
                "(" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "　"+self.settlement_time +"）\n"\
                ""+str(self.zone_settlement)+"の決済で、結果は "+self.main_sign+"pipsでした。\n"\
                "注）成行注文の為、読者様が実際の取引をされる場合、若干の誤差が生じます。\n\n"\
                "" + str(CONFIG.result_month()) + "月度の累計結果\n"\
                "A　  "+self.signalA_main_total+"pips　 Ｂ　  "+self.signalB_main_total+"pips　 C 　 "+self.signalC_main_total+"pips"

