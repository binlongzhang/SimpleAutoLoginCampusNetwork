# -*- coding: utf-8 -*-
"""
@Time ： 2021/9/24 16:59
@Auth ： binlongzhang
@File ：main.py
@Github ：https://github.com/binlongzhang
@E-mail：binlong_zhang@163.com
"""

import requests
import socket
import json
#获取本机电脑名


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

ip = get_host_ip()
# url示例
# url = 'http://172.16.253.3:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&user_account=Q21201135%40telecom&user_password=610202199901202418' \
#       '&wlan_user_ip=172.19.12.40&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=172.16.253.1&wlan_ac_name=&jsVersion=3.3.2&v=4861'


with open("./userData.json",'r') as load_f:
    user = json.load(load_f)
user['wlan_user_ip'] = ip

print(user)
url = 'http://172.16.253.3:801/eportal/'

response = requests.get(url,params=user)
print(response.text)
print("回应代码{}".format(response.status_code ))  # 打印状态码


