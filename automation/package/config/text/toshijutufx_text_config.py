from .. import all_config as CONFIG

class ToshijutufxText():
    def __init__(self,zone,buy,main_sign,main_total,zone_dollar,zone_settlement,buy_time,settlement_time,all_main_total):
        self.zone = zone
        self.buy = buy
        self.main_sign = main_sign
        self.main_total = main_total
        self.zone_dollar = zone_dollar
        self.zone_settlement = zone_settlement
        self.buy_time = buy_time
        self.settlement_time = settlement_time
        self.all_main_total = all_main_total
        if self.settlement_time == "y07:30":
            self.settlement_time = "07：30"
        if self.main_sign == "0":
            self.main_sign = "±0"
        print(self.buy + "   "+str(self.zone_dollar)+"   決済    "+ str(self.zone_settlement) +"")
        print("メイン   " + self.main_sign+"    " + str(CONFIG.result_month()) + "月累計   " + self.main_total)
    def blog_title(self):
        return "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + self.zone +""
    def blog_text(self):
        return  "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + self.zone +"結果　〈USD/JPY〉 \n\n"\
                "（"+self.buy_time +"　"+self.buy +"）"+ str(self.zone_dollar)+"pips  ⇒　（"+self.settlement_time+"　返済）"+str(self.zone_settlement)+"pips \n\n"\
                "結果 "+self.main_sign +"pips\n\n"\
                "" + str(CONFIG.result_month()) + "月" + self.zone + "の累計結果 \n\n"\
                ""+self.main_total +"pips\n\n"\
                "" + str(CONFIG.result_month()) + "月（8：30　⇒　15：30）（16：30　⇒　20：00）（21：00　⇒　7：30）の累計合計結果　 \n\n"\
                ""+self.all_main_total +"pips\n\n"\
                '<a href="http://fxtradesain.blog.fc2.com/blog-entry-6.html" target="_blank" title="～取引内容の説明～">取引の詳細はこちらをクリックして下さい　⇒　⇒　～取引の詳細～</a>'
