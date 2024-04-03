import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def GetAllHttpProxy():
    proxies = []
    proxyList = requests.get("http://127.0.0.1:5010/all/").json()
    for item in proxyList:
        proxies.append("http://" + item['proxy'])
    return proxies


def GetLatestLaunchpad():
    b = webdriver.Chrome()
    while True:
        b.get('https://www.binance.com/zh-CN/support/search?type=1&q=launchpad')
        for e in b.find_elements(By.CLASS_NAME, 'css-116fqin'):
            if "第51期项目" in e.text:
                return
            print(e.text)
        time.sleep(10)
        b.refresh()


def main():
    GetLatestLaunchpad()


if __name__ == '__main__':
    main()
