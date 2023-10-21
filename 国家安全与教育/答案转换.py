from bs4 import BeautifulSoup
from docx import Document

# 创建一个Word文档对象
doc = Document()

# 打开本地HTML文件
with open('666.html', 'r', encoding='utf-8') as html_file:
    content = html_file.read()

    # 创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser')

    # 找到所有的p标签
    p_tags = soup.find_all('p')

    # 将所有p标签的文本添加到Word文档中
    for tag in p_tags:
        doc.add_paragraph(tag.text)

# 保存Word文档
doc.save('output.docx')
