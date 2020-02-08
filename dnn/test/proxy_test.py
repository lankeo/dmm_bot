import requests

#免费代理或不用密码的代理
url = 'http://www.r18.com/'

proxy = '192.168.44.2:8118'

proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}


response = requests.get(url, proxies=proxies)
print(response.text)