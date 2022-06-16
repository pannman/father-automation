from selenium import webdriver
from package.fc2.tradesisutemu import Tradesisutemu
from package.fc2.victoriousfx import Victoriousfx
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

# システムトレードオーバーナイト
tradesisutemu = Tradesisutemu(driver)
tradesisutemu.automation(5)

# ビクトリアスfx16:30~5:30
victoriousfx = Victoriousfx(driver)
victoriousfx.automation(3)
