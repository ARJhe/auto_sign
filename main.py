from selenium import webdriver
from datetime import datetime as dt
import time
from log.logger import create_logger

logger = create_logger('SignLog')

def main():
    _today = f"{dt.today().month}/{dt.today().day} "
    _hour = dt.today().hour
    try:
        _driver = webdriver.Chrome()
        if _hour < 12:
            url = "https://forms.gle/dGdVdwKNdqE9NddV6"
            sign_type = '簽到'
        else:
            url = "https://forms.gle/dv5mDMfRjV8KCYP7A"
            sign_type = '簽退'
        _driver.get(url)

        department = _driver.find_element_by_id("i8")
        department.click()
        name = _driver.find_element_by_css_selector("input[aria-labelledby='i14']")
        name.send_keys('洪崑哲')
        sign = _driver.find_element_by_css_selector("input[aria-labelledby='i18']")
        sign.send_keys(_today + sign_type)
        time.sleep(3)
        submit = _driver.find_element_by_xpath("//span[text()='提交']")
        submit.click()
        time.sleep(2)
        logger.info(f"{sign_type} 成功")
    except Exception as e:
        logger.info(f"{sign_type} 失敗")

    _driver.close()



if __name__ == '__main__':
    main()