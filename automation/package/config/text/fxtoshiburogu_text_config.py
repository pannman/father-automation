from .. import all_config as CONFIG


class  FxtoshiburoguText():
    def __init__(self, zone , zone_state , zone_state_euro , zone_state_lb , zone_state_euro_dol , zone_state_lb_dol , main_sign , main_sign_euro , main_sign_lb , main_sign_euro_dol , main_sign_lb_dol , main_total , main_total_euro , main_total_lb , main_total_euro_dol , main_total_lb_dol , zone_dollar , zone_euro , zone_lb , zone_euro_dol , zone_lb_dol , zone_settlement , zone_settlement_euro , zone_settlement_lb , zone_settlement_euro_dol , zone_settlement_lb_dol , buy_time , settlement_time ):
        self.zone  = zone 
        self.buy  = zone_state 
        self.buy_euro  = zone_state_euro 
        self.buy_lb  = zone_state_lb 
        self.buy_euro_dol  = zone_state_euro_dol 
        self.buy_lb_dol  = zone_state_lb_dol 
        self.main_sign  = main_sign 
        self.main_sign_euro  = main_sign_euro 
        self.main_sign_lb  = main_sign_lb 
        self.main_sign_euro_dol  = main_sign_euro_dol 
        self.main_sign_lb_dol  = main_sign_lb_dol 
        self.main_total  = main_total 
        self.main_total_euro  = main_total_euro 
        self.main_total_lb  = main_total_lb 
        self.main_total_euro_dol  = main_total_euro_dol 
        self.main_total_lb_dol  = main_total_lb_dol 
        self.zone_dollar  = zone_dollar 
        self.zone_euro  = zone_euro 
        self.zone_lb  = zone_lb 
        self.zone_euro_dol  = zone_euro_dol 
        self.zone_lb_dol  = zone_lb_dol 
        self.zone_settlement  = zone_settlement 
        self.zone_settlement_euro  = zone_settlement_euro 
        self.zone_settlement_lb  = zone_settlement_lb 
        self.zone_settlement_euro_dol  = zone_settlement_euro_dol 
        self.zone_settlement_lb_dol  = zone_settlement_lb_dol 
        self.buy_time  = buy_time 
        self.settlement_time  = settlement_time 

        
        if self.settlement_time == "y08:30":
            self.settlement_time = "08s：30"
        if self.main_sign  == "0":
            self.main_sign  = "±0"
        if self.buy == "買い":
            self.buy == "ASK"
        if self.buy == "売り":
            self.buy == "BID"
        if self.buy_euro == "買い":
            self.buy_euro == "ASK"
        if self.buy_euro == "売り":
            self.buy_euro == "BID"
        if self.buy_lb == "買い":
            self.buy_lb == "ASK"
        if self.buy_lb == "売り":
            self.buy_lb == "BID"
        if self.buy_euro_dol == "買い":
            self.buy_euro_dol == "ASK"
        if self.buy_euro_dol == "売り":
            self.buy_euro_dol == "BID"
        if self.buy_lb_dol == "買い":
            self.buy_lb_dol == "ASK"
        if self.buy_lb_dol == "売り":
            self.buy_lb_dol == "BID"

        print(zone )
        print("ドル")
        print(self.buy  + "   "+str(self.zone_dollar ) +
              "   決済    " + str(self.zone_settlement ) + "")
        print("メイン   " + self.main_sign +"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total )
        print("ユーロ")
        print(self.buy_euro  + "   "+str(self.zone_euro ) +
              "   決済    " + str(self.zone_settlement_euro ) + "")
        print("メイン   " + self.main_sign_euro +"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total_euro )
        print("ポンド")
        print(self.buy_lb  + "   "+str(self.zone_lb ) +
              "   決済    " + str(self.zone_settlement_lb ) + "")
        print("メイン   " + self.main_sign_lb +"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total_lb )
        print("ユーロ/ドル")
        print(self.buy_euro_dol  + "   "+str(self.zone_euro_dol ) +
              "   決済    " + str(self.zone_settlement_euro_dol ) + "")
        print("メイン   " + self.main_sign_euro_dol +"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total_euro_dol )
        print("ポンド/ドル")
        print(self.buy_lb_dol  + "   "+str(self.zone_lb_dol ) +
              "   決済    " + str(self.zone_settlement_lb_dol ) + "")
        print("メイン   " + self.main_sign_lb_dol +"    " +
              str(CONFIG.result_month()) + "月累計   " + self.main_total_lb_dol )

    def blog_title(self):
        return "" + str(CONFIG.result_year()) + "/" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "　売買シグナル＊"

    def blog_text(self):
        return "" + str(CONFIG.result_year()) + "/" + str(CONFIG.result_month()) + "/" + str(CONFIG.result_day()) + "　09：00　→　" + str(CONFIG.y_result_year()) + "/" + str(CONFIG.y_result_month()) + "/" + str(CONFIG.y_result_day() ) + "　08：30　の結果\n\n"\
            "ドル/円\n\n"\
            ""+self.buy+"" + self.main_sign +"pips\n\n"\
            "累計 　 " + self.main_total + "pips(" + str(CONFIG.reserve_year()) + "/" + str(CONFIG.reserve_month()) + " ドル/円)\n\n"\
            "ユーロ/円\n\n"\
            ""+self.buy_euro+"" + self.main_sign_euro + "pips\n\n"\
            "累計 　 " + self.main_total_euro + "pips(" + str(CONFIG.reserve_year()) + "/" + str(CONFIG.reserve_month()) + " ユーロ/円)\n\n"\
            "ユーロ/ドル\n\n"\
            ""+self.buy_euro_dol+"" + self.main_sign_euro_dol + "pips\n\n"\
            "累計 　 " + self.main_total_euro_dol + "pips(" + str(CONFIG.reserve_year()) + "/" + str(CONFIG.reserve_month()) + " ユーロ/ドル)\n\n"\
            "ポンド/円\n\n"\
            ""+self.buy_lb+"" + self.main_sign_lb + "pips\n\n"\
            "累計 　 " + self.main_total_lb + "pips(" + str(CONFIG.reserve_year()) + "/" + str(CONFIG.reserve_month()) + " ポンド/円)\n\n"\
            "ポンド/ドル\n\n"\
            ""+self.buy_lb_dol+"" + self.main_sign_lb_dol + "pips\n\n"\
            "累計 　 " + self.main_total_lb_dol + "pips(" + str(CONFIG.reserve_year()) + "/" + str(CONFIG.reserve_month()) + " ポンド/ドル)\n\n"\
          
