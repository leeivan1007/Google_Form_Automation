# 修改時間 2018/7/11
# 版本 1.0.0.0
# 同目錄需有config.txt
# 前三行為 email: xxx@g4.com.tw
#         password: xxxx1234
#         your_form_name: Tom
# 尚未新增功能:
# 1.輸入法檢查
# 2.清空與返回

from selenium import webdriver
from bs4 import BeautifulSoup
import urllib
import time
import random
import selenium.webdriver.support.ui as ui

def investigate_by_xpath(driver, time_wait, object, message):
	# input : 等待時間, 確認目標的xpath內容, 成功回報訊息
    # target : 因驗證帳密會有延遲時間, 故此function為確認有無正常進入下一動作
    wait = ui.WebDriverWait(driver, time_wait)
    wait.until(lambda driver: driver.find_element_by_xpath(object).is_displayed())
    print(message)
def write_daily_record(driver, content, hour, minute, second, next_context):
	# driver, 工作內容, 小時, 分鐘, 秒, 是否繼續
    driver.find_element_by_xpath('//input[@aria-label="工作內容"]').send_keys(content)
    driver.find_element_by_xpath('//input[@aria-label="小時"]').send_keys(hour)
    driver.find_element_by_xpath('//input[@aria-label="分鐘"]').send_keys(minute)
    driver.find_element_by_xpath('//input[@aria-label="秒"]').send_keys(second)
    driver.find_element_by_xpath('//div[@data-value="{}"]'.format(next_context)).click()
    driver.find_element_by_xpath('//span[contains(text(),"繼續")]').click()
def load_config(config_file_path):
	# config.txt 路徑
    with open(config_file_path) as config:
        line = config.read()

    information = line.split('\n')

    email = information[0]
    password = information[1]
    form_url = information[2]
    user_name = information[3]
    return email, password, form_url, user_name

def input_task_information():
    tasks = []
    while True:
        content_dict = {}
        content_dict['content'] = information_content()
        content_dict['hour'] = information_hour()
        content_dict['minute'] = information_minute()
        content_dict['second'] = information_second()
        next_context = input('是否繼續填寫下一份工作?(是則輸入Y/否則直接按Enter)').lower()
        content_dict['next_context'] = '是' if next_context == 'y' else '否'
        
        tasks.append(content_dict)
        if content_dict['next_context'] == "否":
            break
    return tasks
def information_content():
    information = ''
    while True:
        information = input('工作內容：')
        if information != '':
            break
        print('幹\n是都沒在上班哦')
    return information
def information_hour():
    information = ''
    while True:
        information = input('小時：')
        if not information.isdigit():
            print('請輸入數字')
        elif int(information) == 0:
            print('幹是都沒在上班哦')
        elif int(information) >= 12:
            print('有你真好,台灣經濟靠你了')
        else:
            break
    return information
def information_minute():
    information = ''
    while True:
        information = input('分鐘：')
        if information == '':
            information = '00'
            break
        elif not information.isdigit():
            print('請輸入數字')
        elif int(information) > 60:
            print('一分鐘{},好棒棒'.format(information))
        else:
            break
    return information
def information_second():
    information = ''
    while True:
        information = input('秒：')
        if information == '':
            information = '00'
            break
        elif not information.isdigit():
            print('請輸入數字')
        elif int(information) > 60:
            print('一小時{},好棒棒'.format(information))
        else:
            break
    return information

def main():

    # 使用者填寫task資訊
    tasks = input_task_information()

    email, password, form_url, user_name = load_config('Google_Form_Automation/config.txt')

    # 認證

    driver = webdriver.Chrome()
    url = 'https://www.google.com'
    driver.get(url) 

    driver.find_element_by_xpath('//a[contains(text(),"登入")]').click()
    investigate_by_xpath(driver, 10, '//input[@type="email"]', '開始輸入資訊!')

    driver.find_element_by_xpath('//input[@type="email"]').send_keys(email)
    driver.find_element_by_xpath('//span[contains(text(),"繼續")]').click()
    investigate_by_xpath(driver, 10, '//input[@type="password"]', '郵件輸入成功!')

    driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
    driver.find_element_by_xpath('//span[contains(text(),"繼續")]').click()
    investigate_by_xpath(driver, 10, '//input[@class="gsfi"]', '密碼輸入成功!')

    # 進入表單
    driver.get(form_url)

    # 輸入ID
    driver.find_element_by_xpath('//div[@role="radio"][@data-value="{}"]'.format(user_name)).click()
    driver.find_element_by_xpath('//span[contains(text(),"繼續")]').click()

    for task in tasks:
    	write_daily_record(driver, task['content'], task['hour'], task['minute'], task['second'], task['next_context'])

    driver.find_element_by_xpath('//span[contains(text(),"提交")]').click()
    print('填寫成功!')

if __name__ ==  "__main__":
	main()
