import io
import os
import jieba
import csv_util as util

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
