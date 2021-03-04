import io
import os
import jieba
import jieba.analyse
import csv_util as util

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

for file in files:
    file_path = file_dir + "/" + file
    if os.path.isfile(file_path):
        header = ['word', 'count']
        csv_file = file_dir + '/csv/' + file.split(".")[0] + '.csv'
        print('create new csv file: ', csv_file)
        util.create_csv(csv_file, header)

        txt = io.open(file_path, "r", encoding='gbk').read()
        words = jieba.lcut(txt)
        # words = jieba.analyse.textrank(txt, topK=500, withWeight=False,
        #                                allowPOS=('ns', 'nr', 'nt', 'nw', 'n', 'vn'))  # 词性'ns', 'n', 'vn', 'v'
        counts = {}
        for word in words:
            if len(word) == 1:
                continue
            else:
                counts[word] = counts.get(word, 0) + 1
        items = list(counts.items())
        items.sort(key=lambda x: x[1], reverse=True)

    for i in items:
        word, count = i
        rowData = [word, count]
        print(rowData)
        util.write_csv(csv_file, rowData)
