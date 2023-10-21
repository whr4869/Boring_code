import csv

# 读取CSV文件
with open('input.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)

# 转换为指定格式
result = []
for row in rows:
    question = row[0]
    answer = row[1]
    formatted_row = {
        'question': question,
        'answer': answer
    }
    result.append(formatted_row)

# 将转换结果保存到文本文件
with open('output.txt', 'w', encoding='utf-8') as file:
    for item in result:
        file.write("{ question: '" + item['question'] + "', answer: '" + item['answer'] + "' },\n")
