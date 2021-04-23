from .. import all_config as CONFIG

class SakusesunikkiText():
    def __init__(self,zone,buy,sub_sign,main_sign,sub_total,main_total):
        self.zone = zone
        self.buy = buy
        self.sub_sign = sub_sign
        self.main_sign = main_sign
        self.sub_total = sub_total
        self.main_total = main_total
        
    def blog_title(self):
        if self.zone == "日中":
            self.zone_name = ""
            return "サブシグナル！"
        if self.zone == "ナイトセッション":
            self.zone_name = "夕場"
            return "夕場サブシグナル！"
        if self.zone == "オーバーナイト2":
            self.zone_name = "オーバーナイト"
            return "オーバーナイトサブシグナル!"
        return "本日の" + self.zone + "サブナイン!"
    def blog_text(self):
        return  "" + self.zone_name + "サブシグナル！\n\n"\
                "" + self.buy + "\n\n"\
                "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "の" + self.zone_name + "結果！\n\n"\
                "サブシグナル   　 " + self.sub_sign + "　　 " + str(CONFIG.result_month()) + "月収支累計  " + self.sub_total + "\n\n"\
                "メインシグナル    " + self.main_sign + "　  　" + str(CONFIG.result_month()) + "月収支累計　" + self.main_total + "\n\n"\
                "ご協力お願いします！\n"\
                '<a href="http://futures.blogmura.com/225mini/"><img src="http://futures.blogmura.com/225mini/img/225mini150_49.gif" width="88" height="31" border="0" alt="にほんブログ村 先物取引ブログ 日経２２５ミニ先物へ" /></a> <a href="http://blog.with2.net/link.php?952953"><img src="http://image.with2.net/img/banner/banner_22.gif" width="88" height="31" border="0" alt="人気ブログランキングへ"></a><a href="http://futures.blogmura.com/225mini/"><a href="http://futures.blogmura.com/225mini/"></a> <a href="http://blogranking.fc2.com/in.php?id=478645" target="_blank"><img src="http://blogranking.fc2.com/ranking_banner/d_02.gif" style="border:0px"></a>'

