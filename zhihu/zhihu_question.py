import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ZhihuQuestionSpider(object):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(options=chrome_options)

    def request(self, url):
        self.browser.get(url)
        self.browser.implicitly_wait(10)
        num = self.browser.find_element_by_xpath(
            '//main/div/div[2]/div[1]/div/div/div/div/div/div[1]/h4/span').text
        print(num)
        num = re.search(r'\d+,?\d+', num).group().replace(',', '')
        num = int(num)
        print()
        while True:
            self.browser.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)')
            self.browser.execute_script(
                'window.scrollTo(0, document.body.scrollHeight/10*9)')

            # time.sleep(0.5)
            try:
                self.browser.implicitly_wait(0.1)
                last = self.browser.find_element_by_xpath(
                    f'//main/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div[{num}]')
                break
            except:
                last = self.browser.find_element_by_xpath(
                    f'//main/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div[last()-1]')
                print(last.find_element_by_xpath('./div').get_attribute('data-zop'))
            return self.browser.page_source

            



if __name__ == '__main__':
    q = ZhihuQuestionSpider()
    url = 'https://www.zhihu.com/question/336203471'
    q.request(url)
