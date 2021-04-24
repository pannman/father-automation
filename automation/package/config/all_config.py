#結果日(昨日)
def result_year():
    return 2021
def result_month():
    return 4
def result_day():
    return 16

#投稿日
def reserve_year():
    return 2021
def reserve_month():
    return 4
def reserve_day():
    return 27


#日経ミニ
def nikkei_mini_result(zone):
    if zone == "日中":
        return "10"
    if zone == "前場":
        return "10"
    if zone == "後場":
        return "10"
    if zone == "ナイトセッション":
        return "40"
    if zone == "オーバーナイト2":
        return "40"
    if zone == "c"
        return "20"
    if zone == "d"
        return "20"

#サブサイン売買
def sakimononikkei_sub_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "前場":
        return "売り"
    if zone == "後場":
        return "買い"
#先物日経サブサイン
def sakimononikkei_sub(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "前場":
        return "負け"
    if zone == "後場":
        return "負け"
# メインサイン売買
def sakimononikkei_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "前場":
        return "売り"
    if zone == "後場":
        return "買い"
#先物日経メインサイン
def sakimononikkei_main(zone):
    if zone == "日中":
        return "負け"
    if zone == "前場":
        return "勝ち"
    if zone == "後場":
        return "勝ち"


#夢を現実に
# 売買
def yumewogenzituni_main_buy_result(zone):
    if zone == "日中":
        return "買"
    if zone == "前場":
        return "売"
    if zone == "後場":
        return "買"
    if zone == "ナイトセッション":
        return "買"
    if zone == "オーバーナイト2":
        return "売"
#メインサイン
def yumewogenzituni_main(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "前場":
        return "引き分け"
    if zone == "後場":
        return "負け"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "負け"


#サクセス日記
#サブシグナル売買
def sakusesunikki_sub_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "売り"
    if zone == "オーバーナイト2":
        return "買い"
# サブシグナル
def sakusesunikki_sub(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "ナイトセッション":
        return "負け"
    if zone == "オーバーナイト2":
        return "負け"
# メインシグナル売買
def sakusesunikki_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "売り"
    if zone == "オーバーナイト2":
        return "買い"
#　メインシグナル
def sakusesunikki_main(zone):
    if zone == "日中":
        return "負け"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "勝ち"


#ミニ投資法

#ミニ投資法
# investing
# a　前場
# b　後場
# c
# d

# メイン
# 勝ち組
# 幸運の女神
# 優雅な生活
# 素晴らしき人生
# 投資日記
# 億万長者
# 薔薇の人生
# 未来への挑戦


# fx

# 仮想通貨
# 先物




#日経先物ミニ
#先物日経
#サブサイン結果
def sub_sign(zone):
    if zone == "日中":
        return "-20"
    if zone == "前場":
        return "-60"
    if zone == "後場":
        return "±0"

    if zone == "ナイトセッション":
        return "+11"


    if zone == "オーバーナイト1":
        return "+11"
    if zone == "オーバーナイト2":
        return "+11"
#サブサイン累計
def a_sub_total(zone):
    if zone == "日中":
        return "-815"
    if zone == "前場":
        return "-630"
    if zone == "後場":
        return "-140"
    if zone == "ナイトセッション":
        return "+11"

    if zone == "オーバーナイト1":
        return "+11"
    if zone == "オーバーナイト2":
        return "+11"
#サブサイン買いか売りか
def sub_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "前場":
        return "売り"
    if zone == "後場":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    
    if zone == "オーバーナイト1":
        return "買い"
    if zone == "オーバーナイト2":
        return "売り"
#メインサイン結果
def main_sign(zone):
    if zone == "日中":
        return "-20"
    if zone == "前場":
        return "-60"
    if zone == "後場":
        return "±0"
    if zone == "ナイトセッション":
        return "+11"

    if zone == "オーバーナイト1":
        return "+11"
    if zone == "オーバーナイト2":
        return "+11"
#メイン累計
def a_main_total(zone):
    if zone == "日中":
        return "+285"
    if zone == "前場":
        return "+130"
    if zone == "後場":
        return "-140"
    if zone == "ナイトセッション":
        return "+11"

    if zone == "オーバーナイト1":
        return "+11"
    if zone == "オーバーナイト2":
        return "+11"
#メインサイン買いか売りか
def main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "前場":
        return "売り"
    if zone == "後場":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"

    if zone == "オーバーナイト1":
        return "+11"
    if zone == "オーバーナイト2":
        return "売り"

#夢
#メインサイン
def main_sign(zone):
    if zone == "日中":
        return "-20"
    if zone == "前場":
        return "-60"
    if zone == "後場":
        return "±0"
    if zone == "ナイトセッション":
        return "+11"

    if zone == "オーバーナイト2":
        return "+11"
#メイン累計
def main_total(zone):
    if zone == "日中":
        return "+285"
    if zone == "前場":
        return "+130"
    if zone == "後場":
        return "-140"
    if zone == "ナイトセッション":
        return "+11"

    if zone == "オーバーナイト2":
        return "+11"
#メインサイン買いか売りか
def main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "前場":
        return "売り"
    if zone == "後場":
        return "買い"

    if zone == "オーバーナイト2":
        return "売り"

#サクセス
#メインサイン結果
def main_sign(zone):
    if zone == "日中":
        return "-20"
    if zone == "前場":
        return "-60"
    if zone == "後場":
        return "±0"
    if zone == "ナイトセッション":
        return "+11"

    if zone == "オーバーナイト2":
        return "+11"
#メインサイン累計
def main_total(zone):
    if zone == "日中":
        return "-815"
    if zone == "前場":
        return "-630"
    if zone == "後場":
        return "-140"
    if zone == "ナイトセッション":
        return "+11"

    if zone == "オーバーナイト2":
        return "+11"
#メインサイン買いか売りか
def main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "前場":
        return "売り"
    if zone == "後場":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    
    if zone == "オーバーナイト2":
        return "売り"

#ビクトリアス
#メインサイン
def main_sign(zone):
    if zone == "日中":
        return "-20"
    if zone == "ナイトセッション":
        return "+11"

    if zone == "オーバーナイト2":
        return "+11"

#メイン累計
def main_total(zone):
    if zone == "日中":
        return "+285"
    if zone == "ナイトセッション":
        return "+11"

    if zone == "オーバーナイト2":
        return "+11"

#メインサイン買いか売りか
def main_buy_result(zone):
    if zone == "日中":
        return "買い"

    if zone == "オーバーナイト2":
        return "売り"

#荒稼ぎ(今日)
#メインサイン結果
def main_sign(zone):
    if zone == "日中":
        return "-20"
    if zone == "オーバーナイト1":
        return "+11"
    if zone == "オーバーナイトX":
        return "+11"
#メイン累計
def main_total(zone):
    if zone == "日中":
        return "+285"
    if zone == "オーバーナイト1":
        return "+11"
    if zone == "オーバーナイトX":
        return "+11"
#メインサイン買いか売りか
def main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "オーバーナイト1":
        return "+11"
    if zone == "オーバーナイトX":
        return "売り"

#investing
#メインサイン結果
def main_sign(zone):
    if zone == "前場":
        return "-60"
    if zone == "後場":
        return "±0"
    if zone == "C":
        return "+11"
    if zone == "D":
        return "+11"
#メイン累計
def main_total(zone):
    if zone == "前場":
        return "+130"
    if zone == "後場":
        return "-140"
    if zone == "C":
        return "+11"
    if zone == "D":
        return "+11"
#メインサイン買いか売りか
def main_buy_result(zone):
    if zone == "前場":
        return "売り"
    if zone == "後場":
        return "買い"
    if zone == "C":
        return "買い"
    if zone == "D":
        return "+11"

#日経先物
#勝ち組
#サブサイン結果
def sub_sign(zone):
    if zone == "日中":
        return "-20"
    if zone == "ナイトセッション":
        return "+11"


    if zone == "オーバーナイト2":
        return "+11"
#サブサイン累計
def sub_total(zone):
    if zone == "日中":
        return "-815"
    if zone == "ナイトセッション":
        return "+11"

    if zone == "オーバーナイト2":
        return "+11"
#サブサイン買いか売りか
def sub_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    
    if zone == "オーバーナイト2":
        return "売り"
#メインサイン結果
def main_sign(zone):
    if zone == "日中":
        return "-20"
    if zone == "ナイトセッション":
        return "+11"

    if zone == "オーバーナイト2":
        return "+11"
#メイン累計
def main_total(zone):
    if zone == "日中":
        return "+285"
    if zone == "ナイトセッション":
        return "+11"

    if zone == "オーバーナイト2":
        return "+11"
#メインサイン買いか売りか
def main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"

    if zone == "オーバーナイト2":
        return "売り"
