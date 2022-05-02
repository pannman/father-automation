from .. import all_config as CONFIG


class SyohinnsakimonoText():
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
        if self.zone == "（16：30　→　06：00）" or self.zone == "（16：30　→　15：15）":
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
        return "本日"+self.zone+"の売買サイン"

    def blog_text(self):
        return "本日"+self.zone+"の売買サイン\n\n"\
            "本日の売買サイン"+self.zone+"を会員様へメールさせて頂きました。\n\n"\
            "" + str(self.month) + "/" + str(self.day) + "\n\n"\
            "金\n\n"\
            ""+self.buy_gold+" 　"+str(self.start_price_gold)+"　→　"+str(self.end_price_gold)+"　"+self.main_sign_gold+" \n\n"\
            "" + str(self.month) + "月トータル結果　"+self.main_total_gold + "\n\n\n"\
            "白金\n\n"\
            ""+self.buy_platinum+" 　"+str(self.start_price_platinum)+"　→　"+str(self.end_price_platinum)+"　"+self.main_sign_platinum+" \n\n"\
            "" + str(self.month) + "月トータル結果　"+self.main_total_platinum + "\n"\
      