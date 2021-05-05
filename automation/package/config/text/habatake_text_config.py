from .. import all_config as CONFIG

class HabatakeText():
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
        if self.zone == "オーバーナイト1":
            self.zone_name = "オーバーナイトＢ"
        if self.zone == "オーバーナイト2":
            self.zone_name = "オーバーナイトＡ"
        print("メイン   "+main_sign+"   "+ str(CONFIG.result_month()) + "月累計   " + main_total)
    def blog_title(self):
        return ""+self.zone_name+"の配信と前営業日の"+self.zone_name+"結果"
    def blog_text(self):
        return  ""+self.zone_name+"の配信\n\n"\
                "有料読者会員様へ、配信させて頂きました。\n\n"\
                "前営業日の"+self.zone_name+"結果\n\n"\
                ""+self.main_sign+"　　"+ str(CONFIG.result_month()) +"月トータル" + self.main_total+""
