from .. import all_config as CONFIG

class MegamiText():
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
            self.zone_name = ""
        if self.zone == "ナイトセッション":
            self.zone_name = "夕場"
        if self.zone == "オーバーナイト2":
            self.zone_name = "オーバーナイト"
        return "今日の" + self.zone_name + "サブシグナル!"
    def blog_text(self):
        return  "今日の" + self.zone_name + "サブシグナル！\n\n"\
                "" + self.buy + "だよ〜ん!\n\n"\
                "メインはメールしました!!\n\n"\
                "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "の" + self.zone_name + "結果！\n\n"\
                "サブシグナル   　 " + self.sub_sign + "　　 " + str(CONFIG.result_month()) + "月収損益  " + self.sub_total + "\n\n"\
                "メインシグナル    " + self.main_sign + "　  　" + str(CONFIG.result_month()) + "月収損益　" + self.main_total + "\n\n"\
                '<p>協力してね！！<br /><a href="http://futures.blogmura.com/225/"><img height="31" alt="にほんブログ村 先物取引ブログ 日経２２５先物へ" src="http://futures.blogmura.com/225/img/22588_31.gif" width="88" border="0" complete="true" /></a> <a href="http://blog.with2.net/link.php?1264105"><img height="31" alt="人気ブログランキングへ" src="http://image.with2.net/img/banner/banner_22.gif" width="88" border="0" complete="true" /></a> <a href="http://blogranking.fc2.com/in.php?id=479647" target="_blank"><img height="30" src="http://blogranking.fc2.com/ranking_banner/d_02.gif" width="88" complete="true" style="BORDER-TOP-WIDTH: 0px; BORDER-LEFT-WIDTH: 0px; BORDER-BOTTOM-WIDTH: 0px; BORDER-RIGHT-WIDTH: 0px" /></a></p>'
