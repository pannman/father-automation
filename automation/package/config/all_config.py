#結果日(昨日)
def result_year():
    return 2023
def result_month():
    return 4
def result_day():
    return 28

#結果日(翌日)
def y_result_year():
    return 2023
def y_result_month():
    return 5
def y_result_day():
    return 2


#投稿日
def reserve_year():
    return 2023
def reserve_month():
    return 5
def reserve_day():
    return 2



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

    #メインサイン（サブ）
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
    
    #メインサイン（サブ）
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
        
    #メインサイン（メイン）
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
        
    #メインサイン（メイン）
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
    
    #夢を現実に
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


    #サクセス日記(サブ)
def sakusesunikki_sub_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト2":
        return "買い"
   
    #サクセス日記(サブ)
def sakusesunikki_sub(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "勝ち"

    #サクセス日記（メイン）
def sakusesunikki_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト2":
        return "買い"
    
    #サクセス日記（メイン）
def sakusesunikki_main(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "勝ち"

    #ミニ投資法
def investing_main_buy_result(zone):
    if zone == "前場":
        return "買い"
    if zone == "後場":
        return "買い"
    if zone == "c":
        return "買い"
    if zone == "d":
        return "買い"
    
    #ミニ投資法
def investing_main(zone):
    if zone == "前場":
        return "勝ち"
    if zone == "後場":
        return "勝ち"
    if zone == "c":
        return "負け"
    if zone == "d":
        return "勝ち"

    #日経先物
def nikkei_result(zone):
    if zone == "日中":
        return "140"
    if zone == "前場":
        return "130"
    if zone == "後場":
        return "10"
    if zone == "ナイトセッション":
        return "250"
    if zone == "オーバーナイト":
        return "600"
    if zone == "オーバーナイト1":
        return "600"
    if zone == "オーバーナイト2":
        return "350"

    #勝ち組（サブ）
def katigumi_sub_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト2":
        return "買い"
   
    #勝ち組（サブ）
def katigumi_sub(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "勝ち"
    
    #勝ち組（メイン）
def katigumi_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト2":
        return "買い"

    #勝ち組（メイン）
def katigumi_main(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "勝ち"

    #幸運の女神（サブ）
def megami_sub_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト2":
        return "売り"

    #幸運の女神（サブ）
def megami_sub(zone):
    if zone == "日中":
        return "負け"         
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "負け"

    #幸運の女神（メイン）
def megami_main_buy_result(zone):
    if zone == "日中":
        return "売り"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト2":
        return "買い"
    
    #幸運の女神（メイン）
def megami_main(zone):
    if zone == "日中":
        return "負け"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト2":
        return "勝ち"

    #優雅な生活
def yuga_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト2":
        return "買い"
    
    #優雅な生活
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

    #素晴らしき人生
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
    
    #素晴らしき人生
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

    
   #投資日記
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
   
   #投資日記   
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

    #億万長者
def okuman_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "売り"
    if zone == "オーバーナイト2":
        return "買い"
   
    #億万長者
def okuman_main(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "ナイトセッション":
        return "負け"
    if zone == "オーバーナイト2":
        return "勝ち"

    #薔薇の人生
def bara_main_buy_result(zone):
    if zone == "前場":
        return "買い"
    if zone == "後場":
        return "買い"
    if zone == "ナイトセッション":
        return "売り"
    if zone == "オーバーナイト2":
        return "買い"
    
    #薔薇の人生
def bara_main(zone):
    if zone == "前場":
        return "勝ち"
    if zone == "後場":
        return "勝ち"
    if zone == "ナイトセッション":
        return "負け"
    if zone == "オーバーナイト2":
        return "勝ち"

    #未来への挑戦
def miraie_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"

    #未来への挑戦
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
    
    #はばたけ未来へ
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
    
#システムトレード
def tradesisutemu_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト":
        return "買い"

#システムトレード
def tradesisutemu_main(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト":
        return "勝ち"

#システムトレード売買結果金額
def tradesisutemu_result_trade_money(zone):
    if zone == "日中":
        return "29410"
    if zone == "ナイトセッション":
        return "28810"
    if zone == "オーバーナイト":
        return "28810"
    
#ヴィクトリアス
def victorious_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "夜間立会":
        return "買い"
    if zone == "夜間立会引け":
        return "買い"
#ヴィクトリアス
def victorious_main(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "夜間立会":
        return "負け"
    if zone == "夜間立会引け":
        return "勝ち"

    
#幸せな人生
def siawase_main_buy_result(zone):
    if zone == "日中":
        return "買い"
    if zone == "ナイトセッション":
        return "買い"
    if zone == "オーバーナイト":
        return "買い"
#システムトレード
def siawase_main(zone):
    if zone == "日中":
        return "勝ち"
    if zone == "ナイトセッション":
        return "勝ち"
    if zone == "オーバーナイト":
        return "勝ち"

#幸せな人生売買結果金額
def siawase_result_trade_money(zone):
    if zone == "日中":
        return "29410"
    if zone == "ナイトセッション":
        return "28810"
    if zone == "オーバーナイト":
        return "28810"


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
    if zone == "20:30":
        return 114.245
    if zone == "21:00":
        return 114.237
    if zone == "22:00":
        return 114.237
   
    #翌日fxドル(売り)
    if zone == "y05:30":
        return 114.097
    if zone == "y07:00":
        return 114.097
    if zone == "y07:30":
        return 114.163
    if zone == "y08:30":
        return 114.167
    if zone == "y09:00":
        return 130.001   
    if zone == "y15:30":
        return 130.248
    if zone == "y16:30":
        return 130.248

    #fxユーロ/円(売り)
def fx_zone_euro(zone):
    if zone == "08:00":
        return 108.905
    if zone == "09:00":
        return 132.019
    if zone == "16:30":
        return 132.151
    if zone == "20:00":
        return 108.905
    if zone == "20:30":
        return 108.905
    if zone == "21:00":
        return 108.905
    if zone == "22:00":
        return 114.237
    
    #翌日fxユーロ/円(売り)
    if zone == "y05:30":
        return 114.097
    if zone == "y07:30":
        return 108.905
    if zone == "y08:30":
        return 108.905
    if zone == "y09:00":
        return 136.983  
    if zone == "y15:30":
        return 137.394
    if zone == "y16:30":
        return 137.394

    #fxポンド/円(売り)
def fx_zone_lb(zone):
    if zone == "05:30":
        return 114.150
    if zone == "08:00":
        return 108.905
    if zone == "09:00":
        return 156.305
    if zone == "16:30":
        return 156.165
    if zone == "20:00":
        return 108.905
    if zone == "20:30":
        return 108.905
    if zone == "21:00":
        return 108.905
    if zone == "22:00":
        return 114.237
    
    #翌日fxポンド/円(売り)
    if zone == "y05:30":
        return 114.097
    if zone == "y07:30":
        return 108.905
    if zone == "y08:30":
        return 108.905
    if zone == "y09:00":
        return 163.412   
    if zone == "y15:30":
        return 114.237
    if zone == "y16:30":
        return 163.765

    #fxユーロ/ドル(売り)
def fx_zone_euro_dol(zone):
    if zone == "08:00":
        return 108.905
    if zone == "09:00":
        return 132.019
    if zone == "20:00":
        return 108.905
    if zone == "20:30":
        return 108.905

    #翌日fxユーロ/ドル(売り)
    if zone == "y07:30":
        return 108.905
    if zone == "y08:30":
        return 108.905

    #fxポンド/ドル(売り)
def fx_zone_lb_dol(zone):
    if zone == "08:00":
        return 108.905
    if zone == "09:00":
        return 156.305
    if zone == "20:00":
        return 108.905
    if zone == "20:30":
        return 108.905

    #翌日fxポンド/ドル(売り)     
    if zone == "y07:30":
        return 108.905
    if zone == "y08:30":
        return 108.905

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

    #優雅fx
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
    
    #fxテクニカルポンド
def fxtecunikaruponndo_main_buy_result(zone):
    if zone == "今日もがんばります！！ｂｙポンド":
        return "買い"
    if zone == "次の予想も頑張ります！！byポンド":
        return "買い"
    if zone == "ラストスパート！！ｂｙポンド":
        return "買い"

    #ビクトリアスfx
def victoriousfx_main_buy_result(zone):
    if zone == "5：30→9：00":
        # ドル、ユーロ、ポンドの順番
        return "買い", "買い", "買い"
    if zone == "9：00→16：30":
        # ドル、ユーロ、ポンドの順番
        return "売り", "売り", "売り"
    if zone == "16：30→5：30":
        # ドル、ユーロ、ポンドの順番
        return "買い", "売り", "売り"
    
    #fxシステムトレード
def fxsisutemutorade_main_buy_result(zone):
    if zone == "トレード結果（09：00→16：30）":
        # ドル、ユーロ、ポンドの順番
        return "売り", "売り", "売り"
    if zone == "トレード結果（16：30→09：00）":
        # ドル、ユーロ、ポンドの順番
        return "買い", "買い", "買い"
    
    #金
def gold_sakimono(zone):
    if zone == "08:45":
        return 7762
    if zone == "15:15":
        return 7820
    if zone == "16:30":
        return 7875
    if zone == "y06:00":
        return 7951
    if zone == "y15:15":
        return 7879

    #白金
def platinum_sakimono(zone):
    if zone == "08:45":
        return 3721
    if zone == "15:15":
        return 3756
    if zone == "16:30":
        return 3803
    if zone == "y06:00":
        return 3800
    if zone == "y15:15":
        return 3824
    
    #億万先物(金)
def okumansakimono_main_buy_result_gold(zone):
    if zone == "日中":
        return "買い"
    if zone == "夜間":
        return "買い"

    #億万先物(白金)
def okumansakimono_main_buy_result_platinum(zone):
    if zone == "日中":
        return "売り"
    if zone == "夜間":
        return "売り"
    
    #システム先物(金)
def sisutemusakimono_main_buy_result_gold(zone):
    if zone == "日中":
        return "売り"
    if zone == "夜間":
        return "買い"

    #システム先物(白金)
def sisutemusakimono_main_buy_result_platinum(zone):
    if zone == "日中":
        return "買い"
    if zone == "夜間":
        return "買い"
    
    #はばたけ先物(金)
def habatakesakimono_main_buy_result_gold(zone):
    if zone == "日中":
        return "買い"
    if zone == "夜間":
        return "買い"
    if zone == "日通し":
        return "買い"

    #はばたけ先物(白金)
def habatakesakimono_main_buy_result_platinum(zone):
    if zone == "日中":
        return "買い"
    if zone == "夜間":
        return "買い"
    if zone == "日通し":
        return "買い"
    
    #商品先物(金)
def syohinnsakimono_main_buy_result_gold(zone):
    if zone == "（08：45　→　15：15）":
        return "買い"
    if zone == "（16：30　→　06：00）":
        return "買い"
    if zone == "（16：30　→　15：15）":
        return "買い"

    #商品先物(白金)
def syohinnsakimono_main_buy_result_platinum(zone):
    if zone == "（08：45　→　15：15）":
        return "買い"
    if zone == "（16：30　→　06：00）":
        return "売り"
    if zone == "（16：30　→　15：15）":
        return "買い"
    
  #ビット/円(売り)
def kasou_bit_en(zone):
    if zone == "09:00":
        return 2929105
    if zone == "21:00":
        return 2929105
    #翌日ビット/円(売り)
    if zone == "y09:00":
        return 2921105

    
#仮想システム
def kasousisutemu_main_buy_result(zone):
    if zone == "9：00　→　21：00":
        return "買い"
    if zone == "21：00　→　09：00":
        return "買い"
# 仮想通貨
# 先物




