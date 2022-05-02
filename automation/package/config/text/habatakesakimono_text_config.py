from .. import all_config as CONFIG


class HabatakesakimonoText():
    def __init__(self, zone, buy_gold, buy_platinum, main_sign_gold, main_total_gold, zone_gold, zone_settlement_gold, main_sign_platinum, main_total_platinum, zone_platinum, zone_settlement_platinum, buy_time, settlement_time):
        self.zone = zone
        self.buy_gold = buy_gold
        self.buy_platinum = buy_platinum
        self.main_sign_gold = main_sign_gold
        self.main_total_gold = main_total_gold
        self.zone_gold = zone_gold
        self.zone_settlement_gold = zone_settlement_gold
        self.main_sign_platinum = main_sign_platinum
        self.main_total_platinum = main_total_platinum
        self.zone_platinum = zone_platinum
        self.zone_settlement_platinum = zone_settlement_platinum
        self.buy_time = buy_time
        self.settlement_time = settlement_time
        if self.settlement_time == "y06:00":
            self.settlement_time = "06：00"
        if self.settlement_time == "y15:15":
            self.settlement_time = "15：15"
        if self.main_sign_gold == "0":
            self.main_sign_gold = "±0"
        if self.main_sign_platinum == "0":
            self.main_sign_platinum = "±0"
        if self.buy_gold == "買い":
            self.settlement_buy_gold = "売り"
            self.start_price_gold = self.zone_gold
            self.end_price_gold = self.zone_settlement_gold
        if self.buy_gold == "売り":
            self.settlement_buy_gold = "買い"
            self.start_price_gold = self.zone_settlement_gold
            self.end_price_gold = self.zone_gold
        if self.buy_platinum == "買い":
            self.settlement_buy_platinum = "売り"
            self.start_price_platinum = self.zone_platinum
            self.end_price_platinum = self.zone_settlement_platinum
        if self.buy_platinum == "売り":
            self.settlement_buy_platinum = "買い"
            self.start_price_platinum = self.zone_settlement_platinum
            self.end_price_platinum = self.zone_platinum
        if self.zone == "夜間" or self.zone== "日通し":
            self.month = CONFIG.y_result_month()
            self.day = CONFIG.y_result_day()
        else:
            self.month = CONFIG.result_month()
            self.day = CONFIG.result_day()
        print(self.buy_gold + "   "+str(self.zone_gold) +
              "   決済    " + str(self.zone_settlement_gold) + "")
        print("メイン   " + self.main_sign_gold+"    " +
              str(self.month) + "月累計   " + self.main_total_gold)
        print(self.buy_platinum + "   "+str(self.zone_platinum) +
              "   決済    " + str(self.zone_settlement_platinum) + "")
        print("メイン   " + self.main_sign_platinum+"    " +
              str(self.month) + "月累計   " + self.main_total_platinum)

    def blog_title(self):
        return ""+self.zone+"取引の配信と前営業日の"+self.zone+"取引結果"

    def blog_text(self):
        return ""+self.zone+"取引\n\n"\
            "有料読者会員様へ、配信させて頂きました。\n\n"\
            "" + str(self.month) + "/" + str(self.day) + "　"+self.zone + "取引結果("+self.buy_time+"-"+self.settlement_time+"）\n\n"\
            "（金　限月2023/2）　\n\n"\
            ""+self.buy_gold+" 　 \n\n"\
            ""+self.main_sign_gold+"     " + str(self.month) + "月トータル　"+self.main_total_gold+"\n\n"\
            "（白金　限月2023/2）　\n\n"\
            ""+self.buy_platinum+" 　 \n\n"\
            ""+self.main_sign_platinum+"     " + str(self.month) + "月トータル　"+self.main_total_platinum+"\n\n"