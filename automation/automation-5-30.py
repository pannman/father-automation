from selenium import webdriver
import time
from package.fc2.sakimononikkei import Sakimononikkei
from package.fc2.yumewogenzituni import Yumewogenzituni
from package.fc2.sakusesunikki import Sakusesunikki
# from package.fc2.arakasegi import Arakasegi
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    #設定
    options = webdriver.ChromeOptions()
    # Selenium Server に接続する
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options,
    )
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(10)
    driver.set_window_size('300', '300')

    #夢を現実に
    yumewogenzituni = Yumewogenzituni(driver)
    yumewogenzituni.automation(5)

    #サクセス
    # sakusesunikki = Sakusesunikki(driver)
    # sakusesunikki.automation(5)

except Exception as e:
    print(e)
    driver.quit()
finally:
    driver.quit()
