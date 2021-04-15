from selenium import webdriver
import sys
import login_config as LOGIN
import text_config as TEXT
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Chrome のオプションを設定する
options = webdriver.ChromeOptions()

# Selenium Server に接続する
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options,
)


driver.get('https://fc2.com/login.php?ref=blog')
print(driver.current_url)
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
driver.set_window_size('1200', '1000')
args = sys.argv
r_main_total = open('main_total.txt', 'r').read()
r_sub_total = open('sub_total.txt', 'r').read()
w_main_total = open('main_total.txt', 'w')
w_sub_total = open('sub_total.txt', 'w')

try:
    if not len(args) == 3:
        print("サブサインとメインサインを入力してください")
        raise Exception
    mail = wait.until(EC.presence_of_element_located((By.ID, "id")))
    password = wait.until(EC.presence_of_element_located((By.ID, "pass")))
    login_btn = wait.until(EC.presence_of_element_located((By.NAME, "image")))
    prevmail = mail.get_attribute('input_fc2id_login')
    mail.send_keys(LOGIN.FC2_LOGIN['ID'])
    password.send_keys(LOGIN.FC2_LOGIN['PASS'])
    login_btn.click()
    print(driver.current_url)
    driver.get('https://admin.blog.fc2.com/control.php?mode=editor&process=new')
    print(driver.current_url)
    title = wait.until(EC.presence_of_element_located((By.ID, "entry_title")))
    title.send_keys("日中")
    main_text = wait.until(EC.presence_of_element_located((By.ID, "body")))
    main_text.send_keys(TEXT.fc2_text("日中",args[1],args[2],r_sub_total,r_main_total))
    buttun = driver.find_element_by_class_name("admin_common_positive_btn").click()
    print(r_sub_total)
    print(TEXT.fc2_text("日中",args[1],args[2],r_sub_total,r_main_total))
    w_sub_total.write(str(int(r_sub_total) - int(args[1])))
    w_main_total.write(str(int(r_main_total) - int(args[2])))
except Exception as e:
    print(e)
    w_sub_total.write(r_sub_total)
    w_main_total(r_main_total)
    driver.quit()
finally:
    driver.quit()
    
