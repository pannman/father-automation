from .. import all_config as CONFIG


class FxtecunikaruyuroText():
    def __init__(self, zone, buy, main_sign, main_total, zone_euro, zone_settlement, buy_time, settlement_time):
        self.zone = zone
        self.buy = buy
        self.main_sign = main_sign
        self.main_total = main_total
        self.zone_euro = zone_euro
        self.zone_settlement = zone_settlement
        self.buy_time = buy_time
        self.settlement_time = settlement_time
        if self.settlement_time == "y08:30":
            self.settlement_time = "08:30"
        if self.settlement_time == "y15:30":
            self.settlement_time = "15:30"
        if self.main_sign == "0":
            self.main_sign = "±0"
        if self.buy == "買い":
            self.settlement_buy = "売り"
        if self.buy == "売り":
            self.settlement_buy = "買い"
        print(self.buy + "   "+str(self.zone_euro) +
              "   決済    " + str(self.zone_settlement) + "")
        print("メイン   " + self.main_sign+"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total)

    def blog_title(self):
        return self.zone

    def blog_text(self):
        return "前営業日の結果！！\n\n"\
            "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "\n"\
            ""+self.buy_time+"　成行で"+self.buy+"でした。"+str(self.zone_euro)+"pips by ユーロ\n\n"\
            "↓　↓　↓\n\n"\
            "" + str(CONFIG.y_result_month()) + "/" + str(CONFIG.y_result_day()) + "\n"\
            ""+self.settlement_time+"　成行で決済しました。"+str(self.zone_settlement)+"pips by ユーロ\n\n"\
            "結果　　"+self.main_sign + "pips　\n\n"\
            ""+str(CONFIG.result_year()) + "年"+str(CONFIG.result_month()) + "月の月間結果　" + self.main_total+"pips　（"+self.buy_time+"　→　"+self.settlement_time+"）　\n\n\n"\
            "今日の予想！！\n\n"\
            "↓　↓　↓\n\n"\
            '<a href = "http://fxtechnicalanalysisu.blog.fc2.com/blog-entry-3.html" title = "ブログ内容と申込みの詳細" > ブログ内容と申込みの詳細 </a>\n\n'\
            "ポチっとご協力お願いします！！！\n\n"\
            '<a href = "http://fx.blogmura.com/fxsignal/"><img src = "http://fx.blogmura.com/fxsignal/img/fxsignal88_31.gif" width = "88" height = "31" border = "0" alt = "にほんブログ村 為替ブログ FX 売買シグナル配信へ" /></a><br/><a href = "http://fx.blogmura.com/fxsignal/"> </a>\n'
