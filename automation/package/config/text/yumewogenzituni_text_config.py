from .. import all_config as CONFIG

class YumewogenzituniText():
    def __init__(self,zone,buy,main_sign,main_total,win_total,lose_total,draw_total):
        self.zone = zone
        self.buy = buy
        self.main_sign = main_sign
        self.main_total = main_total
        self.win_total = win_total
        self.lose_total = lose_total
        self.draw_total = draw_total
        if self.zone == "日中":
            self.zone_name = ""
        if self.zone == "前場":
            self.zone_name = "前場"
        if self.zone == "後場":
            self.zone_name = "後場"
    def blog_title(self):
        return str(CONFIG.result_month()) + "月" + str(CONFIG.result_day()) + "日 〜" + self.zone_name +"結果報告〜"
    def blog_text(self):
        return  '<span style="font-size:x-large;">　　　　' + str(CONFIG.result_month()) + '月' + str(CONFIG.result_day()) + '日\n\n'\
                '　 ～' + self.zone_name + '結果報告～</span></strong>\n'\
                '<span style="color:#000099"><strong><span style="font-size:x-large;">\n'\
                '　 ⇒ ' + self.buy + ' ' + self.main_sign + '</span></strong></span>\n'\
                '<strong><span style="font-size:x-large;">\n'\
                '' + str(CONFIG.result_month()) + '月累計結果報告 　' + self.main_total + '\n'\
                '　　　' + str(self.win_total) + '勝' + str(self.lose_total) +'敗'+ str(self.draw_total) + '分</span></strong>\n\n'\
                '↓　↓　↓　応援お願いします　↓　↓　↓\n\n'\
                '<a href="http://futures.blogmura.com/225mini/">にほんブログ村 日経２２５ミニ先物</a></span>\n'\
                '<a href="http://blog.with2.net/link.php?1264131">人気ブログランキングへ</>'