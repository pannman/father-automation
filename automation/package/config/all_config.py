#結果日(昨日)
def result_year():
    return 2022
def result_month():
    return 12
def result_day():
    return 12

#結果日(翌日)
def y_result_year():
    return 2022
def y_result_month():
    return 12
def y_result_day():
    return 13


#投稿日
def reserve_year():
    return 2022
def reserve_month():
    return 12
def reserve_day():
    return 13



#日経ミニ
def nikkei_mini_result(zone):
    if zone == "日中":
        return "135"
    if zone == "前場":
        return "125"
    if zone == "後場":
        return "10"
    if zone == "ナイトセッション":
        return "265"
    if zone == "オーバーナイト1":
        return "605"
    if zone == "オーバーナイト2":
        return "340"
    if zone == "c":
        return "75"
    if zone == "d":
        return "300"

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
        return "勝ち"
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
        return "買い"
#メインサイン
def investing_main(zone):
    if zone == "前場":
        return "勝ち"
    if zone == "後場":
        return "勝ち"
    if zone == "c":
        return "負け"
    if zone == "d":
        return "勝ち"


#日経
def nikkei_result(zone):
    if zone == "日中":
        return "140"
    if zone == "前場":
        return "130"
    if zone == "後場":
        return "10"
    if zone == "ナイトセッション":
        return "250"
    if zone == "オーバーナイト1":
        return "600"
    if zone == "オーバーナイト2":
        return "350"

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
        return "勝ち"
# メインサイン売買
def katigumi_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト2":
        return "買い"
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
        return "買い"
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
        return "負け"
# メインシグナル売買
def megami_main_buy_result(zone):
    if zone == "日中":
        return "売り"
    if zone == "ナイトセッション":
        return "買い"
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
        return "買い"
    if zone == "オーバーナイト2":
        return "買い"
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
        return "42"
    if zone == "ナイトセッション":
        return "75"
    if zone == "オーバーナイト2":
        return "105"

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
    if zone == "オーバーナイト1":
        return "買い"
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
    if zone == "オーバーナイト1":
        return "勝ち"
#売買結果金額
def subarashiki_result_trade_money(zone):
    if zone == "日中" or zone == "前場":
        return "29410"
    if zone == "後場":
        return "29540"
    if zone == "ナイトセッション" or zone == "オーバーナイト1":
        return "28810"

    
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
        return "買い"
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
        return "買い"
    if zone == "ナイトセッション":
        return "売り"
    if zone == "オーバーナイト2":
        return "買い"
#　メインシグナル
def okuman_main(zone):
    if zone == "日中":
        return "勝ち"
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
        return "買い"
    if zone == "ナイトセッション":
        return "売り"
    if zone == "オーバーナイト2":
        return "買い"
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
        return "29410"
    if zone == "ナイトセッション":
        return "28810"

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
        return "買い"
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
        return 114.150
    if zone == "08:30":
        return 114.167
    if zone == "09:00":
        return 114.237
    if zone == "15:00":
        return 114.236
    if zone == "15:30":
        return 114.304
    if zone == "16:00":
        return 114.350
    if zone == "16:30":
        return 114.348
    if zone == "20:00":
        return 114.245
    if zone == "21:00":
        return 114.237
    if zone == "22:00":
        return 114.237
    #翌日
    if zone == "y07:00":
        return 114.097
    if zone == "y07:30":
        return 114.163
    if zone == "y08:30":
        return 114.167
    if zone == "y09:00":
        return 114.237   
    if zone == "y15:30":
        return 114.237

# fxユーロ/円(売り)
def fx_zone_euro(zone):
    if zone == "08:00":
        return 108.905
    # if zone == "08:30":
    #     return 108.905
    if zone == "09:00":
        return 132.019
    # if zone == "15:00":
    #     return 108.905
    # if zone == "15:30":
    #     return 108.905
    # if zone == "16:00":
    #     return 108.905
    if zone == "16:30":
        return 132.151
    if zone == "20:00":
        return 108.905
    if zone == "20:30":
        return 108.905
    # if zone == "21:00":
    #     return 108.905
    if zone == "22:00":
        return 114.237
     #翌日
    # if zone == "y07:00":
    #     return 108.905
    if zone == "y07:30":
        return 108.905
    if zone == "y08:30":
        return 108.905
    if zone == "y09:00":
        return 132.019  
    if zone == "y15:30":
        return 114.237

#fxポンド/円(売り)
def fx_zone_lb(zone):
    if zone == "08:00":
        return 108.905
    # if zone == "08:30":
    #     return 108.905
    if zone == "09:00":
        return 156.305
    # if zone == "15:00":
    #     return 109.338
    # if zone == "15:30":
    #     return 108.905
    # if zone == "16:00":
    #     return 108.905
    if zone == "16:30":
        return 156.165
    if zone == "20:00":
        return 108.905
    if zone == "20:30":
        return 108.905
    # if zone == "21:00":
    #     return 108.905
    #  #翌日
    # if zone == "y07:00":
    #     return 108.905
    if zone == "y07:30":
        return 108.905
    if zone == "y08:30":
        return 108.905
    if zone == "y09:00":
        return 156.305   

