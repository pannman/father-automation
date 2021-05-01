from .. import all_config as CONFIG

class SubarashikiText():
    def __init__(self,zone,buy,main_sign,main_total,trade_money,settlement_money):
        self.zone = zone
        self.buy = buy
        self.main_sign = main_sign
        self.main_total = main_total
        self.trade_money = trade_money
        self.settlement_money = settlement_money
        if self.zone == "日中":
            self.zone_name = "日中"
        if self.zone == "前場":
            self.zone_name = "前場"
        if self.zone == "後場":
            self.zone_name = "後場"
        if self.zone == "ナイトセッション":
            self.zone_name = "ナイト"
        if self.zone == "オーバーナイト2":
            self.zone_name = "オーバーナイト"
        print("メイン   "+main_sign+"   "+ str(CONFIG.result_month()) + "月累計   " + main_total)
        print("売買金額   "+str(self.trade_money) +"    決済金額   " + str(self.settlement_money))
    def blog_title(self):
        return "売買シグナル "+self.zone_name
    def blog_text(self):
        return  '売買シグナルは、08：45までにメールさせて頂きました。\n\n'\
                '' + str(CONFIG.result_month()) + '/' + str(CONFIG.result_day()) + '　' + self.zone + 'の結果　08：45　→　11：30\n\n'\
                '売買シグナル   ' + self.buy + '\n\n'\
                '' + self.trade_money + 'で成行きで売買\n\n'\
                '' + self.settlement_money + 'で成行きで決済\n\n'\
                '結果   ' + self.main_sign +'\n\n'\
                '' + str(CONFIG.result_month()) + '月合計' + self.main_total + ''
