from .. import all_config as CONFIG

class ToshiText():
    def __init__(self,zone,buy,main_sign,main_total):
        self.zone = zone
        self.buy = buy
        self.main_sign = main_sign
        self.main_total = main_total
        if self.zone == "日中":
            self.zone_name = "日中"
        if self.zone == "前場":
            self.zone_name = "前場"
        if self.zone == "後場":
            self.zone_name = "後場"
        if self.zone == "ナイトセッション":
            self.zone_name = "ナイト"
        if self.zone == "オーバーナイト2":
            self.zone_name = "ナイト引け日中寄付き"
        print("メイン   "+main_sign+"   "+ str(CONFIG.result_month()) + "月累計   " + main_total)
    def blog_title(self):
        return "＊"+self.zone_name + "サイン＊"
    def blog_text(self):
        return  "＊"+self.zone_name + "サイン＊\n\n"\
                ""+self.zone_name + "サインは会員様へメール致しました。\n\n"\
                "よろしくお願いします。\n\n"\
                "＊" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "の" + self.zone_name + "結果＊\n\n"\
                '' + str(CONFIG.result_month()) + '/' + str(CONFIG.result_day()) + 'の' + self.zone_name + 'サインは　　</span><span style="font-size:x-large;"><strong>　'+ self.buy + '　　</strong></span></span>でした。\n\n'\
                '<span style="font-size:x-large;">' + self.main_sign + '　</span>\n\n'\
                '' + str(CONFIG.result_month()) +'月の収支は　　　<span style="font-size:x-large;">　'+ self.main_total + '　</span>　　　です。'
