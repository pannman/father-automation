from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from package.fc2.fxtecunikaruponndo import Fxtecunikaruponndo
from package.fc2.fxtecunikarudoru import Fxtecunikarudoru
from package.fc2.fxtecunikaruyuro import Fxtecunikaruyuro



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

    # fxテクニカルドル2
    fxtecunikarudoru = Fxtecunikarudoru(driver)
    fxtecunikarudoru.automation(2)
    
    # fxテクニカルユーロ2
    fxtecunikaruyuro = Fxtecunikaruyuro(driver)
    fxtecunikaruyuro.automation(2)
    
    # fxテクニカルポンド2
    fxtecunikaruponndo = Fxtecunikaruponndo(driver)
    fxtecunikaruponndo.automation(2)

except Exception as e:
    print(e)
    driver.quit()
finally:
    driver.quit()
