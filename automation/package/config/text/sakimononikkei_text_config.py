from .. import all_config as CONFIG

class SakimononikkeiText():
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
        if self.zone == "ナイトセッション":
            return "ナイトセッション"
        elif self.zone == "オーバーナイト1":
            return "オーバーナイトサブサイン1"
        elif self.zone == "オーバーナイト2":
            return "オーバーナイトサブサイン2"
        else:
            return "本日の" + self.zone + "サブサイン!"
    def blog_text(self):
        if self.zone == "ナイトセッション":
            return  ""+ self.zone + "本日のサブサイン! \n\n" + self.zone + "寄り付きで" + self.buy + "です。\n\n" + self.zone + "引けで決済します。\n\n"\
                    "メインのサインは、当会員様へメールで配信させて頂きました！\nよろしくお願いします！\n\n"\
                    "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "の" + self.zone + "結果！\n\n"\
                    "サブサイン   　 " + self.sub_sign + "　　 " + str(CONFIG.result_month()) + "月収支累計  " + self.sub_total + "\n\n"\
                    "メインサイン    " + self.main_sign + "　  　" + str(CONFIG.result_month()) + "月収支累計　" + self.main_total + "\n\nポチっとよろしくお願いします！\n\n"\
                    '<a href="http://futures.blogmura.com/225mini/"><img src="http://futures.blogmura.com/225mini/img/225mini150_49.gif" width="88" height="31" border="0" alt="にほんブログ村 先物取引ブログ 日経２２５ミニ先物へ" /></a> <a href="http://blog.with2.net/link.php?927061"><img src="http://image.with2.net/img/banner/banner_22.gif" width="88" height="31" border="0" alt="人気ブログランキングへ"></a><a href="http://futures.blogmura.com/225mini/"><a href="http://futures.blogmura.com/225mini/"></a> <a href="http://blogranking.fc2.com/in.php?id=463399" target="_blank"><img src="http://blogranking.fc2.com/ranking_banner/d_02.gif" style="border:0px;"></a>\n\n'\
                    "お知らせ！！\n\n会員様、読者様には大変お世話になっております。\n\n"\
                    "この度、会員様、読者様のご要望に答えまして、2011/9/22より、" + self.zone + "の取引に加えて、前場と後場の取引も追加させて頂きます。\n\n"\
                    "会員募集！！\n\n長年の研究の成果から作り上げた独自のシステムをもとに、当会員になられた方に、寄引けシステムのメインサインをメールで配信させて頂きます。サインは買い・売り・見送りの3つです。\n\n"\
                    "サブのサインは、無料公開させて頂きます。\n\n詳細は、会員募集からご覧ください。\n\n私と幸せを分かち合いましょう！\n\n"
        elif self.zone == "オーバーナイト1":
            return  "" + self.zone + "サブサイン！\n\nナイトセッション寄り付きで" + self.buy + "です。\n\n"\
                    "メインのサインは、当会員様へメールで配信させて頂きました！\nよろしくお願いします！\n\n"\
                    "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "の" + self.zone + "結果！\n\n"\
                    "サブサイン   　 " + self.sub_sign + "　　 " + str(CONFIG.result_month()) + "月収支累計  " + self.sub_total + "\n\n"\
                    "メインサイン    " + self.main_sign + "　  　" + str(CONFIG.result_month()) + "月収支累計　" + self.main_total + "\n\nポチっとよろしくお願いします！\n\n"\
                    '<a href="http://futures.blogmura.com/225mini/"><img src="http://futures.blogmura.com/225mini/img/225mini150_49.gif" width="88" height="31" border="0" alt="にほんブログ村 先物取引ブログ 日経２２５ミニ先物へ" /></a> <a href="http://blog.with2.net/link.php?927061"><img src="http://image.with2.net/img/banner/banner_22.gif" width="88" height="31" border="0" alt="人気ブログランキングへ"></a><a href="http://futures.blogmura.com/225mini/"><a href="http://futures.blogmura.com/225mini/"></a> <a href="http://blogranking.fc2.com/in.php?id=463399" target="_blank"><img src="http://blogranking.fc2.com/ranking_banner/d_02.gif" style="border:0px;"></a>\n\n'\
                    "お知らせ！！\n\n会員様、読者様には大変お世話になっております。\n\n"\
                    "この度、会員様、読者様のご要望に答えまして、2011/9/22より、" + self.zone + "の取引に加えて、前場と後場の取引も追加させて頂きます。\n\n"\
                    "会員募集！！\n\n長年の研究の成果から作り上げた独自のシステムをもとに、当会員になられた方に、寄引けシステムのメインサインをメールで配信させて頂きます。サインは買い・売り・見送りの3つです。\n\n"\
                    "サブのサインは、無料公開させて頂きます。\n\n詳細は、会員募集からご覧ください。\n\n私と幸せを分かち合いましょう！\n\n"
        elif self.zone == "オーバーナイト2":
            return  "" + self.zone + "サブサイン！\n\nナイトセッション引けで" + self.buy + "です。\n\n"\
                    "メインのサインは、当会員様へメールで配信させて頂きました！\nよろしくお願いします！\n\n"\
                    "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "の" + self.zone + "結果！\n\n"\
                    "サブサイン   　 " + self.sub_sign + "　　 " + str(CONFIG.result_month()) + "月収支累計  " + self.sub_total + "\n\n"\
                    "メインサイン    " + self.main_sign + "　  　" + str(CONFIG.result_month()) + "月収支累計　" + self.main_total + "\n\nポチっとよろしくお願いします！\n\n"\
                    '<a href="http://futures.blogmura.com/225mini/"><img src="http://futures.blogmura.com/225mini/img/225mini150_49.gif" width="88" height="31" border="0" alt="にほんブログ村 先物取引ブログ 日経２２５ミニ先物へ" /></a> <a href="http://blog.with2.net/link.php?927061"><img src="http://image.with2.net/img/banner/banner_22.gif" width="88" height="31" border="0" alt="人気ブログランキングへ"></a><a href="http://futures.blogmura.com/225mini/"><a href="http://futures.blogmura.com/225mini/"></a> <a href="http://blogranking.fc2.com/in.php?id=463399" target="_blank"><img src="http://blogranking.fc2.com/ranking_banner/d_02.gif" style="border:0px;"></a>\n\n'\
                    "お知らせ！！\n\n会員様、読者様には大変お世話になっております。\n\n"\
                    "この度、会員様、読者様のご要望に答えまして、2011/9/22より、" + self.zone + "の取引に加えて、前場と後場の取引も追加させて頂きます。\n\n"\
                    "会員募集！！\n\n長年の研究の成果から作り上げた独自のシステムをもとに、当会員になられた方に、寄引けシステムのメインサインをメールで配信させて頂きます。サインは買い・売り・見送りの3つです。\n\n"\
                    "サブのサインは、無料公開させて頂きます。\n\n詳細は、会員募集からご覧ください。\n\n私と幸せを分かち合いましょう！\n\n"
        else: 
            return  ""+ self.zone + "本日のサブサイン! \n\n" + self.zone + "寄り付きで" + self.buy + "です。\n\n" + self.zone + "引けで決済します。\n\n"\
                    "メインのサインは、当会員様へメールで配信させて頂きました！\nよろしくお願いします！\n\n"\
                    "" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "の" + self.zone + "結果！\n\n"\
                    "サブサイン   　 " + self.sub_sign + "　　 " + str(CONFIG.result_month()) + "月収支累計  " + self.sub_total + "\n\n"\
                    "メインサイン    " + self.main_sign + "　  　" + str(CONFIG.result_month()) + "月収支累計　" + self.main_total + "\n\nポチっとよろしくお願いします！\n\n"\
                    '<a href="http://futures.blogmura.com/225mini/"><img src="http://futures.blogmura.com/225mini/img/225mini150_49.gif" width="88" height="31" border="0" alt="にほんブログ村 先物取引ブログ 日経２２５ミニ先物へ" /></a> <a href="http://blog.with2.net/link.php?927061"><img src="http://image.with2.net/img/banner/banner_22.gif" width="88" height="31" border="0" alt="人気ブログランキングへ"></a><a href="http://futures.blogmura.com/225mini/"><a href="http://futures.blogmura.com/225mini/"></a> <a href="http://blogranking.fc2.com/in.php?id=463399" target="_blank"><img src="http://blogranking.fc2.com/ranking_banner/d_02.gif" style="border:0px;"></a>\n\n'\
                    "お知らせ！！\n\n会員様、読者様には大変お世話になっております。\n\n"\
                    "この度、会員様、読者様のご要望に答えまして、2011/9/22より、" + self.zone + "の取引に加えて、前場と後場の取引も追加させて頂きます。\n\n"\
                    "会員募集！！\n\n長年の研究の成果から作り上げた独自のシステムをもとに、当会員になられた方に、寄引けシステムのメインサインをメールで配信させて頂きます。サインは買い・売り・見送りの3つです。\n\n"\
                    "サブのサインは、無料公開させて頂きます。\n\n詳細は、会員募集からご覧ください。\n\n私と幸せを分かち合いましょう！\n\n"
