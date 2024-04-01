import json
import time

import requests
from selenium import webdriver
from binance.client import Client
from selenium.webdriver import Proxy
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import ProxyType


def Trade():
    cli = Client(
        '',
        '', )
    print(cli.futures_create_order(
        symbol='BNBUSDT',
        quantity=28,
        side='BUY',
        type='MARKET',
        positionSide='LONG'
    ))
    cli.close_connection()


def GetAllHttpProxy():
    proxies = []
    proxyList = requests.get("http://127.0.0.1:5010/all/").json()
    for item in proxyList:
        proxies.append("http://" + item['proxy'])
    return proxies


def GetLatestLaunchpad2():
    while True:
        proxies = GetAllHttpProxy()
        for proxy in proxies:
            options = webdriver.ChromeOptions()
            options.add_argument('--proxy-server=' + proxy)
            b = webdriver.Chrome(options=options)
            b.get('https://www.binance.com/zh-CN/support/search?type=1&q=launchpad')
            for e in b.find_elements(By.CLASS_NAME, 'css-116fqin'):
                if "第51期项目" in e.text:
                    return
                print(e.text)
            b.close()


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


def SendLarkMsg():
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'msg_type': 'text',
        'content': {
            'text': '有新的 launchpad 了',
        }
    }
    response = requests.post('https://open.larksuite.com/open-apis/bot/v2/hook/afd3d7e3-c25b-4944-9779-a5b038e0f353',
                             headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return True
    else:
        return False


def main():
    GetLatestLaunchpad()
    Trade()
    for i in range(100):
        SendLarkMsg()


if __name__ == '__main__':
    main()
