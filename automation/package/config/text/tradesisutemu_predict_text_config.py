from .. import all_config as CONFIG


class TradesisutemuPredictText():
    def __init__(self,zone,time):
        self.zone = zone
        self.time = time
        if self.zone == "日中の予測情報":
            self.nomal_zone ="日中"
        if self.zone == "ナイトセッションの予測情報":
            self.nomal_zone = "ナイトセッション"
        if self.zone == "オーバーナイトの予測情報":
            self.nomal_zone = "オーバーナイト"

        print(zone+"の投稿\n")

    def blog_title(self):
        return self.zone

    def blog_text(self):
        return ''+self.zone+'\n\n\n'\
            ''+self.time+'に'+self.zone+'を有料読者様へ配信しました。\n\n\n'\
            '＊'+self.nomal_zone+'の売買ルール\n\n'\
            ''+self.nomal_zone+'寄付きで売買　⇒　⇒　'+self.nomal_zone+'引けで決済\n'
