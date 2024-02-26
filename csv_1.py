import csv

with open('douban_top20.csv', encoding='utf-8') as inCSVfile:
    csvreader = csv.reader(inCSVfile)
    for row in csvreader:
        print("书名：", row[0])
        print("作者：", row[1])
        print("出版社：", row[2])
        print("出版日期", row[3])
        print("豆瓣评分：", row[4])
        print("定价：", row[5])
