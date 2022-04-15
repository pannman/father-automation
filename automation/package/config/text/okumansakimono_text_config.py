from .. import all_config as CONFIG


class OkumansakimonoText():
    def __init__(self, zone, buy_gold,buy_platinum, main_sign_gold, main_total_gold, zone_gold, zone_settlement_gold, main_sign_platinum, main_total_platinum, zone_platinum, zone_settlement_platinum, buy_time, settlement_time):
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
            self.settlement_time = "06：30"
        if self.main_sign_gold == "0":
            self.main_sign_gold = "±0"
        if self.main_sign_platinum == "0":
            self.main_sign_platinum = "±0"
        # if self.buy_gold == "買い":
        #     self.settlement_buy_gold = "売り"
        #     self.zone_gold = self.zone_gold
        #     self.zone_settlement_gold = self.zone_settlement_gold
        # if self.buy_gold == "売り":
        #     self.settlement_buy_gold = "買い"
        #     self.zone_gold = self.zone_settlement_gold
        #     self.zone_settlement_gold = self.zone_gold
        # if self.buy_platinum == "買い":
        #     self.settlement_buy_platinum = "売り"
        #     self.zone_platinum = self.zone_platinum
        #     self.zone_settlement_platinum = self.zone_settlement_platinum
        # if self.buy_platinum == "売り":
        #     self.settlement_buy_platinum = "買い"
        #     self.zone_platinum = self.zone_settlement_platinum
        #     self.zone_settlement_platinum = self.zone_platinum
        if self.zone == "夜間":
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
        return "" + str(self.month) + "/" + str(self.day) + "　"+self.zone + "取引結果（億万長者への道）"

    def blog_text(self):
        return "" + str(self.month) + "/" + str(self.day) + "　"+self.zone + "取引結果（億万長者への道）\n\n\n\n"\
            "金（限月2023/2）　\n\n"\
            "始値　"+str(self.zone_gold)+"　終値　"+str(self.zone_settlement_gold)+"\n\n"\
            ""+self.buy_gold+" 　 " + self.main_sign_gold+"　 " + str(self.month) + "月累計　"+self.main_total_gold +"\n\n\n"\
            "白金（限月2023/2）　\n\n"\
            "始値　"+str(self.zone_platinum)+"　終値　"+str(self.zone_settlement_platinum)+"\n\n"\
            ""+self.buy_platinum+" 　 " + self.main_sign_platinum+"　 " + str(self.month) + "月累計　"+self.main_total_platinum + "\n\n\n"
            
