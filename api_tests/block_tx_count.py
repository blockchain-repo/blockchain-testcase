import json
import requests
import time

delay = 3

with open('api_config') as fp:
    config = json.load(fp)

print("api config: ", config)
url = 'http://{}:{}/uniledger/v1/transaction/queryGroupByBlock'.format(config['ip'], config['port'])

res = requests.post(url)
print("api response:", res.json())
