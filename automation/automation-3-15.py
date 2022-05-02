from selenium import webdriver
import time
from package.fc2.sakimononikkei import Sakimononikkei
from package.fc2.yumewogenzituni import Yumewogenzituni
from package.fc2.sakusesunikki import Sakusesunikki
from package.fc2.investing import Investing
from package.fc2.katigumi import Katigumi
from package.fc2.megami import Megami
from package.fc2.yuga import Yuga
from package.fc2.subarashiki import Subarashiki
from package.fc2.toshi import Toshi
from package.fc2.okuman import Okuman
from package.fc2.miraie import Miraie
from package.fc2.habatake import Habatake
from package.fc2.kyoifx import Kyoifx
from package.fc2.sararimanfx import Sararimanfx
from package.fc2.toshijutufx import Toshijutufx
from package.fc2.fxtoshinikki import Fxtoshinikki
from package.fc2.okumanfx import Okumanfx
from package.fc2.seikoufx import Seikoufx
from package.fc2.habatakefx import Habatakefx
from package.fc2.miraienotyousennfx import Miraienotyousennfx
from package.fc2.okumansakimono import Okumansakimono
from package.fc2.sisutemusakimono import Sisutemusakimono
from package.fc2.victoriousfx import Victoriousfx
from package.fc2.habatakesakimono import Habatakesakimono
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    #設定
    # options = webdriver.ChromeOptions()
    # Selenium Server に接続する
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
    # sakimononikkei.automation(3)

    # #夢を現実に
    # yumewogenzituni = Yumewogenzituni(driver)
    # yumewogenzituni.automation(3)

    # #サクセス
    # sakusesunikki = Sakusesunikki(driver)
    # sakusesunikki.automation(3)

    # #ミニ投資法
    # investing = Investing(driver)
    # investing.automation(3)

    # #勝ち組
    # katigumi = Katigumi(driver)
    # katigumi.automation(3)

    # #幸運の女神
    # megami = Megami(driver)
    # megami.automation(3)

    # #優雅な生活
    # yuga = Yuga(driver)
    # yuga.automation(3)

    # #素晴らしき人生
    # subarashiki = Subarashiki(driver)
    # subarashiki.automation(3)

    # #投資日記
    # toshi = Toshi(driver)
    # toshi.automation(3)

    # #億万長者
    # okuman = Okuman(driver)
    # okuman.automation(3)

    # #未来への挑戦
    # miraie = Miraie(driver)
    # miraie.automation(3)

    # #はばたけ未来へ
    # habatake = Habatake(driver)
    # habatake.automation(3)

    # # #脅威のFXトレード
    # kyoifx = Kyoifx(driver)
    # kyoifx.automation(3)

    # #サラリーマンFX
    # sararimanfx = Sararimanfx(driver)
    # sararimanfx.automation(3)

    # #世界の市場時間にあわせたFX投資術
    # toshijutufx = Toshijutufx(driver)
    # toshijutufx.automation(3)

    # #FX投資日記
    # fxtoshinikki = Fxtoshinikki(driver)
    # fxtoshinikki.automation(3)

    # #億万FX
    # okumanfx = Okumanfx(driver)
    # okumanfx.automation(3)

    # #未来への挑戦FX
    # miraienotyousennfx = Miraienotyousennfx(driver)
    # miraienotyousennfx.automation(3)

    # #成功のfx
    # seikoufx = Seikoufx(driver)
    # seikoufx.automation(3)

    # #はばたけfx
    # habatakefx = Habatakefx(driver)
    # habatakefx.automation(3)

    # # 億万先物日中
    # okumansakimono = Okumansakimono(driver)
    # okumansakimono.automation(3)

    # # システム先物日中
    # sisutemusakimono = Sisutemusakimono(driver)
    # sisutemusakimono.automation(3)

    # # ビクトリアスfx116:30~5:30
    # victoriousfx = Victoriousfx(driver)
    # victoriousfx.automation(3)
    
    # はばたけ先物日中
    habatakesakimono = Habatakesakimono(driver)
    habatakesakimono.automation(3)


except Exception as e:
    print(e)
    driver.quit()
finally:
    driver.quit()
