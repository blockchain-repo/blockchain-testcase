from time import sleep
import json
import requests

delay = 3

with open('api_config') as fp:
    config = json.load(fp)

print("api config: ",config)
url = 'http://{}:{}/uniledger/v1/transaction/createByPayload'.format(config['ip'],config['port'])

res = requests.post(url, json={"payload":"test for payload"})
print("api response:",res.json())


tx_id = json.loads(res.text)["data"]["id"]
print("tx_id: ",tx_id)

headers = {'content-type': 'application/json'}
url = 'http://{}:{}/uniledger/v1/transaction/queryByID/'.format(config['ip'],config['port'])
data = {
    "type": "3",
    "tx_id": tx_id
}
data = json.dumps(data)


sleep(delay)
res = requests.post(url, data=data, headers=headers)

print("query response: ",res.json())
