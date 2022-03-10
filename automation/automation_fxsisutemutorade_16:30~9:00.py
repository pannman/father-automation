from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from package.fc2.fxsisutemutorade import Fxsisutemutorade


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

    # fxシステムトレード16:30~9:00
    fxsisutemutorade = Fxsisutemutorade(driver)
    fxsisutemutorade.automation(2)

except Exception as e:
    print(e)
    driver.quit()
finally:
    driver.quit()
