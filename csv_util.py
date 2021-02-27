import csv
import os


def create_csv(file_path, header):
    if os.path.exists(file_path):
        os.remove(file_path)
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as f:
            csv_write = csv.writer(f)
            # csv_head = ["good", "bad"]
            csv_write.writerow(header)


def write_csv(file_path, rowData):
    with open(file_path, 'a+', newline='') as f:
        csv_write = csv.writer(f)
        # data_row = ["1", "2"]
        csv_write.writerow(rowData)


def read_csv(file_path):
    with open(file_path, "r") as f:
        csv_read = csv.reader(f)
        for line in csv_read:
            print(line)

# file_path = 'test.csv'
# head = ['c1', 'c2']
# create_csv(file_path, head)
# rowData = ['1', '2']
# write_csv(file_path, rowData)
# rowData = ['1', '2']
# write_csv(file_path, rowData)
# read_csv(file_path)
