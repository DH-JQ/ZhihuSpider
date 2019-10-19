"""
需要Selenium接管本地浏览器
详情参考：https://blog.csdn.net/weixin_42960354/article/details/101321783
 """
import json
import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 接管本地浏览器配置
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "/usr/bin/chromedriver"


class Zhihu(object):
    """ 知乎爬虫 """
    def __init__(self):
        self.browser = webdriver.Chrome(
            chrome_driver,
            chrome_options=chrome_options)

    def login(self, username, password):
        """ 登录
        :param username: 用户名
        :param password: 密码
        """
        self.browser.get('http://www.zhihu.com/')
        print(self.browser.title)
        pwd_login = self.browser.find_element_by_xpath(
            '//div[@class="SignFlow-tab"]')
        print(pwd_login.text)
        pwd_login.click()
        input_username = self.browser.find_element_by_xpath(
            '//input[@name="username"]')
        input_username.click()
        input_username.send_keys(username)
        input_pwd = self.browser.find_element_by_xpath(
            '//input[@name="password"]')
        input_pwd.click()
        input_pwd.send_keys(password)
        login_btn = self.browser.find_element_by_xpath(
            '//button[@type="submit"]')
        print(login_btn.text)
        login_btn.click()
        time.sleep(3)
        print(self.browser.title)

    def parse_hot(self):
        """ 提取热榜信息 """
        hot_btn = self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/main/div/div/div[1]/div/div[1]/nav/a[3]')
        hot_btn.click()
        time.sleep(3)

        # 解析页面
        html = etree.HTML(self.browser.page_source)
        hot_list = html.xpath('.//div[@class="HotList-list"]/section')
        items = {}
        for li in hot_list:
            item = {}
            item['index'] = li.xpath('./div[1]//div/text()')[0]
            item['title'] = li.xpath('./div[2]/a/@title')[0]
            item['url'] = li.xpath('./div[2]/a/@href')[0]
            img_url = li.xpath('.//a/@href')
            item['img_url'] = img_url[0] if img_url else ""
            items.setdefault(item['index'], item)
        return items

    def save(self, items):
        with open('zhihu_hot.json', 'w', encoding='utf-8') as f:
            json.dump(items, f, ensure_ascii=False)


if __name__ == '__main__':
    zhihu = Zhihu()
    # 替换成正确的用户名和账号
    username = 'duhao'
    password = '123456789'
    zhihu.login(username, password)
    hot_items = zhihu.parse_hot()
    zhihu.save(hot_items)
