import csv
import requests
import os
import json
import urllib
# opener = urllib.build_opener()
# opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')]
URL = 'https://dummy.restapiexample.com/api/v1/create'
PARAMS = {"name": "test", "salary": "", "age": "23"}

file_name = "sample.csv"
if os.stat(file_name).st_size == 0:
    print('File is empty')
    PARAMS = {"name": "test", "salary": "*", "age": "23"}
    r = requests.post(url=URL, params=PARAMS)

    print(r.status_code)
    print(r.text)

else:
    print('File is not empty')
    with open('sample.csv', mode='r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            PARAMS["salary"] = line[0]
            NEW_PARAMS = json.dumps(PARAMS)  # ' ' -> " "
            print("PARAMS: ", PARAMS)
            res = json.loads(NEW_PARAMS)
            print(type(PARAMS))
            print(type(NEW_PARAMS))
            print(type(res))
            print("NEW PARAMS: ", NEW_PARAMS)
            # print(line)
            # POST REQUEST
            # print(URL)
            r = requests.post(URL, json=res)
           
            # print(r.status_code)
            # print(r.text)
