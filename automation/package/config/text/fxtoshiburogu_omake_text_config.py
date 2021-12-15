from .. import all_config as CONFIG

class FxtoshiburoguOmakeText():
    def blog_title(self):
        return "＊" + str(CONFIG.reserve_year()) + "/" + str(CONFIG.reserve_month()) + "/" + str(CONFIG.reserve_day()) + "　売買シグナル＊"
    def blog_text(self):
        return "売買シグナルは、08：50迄にメールさせて頂きました。\n"\
            "" + str(CONFIG.reserve_year()) + "/" + str(CONFIG.reserve_month()) + "/" + str(CONFIG.reserve_day()) + "　09：00　→　" + str(CONFIG.reserve_year()) + "/" + str(CONFIG.reserve_month()) + "/" + str(CONFIG.reserve_day() + 1) + "　08：30＊"
