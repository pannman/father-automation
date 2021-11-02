from selenium import webdriver
import time
from package.fc2.sakimononikkei import Sakimononikkei
from package.fc2.yumewogenzituni import Yumewogenzituni
from package.fc2.sakusesunikki import Sakusesunikki
from package.fc2.katigumi import Katigumi
from package.fc2.megami import Megami
from package.fc2.yuga import Yuga
from package.fc2.subarashiki import Subarashiki
from package.fc2.toshi import Toshi
from package.fc2.okuman import Okuman
from package.fc2.bara import Bara
from package.fc2.habatake import Habatake
from package.fc2.kyoifx import Kyoifx
from package.fc2.sararimanfx import Sararimanfx
from package.fc2.toshijutufx import Toshijutufx
from package.fc2.fxtoshinikki import Fxtoshinikki
from package.fc2.okumanfx import Okumanfx
from package.fc2.habatakefx import Habatakefx
from package.fc2.miraienotyousennfx import Miraienotyousennfx
from package.fc2.seikoufx import Seikoufx
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# #設定
# options = webdriver.ChromeOptions()
# # Selenium Server に接続する
# driver = webdriver.Remote(
#     command_executor='http://localhost:4444/wd/hub',
#     options=options,
# )
driver = webdriver.Chrome(executable_path="./chromedriver")
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
driver.set_window_size('300', '300')

# #先物日経
# sakimononikkei = Sakimononikkei(driver)
# sakimononikkei.automation(9)

# #夢を現実に
# yumewogenzituni = Yumewogenzituni(driver)
# yumewogenzituni.automation(9)

# #サクセス
# sakusesunikki = Sakusesunikki(driver)
# sakusesunikki.automation(9)

# #勝ち組
# katigumi = Katigumi(driver)
# katigumi.automation(9)

# #幸運の女神
# megami = Megami(driver)
# megami.automation(9)

# #優雅な生活
# yuga = Yuga(driver)
# yuga.automation(9)

# #素晴らしき人生
# subarashiki = Subarashiki(driver)
# subarashiki.automation(9)

# #投資日記
# toshi = Toshi(driver)
# toshi.automation(9)

# #億万長者
# okuman = Okuman(driver)
# okuman.automation(9)

# #薔薇の人生
# bara = Bara(driver)
# bara.automation()

# #はばたけ未来へ
# habatake = Habatake(driver)
# habatake.automation(9)

# #脅威のFXトレード
# kyoifx = Kyoifx(driver)
# kyoifx.automation(9)

# #サラリーマンFX
# sararimanfx = Sararimanfx(driver)
# sararimanfx.automation(9)

# #世界の市場時間にあわせたFX投資術
# toshijutufx = Toshijutufx(driver)
# toshijutufx.automation(9)

# #FX投資日記
# fxtoshinikki = Fxtoshinikki(driver)
# fxtoshinikki.automation(9)

# #億万FX
# okumanfx = Okumanfx(driver)
# okumanfx.automation(9)

# #未来への挑戦FX
# miraienotyousennfx = Miraienotyousennfx(driver)
# miraienotyousennfx.automation(9)

# #成功のfx
# seikoufx = Seikoufx(driver)
# seikoufx.automation(9)

#はばたけfx
habatakefx = Habatakefx(driver)
habatakefx.automation(9)


