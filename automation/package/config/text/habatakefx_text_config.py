from .. import all_config as CONFIG


class HabatakefxText():
    def __init__(self, zone, zone_state, zone_state_euro, zone_state_lb, main_sign, main_sign_euro, main_sign_lb, main_total, main_total_euro, main_total_lb, zone_dollar, zone_euro, zone_lb, zone_settlement, zone_settlement_euro, zone_settlement_lb, buy_time, settlement_time):
        self.zone = zone
        self.buy = zone_state
        self.buy_euro = zone_state_euro
        self.buy_lb = zone_state_lb
        self.main_sign = main_sign
        self.main_sign_euro = main_sign_euro
        self.main_sign_lb = main_sign_lb
        self.main_total = main_total
        self.main_total_euro = main_total_euro
        self.main_total_lb = main_total_lb
        self.zone_dollar = zone_dollar
        self.zone_euro = zone_euro
        self.zone_lb = zone_lb
        self.zone_settlement = zone_settlement
        self.zone_settlement_euro = zone_settlement_euro
        self.zone_settlement_lb = zone_settlement_lb
        self.buy_time = buy_time
        self.settlement_time = settlement_time
    
        if self.settlement_time == "y09:00":
            self.settlement_time = "09：30"
        if self.main_sign == "0":
            self.main_sign = "±0"
       
        print("ドル")
        print(self.buy + "   "+str(self.zone_dollar) +
              "   決済    " + str(self.zone_settlement) + "")
        print("メイン   " + self.main_sign+"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total)
        print("ユーロ")
        print(self.buy_euro + "   "+str(self.zone_euro) +
              "   決済    " + str(self.zone_settlement_euro) + "")
        print("メイン   " + self.main_sign_euro+"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total_euro)
        print("ポンド")
        print(self.buy_lb + "   "+str(self.zone_lb) +
              "   決済    " + str(self.zone_settlement_lb) + "")
        print("メイン   " + self.main_sign_lb+"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total_lb)

    def blog_title(self):
        return ""+self.zone+"の配信と前営業日の"+self.zone+"の結果"

    def blog_text(self):
        return ""+self.zone+"の配信と前営業日の"+self.zone+"の結果\n\n"\
            "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "\n"\
            ""+self.zone+"の結果（ドル/円）\n\n"\
            ""+self.buy+" "+self.main_sign+"pips   "+str(CONFIG.result_month())+"月トータル　" + self.main_total+"pips\n\n\n"\
            ""+self.zone+"の結果（ユーロ/円）\n\n"\
            ""+self.buy_euro+" "+self.main_sign_euro+"pips   "+str(CONFIG.result_month())+"月トータル　" + self.main_total_euro+"pips\n\n\n"\
            ""+self.zone+"の結果（ポンド/円）\n\n"\
            ""+self.buy_lb+" "+self.main_sign_lb+"pips   "+str(CONFIG.result_month())+"月トータル　" + self.main_total_lb+"pips\n\n\n"