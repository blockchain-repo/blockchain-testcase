from time import sleep
import json
import requests

delay = 3
key_tx = '3viQSvdWJc5AwAu8adKiMajfPDKPv2s7b55LcpVudKLn'
key_query = 's9Z3jMPYX9tM1fxRpya9GVHMhg8ywMfoCfnxmgKD7JV'

with open('api_config') as fp:
    config = json.load(fp)
print("api config: ",config)

print("API:createByPayload")
url = 'http://{}:{}/uniledger/v1/transaction/createByPayload'.format(config['ip'],config['port'])

res = requests.post(url, json={"payload":"test for payload"})
print("api response without key:",res.json())

res = requests.post(url, json={"payload":"test for payload","key":key_tx})
print("api response with key:",res.json())

url = 'http://{}:{}/uniledger/v1/block/queryBlockCount'.format(config['ip'],config['port'])
print("API:queryBlockCount")

res = requests.post(url)
print("api response without key:",res.json())

res = requests.post(url, json={'key':key_query})
print("api response with key:",res.json())
