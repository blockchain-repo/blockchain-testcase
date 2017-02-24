# unichain-testcase

####1.[`create_double_tx.py`](./create_double_tx.py)

交易双花
```
~/unichain-testcase$ python3 create_double_tx.py

1.tx_create asset id    :  alice-----bicycle( ca7bb1e4-37ca-483a-8abd-88255ccd7333 )----->alice
1.tx_create tx id       :  e01f9463aa4a47d085a46330e3e42f023e9ea0242cd32845c86eec88053200c4
1.tx_create db response :  {'replaced': 0, 'unchanged': 0, 'skipped': 0, 'inserted': 1, 'deleted': 0, 'errors': 0}
1.tx_create query       :  {"id":"e01f9463aa4a47d085a46330e3e42f023e9ea0242cd32845c86eec88053200c4","transaction":{"asset":{"data":{"bicycle":{"manufacturer":"bkfab","serial_number":"abcd1234"}},"divisible":false,"id":"ca7bb1e4-37ca-483a-8abd-88255ccd7333","refillable":false,"updatable":false},"conditions":[{"amount":1,"cid":0,"condition":{"details":{"bitmask":32,"public_key":"9wbrHZHFbCzwvnfwNqr1N4ryP2Fan6G6htep39S6FW2J","signature":null,"type":"fulfillment","type_id":4},"uri":"cc:4:20:hNpDiuMYYlfIGI3BVyFM3xokVCpgPt_D4TtPVeYG3X8:96"},"owners_after":["9wbrHZHFbCzwvnfwNqr1N4ryP2Fan6G6htep39S6FW2J"]}],"fulfillments":[{"fid":0,"fulfillment":null,"input":null,"owners_before":["9wbrHZHFbCzwvnfwNqr1N4ryP2Fan6G6htep39S6FW2J"]}],"metadata":{"data":{"planet":"earth"},"id":"717a7671-8ae7-4d7d-b26a-fe21b5cf60fe"},"operation":"CREATE","timestamp":"1487919712065"},"version":1}

2.tx_transfer asset id    :  alice-----bicycle( ca7bb1e4-37ca-483a-8abd-88255ccd7333 )----->bob
2.tx_transfer tx id       :  a4f66217c882d79dcbefdf8f8197604dac6187b3dc330ad73675dfc1ba8cf4bb
2.tx_transfer db response :  {'replaced': 0, 'unchanged': 0, 'skipped': 0, 'inserted': 1, 'deleted': 0, 'errors': 0}
2.tx_transfer query       :  {"id":"a4f66217c882d79dcbefdf8f8197604dac6187b3dc330ad73675dfc1ba8cf4bb","transaction":{"asset":{"id":"ca7bb1e4-37ca-483a-8abd-88255ccd7333"},"conditions":[{"amount":1,"cid":0,"condition":{"details":{"bitmask":32,"public_key":"2CvTYrxf4GektkTHn1HhDMEwQyxwLdn4graAyVroWpLQ","signature":null,"type":"fulfillment","type_id":4},"uri":"cc:4:20:EemFTCx2cLiwzy0C_1y2yyPlrxtwTSyUKmO2kDP2Swk:96"},"owners_after":["2CvTYrxf4GektkTHn1HhDMEwQyxwLdn4graAyVroWpLQ"]}],"fulfillments":[{"fid":0,"fulfillment":null,"input":{"cid":0,"txid":"e01f9463aa4a47d085a46330e3e42f023e9ea0242cd32845c86eec88053200c4"},"owners_before":["9wbrHZHFbCzwvnfwNqr1N4ryP2Fan6G6htep39S6FW2J"]}],"metadata":null,"operation":"TRANSFER","timestamp":"1487919714150"},"version":1}

3.tx_double asset id    :  alice-----bicycle( ca7bb1e4-37ca-483a-8abd-88255ccd7333 )----->bob
3.tx_double tx id       :  372ff78ce4ba1b979a97940e37e2dd4bfa0a630b95770dc3a78d6f5604bdf456
3.tx_double db response :  {'replaced': 0, 'unchanged': 0, 'skipped': 0, 'inserted': 1, 'deleted': 0, 'errors': 0}
3.tx_double query       :  None
```

####2.[`create_fake_tx.py`](./create_fake_tx.py.py)

