import json
import requests
import time

delay = 3

with open('api_config') as fp:
    config = json.load(fp)

print("api config: ", config)
url = 'http://{}:{}/uniledger/v1/timestat/blockCreateAvgTimeByRange'.format(config['ip'], config['port'])

timestamp = str(round(time.time() * 1000))
res = requests.post(url, json={'beginTime': "1487066476", 'endTime': timestamp})
print("api response:", res.json())

