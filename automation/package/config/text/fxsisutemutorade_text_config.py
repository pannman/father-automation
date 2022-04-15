from .. import all_config as CONFIG


class FxsisutemutoradeText():
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

        if self.buy ==  "買い":
            self.buy = "ASK"
        if self.buy == "売り":
            self.buy = "BID"
        if self.buy_euro ==  "買い":
            self.buy_euro = "ASK"
        if self.buy_euro == "売り":
            self.buy_euro = "BID"
        if self.buy_lb ==  "買い":
            self.buy_lb = "ASK"
        if self.buy_lb == "売り":
            self.buy_lb = "BID"

        if self.zone == "トレード結果（09：00→16：30）":
            self.month = str(CONFIG.reserve_month())
            self.day = str(CONFIG.reserve_day())
        else:
            self.month = str(CONFIG.result_month())
            self.day = str(CONFIG.result_day())


        if self.settlement_time == "y09:00":
            self.settlement_time = "09：30"
        if self.settlement_time == "y16:30":
            self.settlement_time = "16：30"
        if self.buy_time == "y09:00":
            self.buy_time = "09：00"
        if self.buy_time == "y16:30":
            self.buy_time = "16：30"

        if self.main_sign == "0":
            self.main_sign = "±0"

        print("ドル")
        print(self.buy + "   "+str(self.zone_dollar) +
              "   決済    " + str(self.zone_settlement) + "")
        print("メイン   " + self.main_sign+"    " +
              self.month + "月累計   " + self.main_total)
        print("ユーロ")
        print(self.buy_euro + "   "+str(self.zone_euro) +
              "   決済    " + str(self.zone_settlement_euro) + "")
        print("メイン   " + self.main_sign_euro+"    " +
              self.month + "月累計   " + self.main_total_euro)
        print("ポンド")
        print(self.buy_lb + "   "+str(self.zone_lb) +
              "   決済    " + str(self.zone_settlement_lb) + "")
        print("メイン   " + self.main_sign_lb+"    " +
              self.month + "月累計   " + self.main_total_lb)

    def blog_title(self):
        return "" + self.month + "/" + self.day + "　"+self.zone+""

    def blog_text(self):
        return "" + self.month + "/" + self.day + "　"+self.zone+"\n\n"\
            "ドル/円　("+self.buy+"）\n\n"\
            ""+str(self.zone_dollar)+"　→　"+str(self.zone_settlement) + "\n\n"\
            ""+self.main_sign+"pips\n\n"\
            ""+self.month+"月累計　" + self.main_total+"pips\n\n\n"\
            "ユーロ/円　("+self.buy_euro+"）\n\n"\
            ""+str(self.zone_euro)+"　→　"+str(self.zone_settlement_euro) + "\n\n"\
            ""+self.main_sign_euro+"pips\n\n"\
            ""+self.month+"月累計　" + \
            self.main_total_euro+"pips\n\n\n"\
            "ポンド/円　("+self.buy_lb+"）\n\n"\
            ""+str(self.zone_lb)+"　→　"+str(self.zone_settlement_lb) + "\n\n"\
            ""+self.main_sign_lb+"pips\n\n"\
            ""+self.month+"月累計　" + \
            self.main_total_lb+"pips\n\n\n"
