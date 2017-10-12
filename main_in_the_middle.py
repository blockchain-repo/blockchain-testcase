from time import sleep
from crypto import generate_keypair

from bigchaindb.common.transaction import Transaction, Asset, Fulfillment
from bigchaindb.common.util import serialize
from bigchaindb import Bigchain

delay = 4


def create_transfer():
    ##################################################### 1.CREATE
    # Cryptographic Identities Generation
    alice, bob, tom = generate_keypair(), generate_keypair(), generate_keypair()
    asset = Asset(data={"bicycle": {"manufacturer": "bkfab", "serial_number": "abcd1234"}})
    metadata = {'planet': 'earth'}

    tx = Transaction.create([alice.public_key], [([alice.public_key], 1)], metadata=metadata, asset=asset)
    print(" ")
    print("1.tx_create asset id    :  alice-----bicycle(", tx.to_dict()['transaction']['asset']['id'], ")----->alice")
    print("1.tx_create tx id       : ", tx.to_dict()['id'])

    # sign with alice's private key
    tx = tx.sign([alice.private_key])
    tx_id = tx.to_dict()['id']

    # write to backlog
    b = Bigchain()
    print("1.tx_create db response : ", b.write_transaction(tx))

    # wait 4 sec
    sleep(delay)

    # get tx by id
    tx = b.get_transaction(tx_id)
    print("1.tx_create query       : ", tx)
    # print("tx1_id:"+tx.to_dict()['id'])
    print(" ")
    ##################################################### 2.TRANSFER
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
    tx = Transaction.transfer([inputs], [([bob.public_key], 1)], asset)
    print("2.tx_transfer asset id    :  alice-----bicycle(", tx.to_dict()['transaction']['asset']['id'], ")----->bob")
    print("2.tx_transfer tx id       : ", tx.to_dict()['id'])
    print("2.tx_transfer tx          : ", tx.to_dict())
    print(" ")
    # sign with alice's private key
    tx = tx.sign([alice.private_key])

    # man in the middle attack, then write to backlog
    tx.conditions[0].owners_after = [tom.public_key]
    print("3.tx_attack asset id    :  alice-----bicycle(", tx.to_dict()['transaction']['asset']['id'], ")----->tom")
    print("3.tx_attack tx id       : ", tx.to_dict()['id'])
    print("3.tx_attack tx          : ", tx.to_dict())
    tx_id = tx.to_dict()['id']
    b = Bigchain()
    print("3.tx_attack db response : ", b.write_transaction(tx))

    # wait 4 sec
    sleep(delay)

    # get tx by id
    tx = b.get_transaction(tx_id)
    print("3.tx_attack query       : ", tx)
    print(" ")


if __name__ == '__main__':
    create_transfer()
