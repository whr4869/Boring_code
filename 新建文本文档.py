import requests
from bs4 import BeautifulSoup

url = 'http://fund.eastmoney.com/160643.html'  # 这里以鹏华空天军工指数为例
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 查找基金净值的元素
net_value_element = soup.find_all('span', {'id': 'gz_gsz'})[0]
net_value = net_value_element.text  # 获取基金净值

print('华安创新动力混合的最新净值为:', net_value)
