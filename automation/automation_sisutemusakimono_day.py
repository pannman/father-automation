from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from package.fc2.sisutemusakimono import Sisutemusakimono


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

    # システム先物日中
    sisutemusakimono = Sisutemusakimono(driver)
    sisutemusakimono.automation(3)

except Exception as e:
    print(e)
    driver.quit()
finally:
    driver.quit()
