from .. import all_config as CONFIG

class KatigumiText():
    def __init__(self,zone,buy,sub_sign,main_sign,sub_total,main_total):
        self.zone = zone
        self.buy = buy
        self.sub_sign = sub_sign
        self.main_sign = main_sign
        self.sub_total = sub_total
        self.main_total = main_total
        print("メイン   "+main_sign+"   " + str(CONFIG.result_month()) + "月累計   " + main_total)
        print("サブ     "+sub_sign+"   " + str(CONFIG.result_month()) + "月累計   " + sub_total)
    def blog_title(self):
        if self.zone == "日中":
            self.zone_name = "日中"
            return "日中予想☆"
        if self.zone == "ナイトセッション":
            self.zone_name = "夕場"
            return "夕場予想☆"
        if self.zone == "オーバーナイト2":
            self.zone_name = "オーバーナイト"
            return "オーバーナイト予想☆"
    def blog_text(self):
        return  "" + self.zone_name + "予想☆\n\n"\
                "" + self.buy + "です。\n\n"\
                "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "の" + self.zone_name + "結果！\n\n"\
                "本命予想    " + self.main_sign + "　  　" + str(CONFIG.result_month()) + "月成績　" + self.main_total + "\n\n"\
                "無料予想   　 " + self.sub_sign + "　　 " + str(CONFIG.result_month()) + "月成績  " + self.sub_total + "\n\n"\
                "本命予想は、当会員様へ配信させて頂きました。\n幸運を期待します☆\n\n"\
                '予想が参考になりましたら、ランキングをクリックして頂ければうれしいです。'
