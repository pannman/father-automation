from .. import all_config as CONFIG

class YugaText():
    def __init__(self,zone,buy,main_sign,main_total,self_money,self_money_total):
        self.zone = zone
        self.buy = buy
        self.main_sign = main_sign
        self.main_total = main_total
        self.self_money = self_money
        self.self_money_total = self_money_total
        print("メイン   "+main_sign+"   " + str(CONFIG.result_month()) + "月累計   " + main_total)
        print("自己投資   "+self_money+"万円   " + str(CONFIG.result_month()) + "月累計   " + self_money_total + "万円")
    def blog_title(self):
        if self.zone == "日中":
            self.zone_name = ""
        if self.zone == "ナイトセッション":
            self.zone_name = "夕場"
        if self.zone == "オーバーナイト2":
            self.zone_name = "オーバーナイト"
        return "今日の" + self.zone_name + "売買！！"
    def blog_text(self):
        return  "今日の" + self.zone_name + "売買！！\n\n"\
                "" + self.zone_name + "寄付きシグナルを当会員様へメール配信させて頂きました。\n\n"\
                "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "の" + self.zone_name + "結果\n\n"\
                "" + self.main_sign + "\n\n"\
                "" + str(CONFIG.result_month()) + "月結果＊"+ self.zone_name +"＊\n\n"\
                "" + self.main_total + "\n\n"\
                "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "は" + self.buy + "3枚でした。\n\n"\
                "" + self.self_money + "万円\n\n"\
                "" + str(CONFIG.result_month()) + "月自己結果＊"+ self.zone_name +"＊\n\n"\
                "" + self.self_money_total + "万円\n\n"\
                "ランキングに参加していますので、ご協力お願いします！\n"\
                '<p><a href="http://futures.blogmura.com/225/"><img src="http://futures.blogmura.com/225/img/22588_31.gif" width="88" height="31" border="0" alt="にほんブログ村 先物取引ブログ 日経２２５先物へ" /></a>&nbsp;<a href="http://blog.with2.net/link.php?1263648" title="人気ブログランキングへ"><img src="http://image.with2.net/img/banner/banner_23.gif" width="88" height="31" border="0" /></a></p>'
