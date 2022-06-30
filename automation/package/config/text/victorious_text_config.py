from .. import all_config as CONFIG


class VictoriousText():
    def __init__(self, zone, buy, main_sign, main_total_1,main_total_2,main_total_3):
        self.zone = zone
        self.buy = buy
        self.main_sign = main_sign
        self.main_total_1 = main_total_1
        self.main_total_2 = main_total_2
        self.main_total_3 = main_total_3
        print("メイン   "+main_sign+"   " +
              str(CONFIG.result_month()) + "月累計   " + main_total_1)

    def blog_title(self):
        if self.zone == "日中":
            self.zone_name = "日中"
            self.zone_time = "（8:45）"
            return "日中結果"
        if self.zone == "夜間立会":
            self.zone_name = "夜間立会"
            self.zone_time = "（16:30）"
            return "夜間立会結果"
        if self.zone == "夜間立会引け":
            self.zone_name = "夜間立会引け日中寄付き"
            self.zone_time = "（5：30）"
            return "夜間立会引け日中寄付き結果"

    def blog_text(self):
        return "" + self.zone_name + "結果\n\n"\
            "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + self.zone_time+"の夜間立会の有料配信は"+self.buy+"でした。\n\n"\
            "" + self.zone_name + "結果　"+str(self.main_sign)+"\n\n"\
            "6月度累計\n\n"\
            "日中　"+str(self.main_total_1)+"　夜間立会　"+str(self.main_total_2)+"　夜間立会引け日中寄付き "+str(self.main_total_3)+"\n\n"\
            '有料配信の申込みはこちら　⇒　⇒　　<a href="http://victorioustrade.blog.fc2.com/blog-category-4.html" title="申込み入り口">申込み入り口</a>'