伪造交易
```
~/unichain-testcase$ python3 create_fake_tx.py

1.tx_create asset id    :  alice-----bicycle( 91f3c011-8ed4-4eb6-acf3-555d8b30307f )----->alice
1.tx_create tx id       :  c8fe042f3d6c15262ef29cd47c5d6481b5975b66687f69643a610be09673eae4
1.tx_create db response :  {'skipped': 0, 'unchanged': 0, 'inserted': 1, 'errors': 0, 'deleted': 0, 'replaced': 0}
1.tx_create query       :  {"id":"c8fe042f3d6c15262ef29cd47c5d6481b5975b66687f69643a610be09673eae4","transaction":{"asset":{"data":{"bicycle":{"manufacturer":"bkfab","serial_number":"abcd1234"}},"divisible":false,"id":"91f3c011-8ed4-4eb6-acf3-555d8b30307f","refillable":false,"updatable":false},"conditions":[{"amount":1,"cid":0,"condition":{"details":{"bitmask":32,"public_key":"BQZ8MtexcxQQ8vsiLePvUv6GhX75cwfeYfpDF7LCAQhe","signature":null,"type":"fulfillment","type_id":4},"uri":"cc:4:20:mp2Nyqgy7mW3zrLjr2wNSM2gF2cKRSca27yoB9wU1-k:96"},"owners_after":["BQZ8MtexcxQQ8vsiLePvUv6GhX75cwfeYfpDF7LCAQhe"]}],"fulfillments":[{"fid":0,"fulfillment":null,"input":null,"owners_before":["BQZ8MtexcxQQ8vsiLePvUv6GhX75cwfeYfpDF7LCAQhe"]}],"metadata":{"data":{"planet":"earth"},"id":"7f1c4fcb-5496-47cc-bcfa-498b810da9ff"},"operation":"CREATE","timestamp":"1487919882665"},"version":1}

2.tx_fake asset id    :  bob-----bicycle( 91f3c011-8ed4-4eb6-acf3-555d8b30307f )----->bob
2.tx_fake tx id       :  7a9a1cecce0d49561b977cf4c13c5b8d2c5b4901cd2f55b14f9b4cb34de055a4
2.tx_fake db response :  {'skipped': 0, 'unchanged': 0, 'inserted': 1, 'errors': 0, 'deleted': 0, 'replaced': 0}
2.tx_fake query       :  None
```

####3.[`tamper_block.py`](./tamper_block.py)

篡改区块
```
~/unichain-testcase$ python3 tamper_block.py

tx_id                       :  41bd28be2900e39d3a472883763af60bf8d9b6974608a5245cef1a64a4893f62
block timestamp right now   :  1487919998985
tamper block.timestamp to 1 :
block timestamp right now   :  1
tamper_block_id             :  b30d1672b57cc1df7781162e8f276059d8a81d24346d36b6e844238ddb14597c
db response                 :  {'replaced': 0, 'errors': 0, 'skipped': 0, 'inserted': 1, 'unchanged': 0, 'deleted': 0}
tamper_block status         :  invalid
blocks_status_containing_tx :  {'a5b066026a3d74f0481de67e42df34e96f4541389100fcfc5af444c2eb242986': 'valid', 'b30d1672b57cc1df7781162e8f276059d8a81d24346d36b6e844238ddb14597c': 'invalid'}
```

####4.[`BFT.py`](./BFT.py)

拜占庭容错（伪造投票）
```
~/unichain-testcase$ sudo killall unichain
~/unichain-testcase$ python3 BFT.py

tx_id                       :  1c07f5ce53a5b8eb421d0a57f132ffd703bc15dab57a8151c8cc8e0bbdb9d320
valid block       timestamp :  1487920179532
tamper block.timestamp to 1 :
invalid block     timestamp :  1
tamper_block_id             :  8642e936dda6d12b4d8ef33e59bfa7d849204c06c406b8134a5e5f1812070cf3
db response of block        :  {'skipped': 0, 'inserted': 1, 'unchanged': 0, 'replaced': 0, 'deleted': 0, 'errors': 0}
crate vote 'True'           :  {'signature': b'4dg1Z4EDYKd2ukY7WUTpSWxxuFyptxK6JN1ruywi9EUrQ7JY2GbUhHcsqL3knBUJjNXj9XoeWb5d4Ng8QW8HUsp7', 'vote': {'invalid_reason': None, 'timestamp': '1487920181596', 'previous_block': 'cf3c20d0be478f088eb7a7bcd32993aea952fe40a02d70cefd8b45442461c881', 'is_block_valid': True, 'voting_for_block': '8642e936dda6d12b4d8ef33e59bfa7d849204c06c406b8134a5e5f1812070cf3'}, 'node_pubkey': 'CLGX2DmFKUCYzBExDgoUbXqotuVjg2uGDSKnirew7Tad'}
db response of vote         :  {'skipped': 0, 'inserted': 1, 'unchanged': 0, 'replaced': 0, 'deleted': 0, 'generated_keys': ['67820ae2-6675-441c-88b4-9dacb7064a36'], 'errors': 0}
tamper_block status         :  valid
blocks_status_containing_tx :  {'8642e936dda6d12b4d8ef33e59bfa7d849204c06c406b8134a5e5f1812070cf3': 'valid'}
wait for 15 sec             :
blocks_status_containing_tx :  {'8642e936dda6d12b4d8ef33e59bfa7d849204c06c406b8134a5e5f1812070cf3': 'valid'}
```