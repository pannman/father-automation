from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from package.fc2.habatakesakimono import Habatakesakimono
from package.fc2.syohinnsakimono import Syohinnsakimono




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

    # はばたけ先物日通し
    habatakesakimono = Habatakesakimono(driver)
    habatakesakimono.automation(2)
    
    # 商品先物日通し
    syohinnsakimono = Syohinnsakimono(driver)
    syohinnsakimono.automation(2)

except Exception as e:
    print(e)
    driver.quit()
finally:
    driver.quit()