# fxユーロ/ドル(売り)
def fx_zone_euro_dol(zone):
    if zone == "08:00":
        return 108.905
    # if zone == "08:30":
    #     return 108.905
    if zone == "09:00":
        return 132.019
    # if zone == "15:00":
    #     return 108.905
    # if zone == "15:30":
    #     return 108.905
    # if zone == "16:00":
    #     return 108.905
    if zone == "16:30":
        return 132.151
    if zone == "20:00":
        return 108.905
    if zone == "20:30":
        return 108.905
    # if zone == "21:00":
    #     return 108.905
     #翌日
    # if zone == "y07:00":
    #     return 108.905
    if zone == "y07:30":
        return 108.905
    if zone == "y08:30":
        return 108.905
    if zone == "y09:00":
        return 132.019

#fxポンド/ドル(売り)
def fx_zone_lb_dol(zone):
    if zone == "08:00":
        return 108.905
    # if zone == "08:30":
    #     return 108.905
    if zone == "09:00":
        return 156.305
    # if zone == "15:00":
    #     return 109.338
    # if zone == "15:30":
    #     return 108.905
    # if zone == "16:00":
    #     return 108.905
    if zone == "16:30":
        return 156.165
    if zone == "20:00":
        return 108.905
    if zone == "20:30":
        return 108.905
    # if zone == "21:00":
    #     return 108.905
    #  #翌日
    # if zone == "y07:00":
    #     return 108.905
    if zone == "y07:30":
        return 108.905
    if zone == "y08:30":
        return 108.905
    if zone == "y09:00":
        return 156.305

#脅威のFXトレード
def kyoifx_main_buy_result(zone):
    if zone == "パターン1":
        return "買い"
    if zone == "パターン2":
        return "売り"
    if zone == "パターン3":
        return "売り"

#サラリーマンの副業に最適なＦＸ投資
def sararimanfx_main_buy_result(zone):
    if zone == "シグナルA":
        return "買い"
    if zone == "シグナルB":
        return "売り"
    if zone == "シグナルC":
        return "売り"

#世界の市場時間にあわせたFX投資術
def toshijutufx_main_buy_result(zone):
    if zone == "（8：30　⇒　15：30）":
        return "買い"
    if zone == "（16：30　⇒　20：00）":
        return "売り"
    if zone == "（21：00　⇒　7：30）":
        return "売り"

#FX投資日記
def fxtoshinikki_main_buy_result(zone):
    if zone == "FX投資日記1":
        return "買い"
    if zone == "FX投資日記2":
        return "売り"
        
#億万FX
def okumanfx_main_buy_result(zone):
    if zone == "09：00　→　16：30":
        return "買い"
    if zone == "16：30　→　09：00":
        return "売り"

#未来への挑戦FX
def miraienotyousennfx_main_buy_result(zone):
    if zone == "09：00→21：00":
        return "買い"
    if zone == "21：00→09：00":
        return "売り"

#成功のfx
def seikoufx_main_buy_result(zone):
    if zone == "09:00成行き売買→16：30成行き決済":
        # ドル、ユーロ、ポンドの順番
        return "買い","買い","買い"
    if zone == "16:30成行き売買→09：00成行き決済":
        # ドル、ユーロ、ポンドの順番
        return "買い","売り","売り"
    
#はばたけfx
def habatakefx_main_buy_result(zone):
    if zone == "09：00→21：00":
        # ドル、ユーロ、ポンドの順番
        return "買い", "売り", "売り"
    if zone == "21：00→09：00":
        # ドル、ユーロ、ポンドの順番
        return "買い", "買い", "買い"

#ゆうがfx
def yugafx_main_buy_result(zone):
    if zone == "08：00（成行売買）～20：00（成行決済）":
        # ドル/円、ユーロ/円、ポンド/円,ユーロ/ドル,ポンド/ドルの順番
        return "買い", "売り", "売り", "売り", "売り"
    if zone == "20：30（成行売買）～07：30（成行決済）":
        # ドル/円、ユーロ/円、ポンド/円,ユーロ/ドル,ポンド/ドルの順番
        return "買い", "買い", "買い", "売り", "売り"
    
#fx投資ブログ
def fxtoshiburogu_main_buy_result(zone):
    if zone == "09：00　→　08：30":
        # ドル/円、ユーロ/円、ポンド/円,ユーロ/ドル,ポンド/ドルの順番
        return "買い", "売り", "売り", "売り", "売り"
    
#fxテクニカルドル
def fxtecunikarudoru_main_buy_result(zone):
    if zone == "今日もがんばります！！ｂｙドル":
        return "買い"
    if zone == "次の予想も頑張ります！！byドル":
        return "買い"
    if zone == "ラストスパート！！ｂｙドル":
        return "買い"
    
#fxテクニカルユーロ
def fxtecunikaruyuro_main_buy_result(zone):
    if zone == "今日もがんばります！！ｂｙユーロ":
        return "買い"
    if zone == "次の予想も頑張ります！！byユーロ":
        return "買い"
    if zone == "ラストスパート！！ｂｙユーロ":
        return "買い"

# 仮想通貨
# 先物




