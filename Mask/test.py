from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import time


#클립보드에 input을 복사한 뒤
#해당 내용을 actionChain을 이용해 로그인 폼에 붙여넣기
def copy_input(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)


id = 'sponjjanc'
pw = 'sldjaak12'

driver = webdriver.Chrome(r'C:/Users/sponj/PycharmProjects/python/Mask/chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://nid.naver.com/nidlogin.login')

copy_input('//*[@id="id"]', id)
time.sleep(1)
copy_input('//*[@id="pw"]', pw)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()