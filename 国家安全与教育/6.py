import csv
from bs4 import BeautifulSoup

# 打开本地HTML文件
with open('666.html', 'r', encoding='utf-8') as html_file:
    content = html_file.read()

    # 创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser')

    # 找到所有的p标签
    p_tags = soup.find_all('p')

    # 创建一个CSV文件
    with open('output.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # 将所有p标签的文本写入CSV文件
        for tag in p_tags:
            writer.writerow([tag.text])
