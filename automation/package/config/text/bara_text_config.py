from .. import all_config as CONFIG
import math


class BaraText():
    def __init__(self,before_buy,before_main_sign,before_main_total,after_buy,after_main_sign,after_main_total,nightsession_buy,nightsession_main_sign,nightsession_main_total,overnight2_buy,overnight2_main_sign,overnight2_main_total):
        self.before_buy = before_buy
        self.before_main_sign = before_main_sign
        self.before_main_total = before_main_total
        self.after_buy = after_buy
        self.after_main_sign = after_main_sign
        self.after_main_total = after_main_total
        self.nightsession_buy = nightsession_buy
        self.nightsession_main_sign = nightsession_main_sign
        self.nightsession_main_total = nightsession_main_total
        self.overnight2_buy = overnight2_buy
        self.overnight2_main_sign = overnight2_main_sign
        self.overnight2_main_total = overnight2_main_total
        print("前場")
        print("メイン   "+before_main_sign+"   " + str(CONFIG.result_month()) + "月累計   " + before_main_total)
        print("後場")
        print("メイン   "+after_main_sign+"   " + str(CONFIG.result_month()) + "月累計   " + after_main_total)
        print("ナイトセッション")
        print("メイン   "+nightsession_main_sign+"   " + str(CONFIG.result_month()) + "月累計   " + nightsession_main_total)
        print("オーバーナイト2")
        print("メイン   "+overnight2_main_sign+"   " + str(CONFIG.result_month()) + "月累計   " + overnight2_main_total)
    def blog_title(self):
        return "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "の投資結果"
    def blog_text(self):
        return  "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "の投資結果\n\n"\
                "前場\n\n"\
                "8：45　→　11：30　　              　 "+self.before_buy+"　　　　結果　"+ self.before_main_sign+"\n\n"\
                "後場\n\n"\
                "12：30　→　15：15　　              　"+self.after_buy+"　　　　結果　"+ self.after_main_sign+"\n\n"\
                "夜間立会\n\n"\
                "16：30　→　翌日5：30　　              "+self.nightsession_buy+"　　　　結果　"+ self.nightsession_main_sign+"\n\n"\
                "オーバーナイト\n\n"\
                "翌日5：30　→　翌営業日8：45　　        "+self.overnight2_buy+"　　　　結果　"+ self.overnight2_main_sign+"\n\n"\
                "" + str(CONFIG.result_month()) + "月累計投資結果\n\n"\
                "前場　　　　　　　 "+ self.before_main_total+"\n"\
                "後場　　　　　　　 "+ self.after_main_total+"\n"\
                "夜間立会　　　　　 "+ self.nightsession_main_total+"\n"\
                "オーバーナイト　　 "+ self.overnight2_main_total+"\n\n"\
                '配信をご希望される方はこちらへ　→　<a href="http://roselife98.blog.fc2.com/blog-entry-7.html" title="投資予測提供会員詳細内容">投資予測提供会員詳細内容</a>'
