from time import sleep

from crypto import generate_keypair
from bigchaindb.common.transaction import Transaction, Asset, Fulfillment
from bigchaindb.common.util import serialize
from bigchaindb import Bigchain
import json


def create_transfer(alicepub,alicepriv,bobpub,bobpriv,include_spent):
    ##################################################### 1.CREATE
    # Cryptographic Identities Generation
    # alice, bob = generate_keypair(), generate_keypair()

    # Digital Asset Definition (e.g. bicycle)
    asset = Asset(data={"bicycle": {"manufacturer": "bkfab", "serial_number": "abcd1234"}},data_id="334cd061-846b-4213-bd25-588e951def5f")

    # Metadata Definition
    metadata = {'planet': 'earth'}

    # create trnsaction  TODO : owners_before might be node_pubkey in v0.8.0
    tx = Transaction.create([alicepub], [([alicepub], 100)], metadata=metadata, asset=asset)

    # sign with alice's private key
    tx = tx.sign([alicepriv])
    tx_id = tx.to_dict()['id']

    # write to backlog
    b = Bigchain()
    b.write_transaction(tx)

    # wait 2 sec
    sleep(5)

    # get tx by id
    tx = b.get_transaction(tx_id)

    print("create asset tx1_id:" + tx.to_dict()['id'])

    ##################################################### 2.Freeze
    #  inputs and asset
    cid = 0
    condition = tx.to_dict()['transaction']['conditions'][cid]
    inputs = Fulfillment.from_dict({
        'fulfillment': condition['condition']['details'],
        'input': {
            'cid': cid,
            'txid': tx.to_dict()['id'],
        },
        'owners_before': condition['owners_after'],
    })
    asset = Asset.from_dict(tx.to_dict()['transaction']['asset'])

    # transfer
    tx = Transaction.freeze_asset([inputs], [([alicepub],90,True),([alicepub],10,False)], asset)

    # sign with alice's private key
    tx = tx.sign([alicepriv])
    tx_id = tx.to_dict()['id']

    # write to backlog
    b = Bigchain()
    b.write_transaction(tx)

    # wait 2 sec
    sleep(5)

    # get tx by id
    tx = b.get_transaction(tx_id)

    print("freeze asset tx2_id:" + tx.to_dict()['id'])

    ##################################################### 3.UTXO
    #  inputs and asset
    utxo = b.get_outputs_filtered_not_include_freeze(alicepub, include_spent)
    for u in utxo:
        # print(u)
        u.pop('details')
    print('unspent asset:')
    print(json.dumps(utxo,indent=4))
    # print(json.load(utxo))


if __name__ == '__main__':
    alice, bob = generate_keypair(), generate_keypair()

    alicepublic_key = alice.public_key
    aliceprivate_key = alice.private_key

    bobpublic_key = bob.public_key
    bobprivate_key = bob.private_key

    include_spent = False
    print("the owner's public key  : ", alicepublic_key)
    print("the owner's private key : ", aliceprivate_key)
    create_transfer(alicepublic_key,aliceprivate_key,bobpublic_key,bobprivate_key,include_spent)

