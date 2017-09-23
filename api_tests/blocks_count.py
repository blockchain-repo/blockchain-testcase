from time import sleep
import json
import requests

delay = 3

with open('api_config') as fp:
    config = json.load(fp)

print("api config: ",config)
url = 'http://{}:{}/uniledger/v1/block/queryBlockCount'.format(config['ip'],config['port'])

res = requests.post(url)
print("api response:",res.json())

