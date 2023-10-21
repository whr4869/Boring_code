import pandas as pd
import re

# 获取用户输入的颜色数量
num_colors = int(input("输入操作的数量: "))

# 初始化一个列表来存储颜色代码
colors = [[] for _ in range(num_colors)]

# 打开并读取文件，指定编码为UTF-8
with open('colors.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # 使用正则表达式提取颜色代码
        codes = re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}', line)
        # 过滤掉长度不为7的颜色代码
        codes = [code for code in codes if len(code) == 7]
        # 如果找到足够的颜色代码，将它们添加到对应的列表
        if len(codes) >= num_colors:
            for i in range(num_colors):
                colors[i].append(codes[i])

# 创建一个字典，其中键是列名，值是对应的数据
data = {f'color{i+1}': colors[i] for i in range(num_colors)}

# 创建一个DataFrame
df = pd.DataFrame(data)

# 将DataFrame写入.xlsx文件
df.to_excel('colors.xlsx', index=False)
