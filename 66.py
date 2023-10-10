import requests
from bs4 import BeautifulSoup

url = "http://fund.eastmoney.com/014806.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

fund_name_element = soup.find("div", class_="fundDetail-tit")
if fund_name_element and fund_name_element.h1:
    fund_name = fund_name_element.h1.text.strip()
else:
    fund_name = "未知基金名称"

print(fund_name)

