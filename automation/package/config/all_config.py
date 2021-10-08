#結果日(昨日)
def result_year():
    return 2021
def result_month():
    return 10
def result_day():
    return 7

#投稿日
def reserve_year():
    return 2021
def reserve_month():
    return 10
def reserve_day():
    return 8


#日経ミニ
def nikkei_mini_result(zone):
    if zone == "日中":
        return "170"
    if zone == "前場":
        return "345"
    if zone == "後場":
        return "45"
    if zone == "ナイトセッション":
        return "295"
    if zone == "オーバーナイト1":
        return "255"
    if zone == "オーバーナイト2":
        return "40"
    if zone == "c":
        return "150"
    if zone == "d":
        return "115"

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
        return "負け"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト1":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "負け"
# メインサイン売買
def sakimononikkei_main_buy_result(zone):
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
#先物日経メインサイン
def sakimononikkei_main(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "前場":
        return "勝ち"
    if zone == "後場":
        return "負け"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト1":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "負け"


#夢を現実に
# 売買
def yumewogenzituni_main_buy_result(zone):
    if zone == "日中":
        return "買"
    if zone == "前場":
        return "買"
    if zone == "後場":
        return "売"
    if zone == "ナイトセッション":
        return "売"
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
        return "負け"
    if zone == "オーバーナイト2":
        return "勝ち"


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
        return "買い"
    if zone == "オーバーナイト2":
        return "買い"
#　メインシグナル
def sakusesunikki_main(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "負け"

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
        return "買い"
#メインサイン
def investing_main(zone):
    if zone == "前場":
        return "勝ち"
    if zone == "後場":
        return "負け"
    if zone == "c":
        return "勝ち"
    if zone == "d":
        return "勝ち"


#日経
def nikkei_result(zone):
    if zone == "日中":
        return "170"
    if zone == "前場":
        return "340"
    if zone == "後場":
        return "50"
    if zone == "ナイトセッション":
        return "290"
    if zone == "オーバーナイト1":
        return "260"
    if zone == "オーバーナイト2":
        return "30"

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
        return "買い"
    if zone == "オーバーナイト2":
        return "売り"
#　メインサイン
def katigumi_main(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "勝ち"

#幸運の女神
#サブシグナル売買
def megami_sub_buy_result(zone):
    if zone == "日中":
        return "売り"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト2":
        return "売り"
# サブシグナル
def megami_sub(zone):
    if zone == "日中":
        return "負け"         
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "勝ち"
# メインシグナル売買
def megami_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト2":
        return "買い"
#　メインシグナル
def megami_main(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "負け"

# 優雅な生活
# メインシグナル売買
def yuga_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト2":
        return "売り"
#　メインシグナル
def yuga_main(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "勝ち"
#自己結果の金額
def yuga_self_money(zone):
    if zone == "日中":
        return "51"
    if zone == "ナイトセッション":
        return "87"
    if zone == "オーバーナイト2":
        return "9"

# 素晴らしき人生
def subarashiki_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "前場":
        return "買い"
    if zone == "後場":
        return "買い"
    if zone == "ナイトセッション":
        return "売り"
    if zone == "オーバーナイト1":
        return "買い"
#メインサイン
def subarashiki_main(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "前場":
        return "勝ち"
    if zone == "後場":
        return "負け"
    if zone == "ナイトセッション":
        return "負け"
    if zone == "オーバーナイト1":
        return "勝ち"
#売買結果金額
def subarashiki_result_trade_money(zone):
    if zone == "日中" or zone == "前場":
        return "27650"
    if zone == "後場":
        return "27870"
    if zone == "ナイトセッション" or zone == "オーバーナイト1":
        return "27770"

    
# 投資日記
def toshi_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "前場":
        return "買い"
    if zone == "後場":
        return "売り"
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
        return "勝ち"

# 億万長者
# メインシグナル売買
def okuman_main_buy_result(zone):
    if zone == "日中":
        return "売り"
    if zone == "ナイトセッション":
        return "売り"
    if zone == "オーバーナイト2":
        return "売り"
#　メインシグナル
def okuman_main(zone):
    if zone == "日中":
        return "負け"
    if zone == "ナイトセッション":
        return "負け"
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
        return "売り"
    if zone == "オーバーナイト2":
        return "売り"
#メインサイン
def bara_main(zone):
    if zone == "前場":
        return "勝ち"
    if zone == "後場":
        return "勝ち"
    if zone == "ナイトセッション":
        return "負け"
    if zone == "オーバーナイト2":
        return "勝ち"

# 未来への挑戦
#売買結果
def miraie_main_buy_result(zone):
    if zone == "日中":
        return "売り"
    if zone == "ナイトセッション":
        return "買い"
#メインサイン
def miraie_main(zone):
    if zone == "日中":
        return "負け"
    if zone == "ナイトセッション":
        return "勝ち"
#売買結果金額
def miraie_result_trade_money(zone):
    if zone == "日中":
        return "27650"
    if zone == "ナイトセッション":
        return "27770"

#はばたけ未来へ
def habatake_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "前場":
        return "買い"
    if zone == "後場":
        return "売り"
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
        return "勝ち"
    if zone == "オーバーナイト2":
        return "勝ち"

#fxドル(売り)
def fx_zone_dollar(zone):
    if zone == "08:00":
        return 111.437
    if zone == "08:30":
        return 111.399
    if zone == "09:00":
        return 111.409
    if zone == "15:00":
        return 111.482
    if zone == "15:30":
        return 111.460
    if zone == "16:00":
        return 111.359
    if zone == "16:30":
        return 111.265
    if zone == "20:00":
        return 111.401
    if zone == "21:00":
        return 111.353
    #翌日
    if zone == "y07:00":
        return 111.622
    if zone == "y07:30":
        return 111.633
    if zone == "y08:30":
        return 111.653
    if zone == "y09:00":
        return 111.663    

#fxユーロ(売り)
# def fx_zone_euro(zone):
#     if zone == "08:00":
#         return 108.905
#     if zone == "08:30":
#         return 108.905
#     if zone == "09:00":
#         return 108.905
#     if zone == "15:00":
#         return 108.905
#     if zone == "15:30":
#         return 108.905
#     if zone == "16:00":
#         return 108.905
#     if zone == "16:30":
#         return 108.905
#     if zone == "20:00":
#         return 108.905
#     if zone == "21:00":
#         return 108.905
#      #翌日
#     if zone == "y07:00":
#         return 108.905
#     if zone == "y07:30":
#         return 108.905
#     if zone == "y08:30":
#         return 108.905
#     if zone == "y09:00":
#         return 108.905   

# #fxポンド(売り)
# def fx_zone_lb(zone):
#     if zone == "08:00":
#         return 108.905
#     if zone == "08:30":
#         return 108.905
#     if zone == "09:00":
#         return 108.905
#     if zone == "15:00":
#         return 109.338
#     if zone == "15:30":
#         return 108.905
#     if zone == "16:00":
#         return 108.905
#     if zone == "16:30":
#         return 108.905
#     if zone == "20:00":
#         return 108.905
#     if zone == "21:00":
#         return 108.905
#      #翌日
#     if zone == "y07:00":
#         return 108.905
#     if zone == "y07:30":
#         return 108.905
#     if zone == "y08:30":
#         return 108.905
#     if zone == "y09:00":
#         return 108.905   

#脅威のFXトレード
def kyoifx_main_buy_result(zone):
    if zone == "パターン1":
        return "買い"
    if zone == "パターン2":
        return "買い"
    if zone == "パターン3":
        return "買い"

#サラリーマンの副業に最適なＦＸ投資
def sararimanfx_main_buy_result(zone):
    if zone == "シグナルA":
        return "買い"
    if zone == "シグナルB":
        return "買い"
    if zone == "シグナルC":
        return "買い"

#世界の市場時間にあわせたFX投資術
def toshijutufx_main_buy_result(zone):
    if zone == "（8：30　⇒　15：30）":
        return "買い"
    if zone == "（16：30　⇒　20：00）":
        return "買い"
    if zone == "（21：00　⇒　7：30）":
        return "買い"

#FX投資日記
def fxtoshinikki_main_buy_result(zone):
    if zone == "FX投資日記1":
        return "買い"
    if zone == "FX投資日記2":
        return "買い"
        
#億万FX
def okumanfx_main_buy_result(zone):
    if zone == "09：00　→　16：30":
        return "買い"
    if zone == "16：30　→　09：00":
        return "買い"

#未来への挑戦FX
def miraienotyousennfx_main_buy_result(zone):
    if zone == "09：00→21：00":
        return "買い"
    if zone == "21：00→09：00":
        return "買い"

# fx

# 仮想通貨
# 先物




