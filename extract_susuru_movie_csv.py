import urllib.request
import urllib.parse
import json
import csv
import isodate
import datetime
import re

input_filename = "20230111_201817" + "_UCXcjvt8cOfwtcqaMeE7-hqA_channel-video-info.csv"
output_filename = "susuru.csv"

# csvをすべて読み込む
content = []

with open(input_filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    # 二次元配列になる
    content = [row for row in csvreader]


with open(output_filename, 'w', encoding='utf8') as f:
    writer = csv.writer(f)
    for row in content:
        index1 = row[1].rfind("第") + 1
        index2 = row[1].rfind("回")
        if(index1 != -1 and index2 != -1):
            count = row[1][index1:index2]
            title = row[1]
            url = row[3]
            genre = ""
            #店名
            index1 = row[2].find("【本日のお店】") + len("【本日のお店】") + len("\n")
            index2 = index1 + row[2][index1:].find("\n")
            name = row[2][index1:index2]
            #住所
            index2 = index2 + len("\n")
            index3 = index2 + row[2][index2:].find("\n")
            address = row[2][index2:index3]

            out = count + "," + title + "," + url + "," +  genre + "," + address + "," + name
            print(out)
            writer.writerow([count,title,url,genre,address,name])

