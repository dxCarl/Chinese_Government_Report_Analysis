import io
import os
import jieba
import csv_util as util
import jieba.analyse

jieba.load_userdict("userdict.txt")
jieba.add_word('财政支出')
jieba.add_word('经济增长')
jieba.add_word('支出结构')
jieba.add_word('科教文卫')
jieba.add_word('社会保障')
jieba.add_word('基础设施')
jieba.add_word('财政补贴')
jieba.add_word('财政预算')
jieba.add_word('社会保障')

file_dir = "./data"  # 文件夹目录
files = os.listdir(file_dir)  # 得到文件夹下的所有文件名称
s = []
csv_file = ''
full_text = ''
for file in files:
    file_path = file_dir + "/" + file
    if os.path.isfile(file_path):
        txt = io.open(file_path, "r", encoding='gbk').read()
        full_text = full_text + txt

    words = jieba.lcut(full_text)
# words = jieba.analyse.textrank(full_text, topK=500, withWeight=False,
#                                allowPOS=('ns', 'nr', 'nt', 'nw', 'n', 'vn'))  # 词性'ns', 'n', 'vn
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())

items.sort(key=lambda x: x[1], reverse=True)

header = ['word', 'count']
csv_file = file_dir + '/csv/total.csv'
print('create new csv file: ', csv_file)
util.create_csv(csv_file, header)
for i in items:
    word, count = i
    rowData = [word, count]
    print(rowData)
    util.write_csv(csv_file, rowData)
