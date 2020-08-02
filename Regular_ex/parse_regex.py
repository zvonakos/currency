import csv
import re

PATH = './nginx.log'

regex = re.compile(
    r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*\[(?P<date>.*)\].*  \"'
    r'(?:POST|GET|DELETE|PUT|HEAD|OPTIONS|CONNECT)\s(.*?)\sHTTP\/\d\.\d'
)

with open(PATH) as file:
    with open('nginx_regex.csv', 'w', newline='') as csv_file:
        data_writer = csv.writer(csv_file, delimiter=',')
        for index, line in enumerate(file):
            res = regex.search(line)
            if res is not None:
                res = res.groupdict()

                ip = res['ip']
                date = res['date']
                method = res['POST|GET|DELETE|PUT|HEAD|OPTIONS|CONNECT']
                path = '/' + res['HTTP']
                data_writer.writerow([ip, date, method, path])
