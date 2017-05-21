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
blocks_status_containing_tx : 
 {'a5b066026a3d74f0481de67e42df34e96f4541389100fcfc5af444c2eb242986': 'valid',
'b30d1672b57cc1df7781162e8f276059d8a81d24346d36b6e844238ddb14597c': 'invalid'}
```

####4.[`BFT.py`](./BFT.py)

拜占庭容错（伪造投票）
```
~/unichain-testcase$ sudo killall unichain
~/unichain-testcase$ python3 BFT.py 
 
tx_id                       :  aa648edd0c2dfeca734bf078da3ccea75901a22501cbfd0852beac214f6bdf41
valid block       timestamp :  1488164106038
tamper block.timestamp to 1 : 
invalid block     timestamp :  1
tamper_block_id             :  70b299415bc245b75fa34d3dcf0a7ec5acf77e72b5dac1bcbd9274b2686634df
db response of block        :  {'deleted': 0, 'replaced': 0, 'inserted': 1, 'skipped': 0, 'errors': 0, 'unchanged': 0}
crate vote 'True'           :  {'signature': b'rzzfuphD6ma4syVgnbWdMGo1qkoD4BuDw3tydzCC2F4fqsPDCGjpXSz6dAgRqxURZiuN8gsobJn3QUGtxFfoyaQ', 'vote': {'previous_block': 'ad5df5d07b7d282852db0e19d8f3e31b2c9a2e0920419e911f66e2f6ba67e124', 'timestamp': '1488164108069', 'is_block_valid': True, 'voting_for_block': '70b299415bc245b75fa34d3dcf0a7ec5acf77e72b5dac1bcbd9274b2686634df', 'invalid_reason': None}, 'node_pubkey': 'ETbj6aHqTCqnHSw4SUDhy8M98RjnNp79DowMyKfPiUb3'}
db response of vote         :  {'deleted': 0, 'errors': 0, 'replaced': 0, 'inserted': 1, 'skipped': 0, 'generated_keys': ['215d463c-9678-4484-bb95-3f702d059763'], 'unchanged': 0}
tamper_block status         :  invalid
blocks_status_containing_tx :  {'70b299415bc245b75fa34d3dcf0a7ec5acf77e72b5dac1bcbd9274b2686634df': 'invalid'}
wait for 15 sec             : 
blocks_status_containing_tx :  {'c5e1e61cb4523062f0b18891db224e7a08d7d9bd7f0b52a7605d3a15864db29f': 'valid', '70b299415bc245b75fa34d3dcf0a7ec5acf77e72b5dac1bcbd9274b2686634df': 'invalid'}
```