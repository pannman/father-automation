from .. import all_config as CONFIG


class TradesisutemuText():
    def __init__(self, zone, buy, main_sign, main_total, trade_money, settlement_money, all_main_total):
        self.zone = zone
        self.buy = buy
        self.main_sign = main_sign
        self.main_total = main_total
        self.trade_money = trade_money
        self.settlement_money = settlement_money
        self.all_main_total = all_main_total

        print("メイン   "+main_sign+"   " +
              str(CONFIG.result_month()) + "月累計   " + main_total)
        print("売買金額   "+str(self.trade_money) +
              "    決済金額   " + str(self.settlement_money))

    def blog_title(self):
        return ''+self.zone+'の予想情報結果'

    def blog_text(self):
        return ''+self.zone+'の予想情報結果\n\n'\
            ''+self.zone+'の仕掛け　 　 '+self.trade_money+'で'+self.buy+'\n\n'\
            '結果　　　　　 　 '+self.settlement_money+'で決済\n\n'\
            ''+self.main_sign+'の勝ちでした。\n\n'\
            '' + str(CONFIG.result_month()) + '月の'+self.zone+'累計は　'+self.main_total+'です。\n\n'\
            '' + str(CONFIG.result_month()) + '月の日中・ナイトセッション・オーバーナイトのトータル　'+self.all_main_total+'です。'
