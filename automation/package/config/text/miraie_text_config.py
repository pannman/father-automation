from .. import all_config as CONFIG

class MiraieText():
    def __init__(self,zone,buy,main_sign,main_total,trade_money,settlement_money,all_main_total):
        self.zone = zone
        self.buy = buy
        self.main_sign = main_sign
        self.main_total = main_total
        self.trade_money = trade_money
        self.settlement_money = settlement_money
        self.all_main_total = all_main_total
        if self.zone == "日中":
            self.zone_name = "日中"
        if self.zone == "ナイトセッション":
            self.zone_name = "夜間"
        print("メイン   "+main_sign+"   "+ str(CONFIG.result_month()) + "月累計   " + main_total)
        print("売買金額   "+str(self.trade_money) +"    決済金額   " + str(self.settlement_money))
    def blog_title(self):
        return '' + str(CONFIG.result_month()) + '/' + str(CONFIG.result_day()) + 'の' + self.zone_name + '結果です。'
    def blog_text(self):
        return  '' + str(CONFIG.result_month()) + '/' + str(CONFIG.result_day()) + 'の' + self.zone_name + '結果です。\n\n'\
                '' + self.trade_money + ' ('+self.buy+') →' + self.settlement_money + ' (決済)\n\n'\
                '' + self.main_sign + '\n\n'\
                '' + str(CONFIG.result_month()) + '月（'+self.zone_name+'）累計損益 '+self.main_total+'\n\n'\
                '' + str(CONFIG.result_month()) + '月（日中・夜間）累計損益 '+self.all_main_total+''
