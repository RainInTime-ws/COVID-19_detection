import csv

filename = 'usa_county_wise.csv'


# 删除有缺失列的数据
def delete_error(List, col):
    for i in range(0, List.__len__())[::-1]:
        if len(List[i]) != col:
            List.pop(List[i])
        else:
            pass


# 只保留数据的有效列
def simple_item(item, cols):
    '''
    :param item:a list, means each item record
    :param cols: a list, means which cols want to delete
    :return: simplified item
    '''
    new_item = []
    for i in range(len(item)):
        if i not in cols:
            new_item.append(item[i])
    return new_item


# 部分日期有错误，进行更正
def correct_date(List):
    List[4] = List[4].replace('200', '')
    return List


# 把纠正简化过的数据写进一个新的csv文件
def new_csv(List):
    '''
    :param List: a list of list, the processed data you want to write in a csv
    :return: no return
    '''
    with open("processed_data.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(List)
    print("processed_data.csv has been written successfully!")


# 整合上面函数，作为调用接口处理原始文件
def data_process(filename):
    with open(filename, encoding='utf8') as f:
        reader = csv.reader(f)
        data = list(reader)
        write_in = []
        delete_error(data, 14)
        for item in data:
            write_row = simple_item(item, [0, 1, 2, 3, 4, 7, 10])
            write_row[4] = write_row[4].replace("200", "a")
            write_row[4] = "a" + write_row[4]
            write_row[4] = write_row[4].replace("aa", "a")
            if write_row[2] == '0':
                continue
            print(write_row)
            write_in.append(write_row)
        new_csv(write_in)
