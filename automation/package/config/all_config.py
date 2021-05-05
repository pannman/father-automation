#結果日(昨日)
def result_year():
    return 2021
def result_month():
    return 5
def result_day():
    return 27

#投稿日
def reserve_year():
    return 2021
def reserve_month():
    return 5
def reserve_day():
    return 28


#日経ミニ
def nikkei_mini_result(zone):
    if zone == "日中":
        return "95"
    if zone == "前場":
        return "100"
    if zone == "後場":
        return "10"
    if zone == "ナイトセッション":
        return "40"
    if zone == "オーバーナイト1":
        return "40"
    if zone == "オーバーナイト2":
        return "40"
    if zone == "c":
        return "20"
    if zone == "d":
        return "20"

#サブサイン売買
def sakimononikkei_sub_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "前場":
        return "買い"
    if zone == "後場":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト1":
        return "買い"
    if zone == "オーバーナイト2":
        return "買い"
    
#先物日経サブサイン
def sakimononikkei_sub(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "前場":
        return "勝ち"
    if zone == "後場":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト1":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "勝ち"
# メインサイン売買
def sakimononikkei_main_buy_result(zone):
    if zone == "日中":
        return "売り"
    if zone == "前場":
        return "売り"
    if zone == "後場":
        return "売り"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト1":
        return "買い"
    if zone == "オーバーナイト2":
        return "買い"
#先物日経メインサイン
def sakimononikkei_main(zone):
    if zone == "日中":
        return "負け"
    if zone == "前場":
        return "負け"
    if zone == "後場":
        return "負け"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト1":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "勝ち"


#夢を現実に
# 売買
def yumewogenzituni_main_buy_result(zone):
    if zone == "日中":
        return "買"
    if zone == "前場":
        return "買"
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
        return "勝ち"
    if zone == "後場":
        return "勝ち"
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
        return "買い"
    if zone == "オーバーナイト2":
        return "買い"
# サブシグナル
def sakusesunikki_sub(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
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
# 売買
def investing_main_buy_result(zone):
    if zone == "前場":
        return "買い"
    if zone == "後場":
        return "買い"
    if zone == "c":
        return "買い"
    if zone == "d":
        return "売り"
#メインサイン
def investing_main(zone):
    if zone == "前場":
        return "勝ち"
    if zone == "後場":
        return "勝ち"
    if zone == "c":
        return "勝ち"
    if zone == "d":
        return "負け"


#日経
def nikkei_result(zone):
    if zone == "日中":
        return "95"
    if zone == "前場":
        return "100"
    if zone == "後場":
        return "10"
    if zone == "ナイトセッション":
        return "40"
    if zone == "オーバーナイト1":
        return "40"
    if zone == "オーバーナイト2":
        return "40"
    if zone == "c":
        return "20"
    if zone == "d":
        return "20"

#勝ち組
#サブサイン売買
def katigumi_sub_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト2":
        return "買い"
# サブシグナル
def katigumi_sub(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "負け"
# メインサイン売買
def katigumi_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "売り"
    if zone == "オーバーナイト2":
        return "買い"
#　メインサイン
def katigumi_main(zone):
    if zone == "日中":
        return "負け"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "勝ち"

#幸運の女神
#サクセス日記
#サブシグナル売買
def megami_sub_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト2":
        return "買い"
# サブシグナル
def megami_sub(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "負け"
# メインシグナル売買
def megami_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "売り"
    if zone == "オーバーナイト2":
        return "買い"
#　メインシグナル
def megami_main(zone):
    if zone == "日中":
        return "負け"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "勝ち"

# 優雅な生活
# メインシグナル売買
def yuga_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "売り"
    if zone == "オーバーナイト2":
        return "買い"
#　メインシグナル
def yuga_main(zone):
    if zone == "日中":
        return "負け"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "勝ち"
#自己結果の金額
def yuga_self_money(zone):
    if zone == "日中":
        return "40"
    if zone == "ナイトセッション":
        return "80"
    if zone == "オーバーナイト2":
        return "30"

# 素晴らしき人生
def subarashiki_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "前場":
        return "買い"
    if zone == "後場":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト2":
        return "売り"
#メインサイン
def subarashiki_main(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "前場":
        return "勝ち"
    if zone == "後場":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "負け"
#売買結果金額
def subarashiki_result_trade_money(zone):
    if zone == "日中":
        return "29000"
    if zone == "前場":
        return "29000"
    if zone == "後場":
        return "29000"
    if zone == "ナイトセッション":
        return "29000"
    if zone == "オーバーナイト2":
        return "29000"
    
# 投資日記
def toshi_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "前場":
        return "買い"
    if zone == "後場":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト2":
        return "売り"
#メインサイン
def toshi_main(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "前場":
        return "勝ち"
    if zone == "後場":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "負け"

# 億万長者
# メインシグナル売買
def okuman_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "売り"
    if zone == "オーバーナイト2":
        return "買い"
#　メインシグナル
def okuman_main(zone):
    if zone == "日中":
        return "負け"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "勝ち"

# 薔薇の人生
# 売買
def bara_main_buy_result(zone):
    if zone == "前場":
        return "買い"
    if zone == "後場":
        return "売り"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト2":
        return "売り"
#メインサイン
def bara_main(zone):
    if zone == "前場":
        return "勝ち"
    if zone == "後場":
        return "負け"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "負け"

# 未来への挑戦
#売買結果
def miraie_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
#メインサイン
def miraie_main(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
#売買結果金額
def miraie_result_trade_money(zone):
    if zone == "日中":
        return "29000"
    if zone == "ナイトセッション":
        return "29000"

#はばたけ未来へ
def habatake_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "前場":
        return "買い"
    if zone == "後場":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト1":
        return "買い"
    if zone == "オーバーナイト2":
        return "売り"
#メインサイン
def habatake_main(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "前場":
        return "勝ち"
    if zone == "後場":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト1":
        return "買い"
    if zone == "オーバーナイト2":
        return "負け"


# メイン

#habatake


# fx

# 仮想通貨
# 先物




