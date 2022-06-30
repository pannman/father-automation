from .. import all_config as CONFIG


class SiawaseText():
    def __init__(self, zone, buy, main_sign, main_total,trade_money,settlement_money,result):
        self.zone = zone
        self.buy = buy
        self.main_sign = main_sign
        self.main_total = main_total
        self.trade_money = trade_money
        self.settlement_money = settlement_money
        self.result = result
        print("メイン   "+main_sign+"   " +
              str(CONFIG.result_month()) + "月累計   " + main_total)

    def blog_title(self):
        if self.zone == "日中":
            self.zone_name = "a)日中寄付きで成行売買・日中引けで成行決済"
            self.zone_time = "08：45　～　15：30"
            return "日中結果"
        if self.zone == "ナイトセッション":
            self.zone_name = "b)ナイトセッション寄付きで成行売買・ナイトセッション引けで成行決済"
            self.zone_time = "16：30　～　06：00"

            return "ナイトセッション結果"
        if self.zone == "オーバーナイト":
            self.zone_name = "c)ナイトセッション寄付きで成行売買・日中寄付きで成行決済"
            self.zone_time = "16：30　～　08：45"

            return "オーバーナイト結果"

    def blog_text(self):
        return "＝"+self.zone+"結果＝\n\n"\
            ""+self.zone_name+"\n"\
            ""+self.zone_time+"\n\n"\
            ""+self.trade_money+"で成行買い・"+self.settlement_money+"で成行決済\n\n"\
            "結果    "+self.main_sign+"\n\n"\
            "今日の"+self.zone+"は"+self.result+"でした。\n\n"\
            "今月の"+self.zone+"結果 　　"+self.main_total+"\n\n"\
            "応援クリックお願い！！\n"\
            "↓　↓　↓\n"\
            '<a href = "http://futures.blogmura.com/225/" > にほんブログ村 日経２２５先物 < /a >\n'\
            '<a href = "http://ranking.kuruten.jp/rankin.php" title = "くる天 ブログランキング" target = "_blank" > くる天 人気ブログランキング < /a >\n'

  