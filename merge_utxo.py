"""A simple way to generate a `TRANSFER` transaction to merge utxo.

"""
from time import sleep

import sys

from crypto import generate_keypair
from bigchaindb.common.transaction import Transaction, Asset, Fulfillment
from bigchaindb.common.util import serialize
from bigchaindb import Bigchain
import json


def merge_utxo(alicepub,alicepriv,include_spent):
    asset = Asset(data={"bicycle": {"manufacturer": "bkfab", "serial_number": "abcd1234"}}, data_id="334cd061-846b-4213-bd25-588e951def5f")
    metadata = {'planet': 'earth'}
    b = Bigchain()
    utxo = b.get_outputs_filtered_not_include_freeze(alicepub, include_spent)
    for u in utxo:
        # print(u)
        u.pop('details')
    print('userA unspent asset:')
    print(json.dumps(utxo, indent=4))
    inputs = []
    balance = 0
    for i in utxo:
        f = Fulfillment.from_dict({
            'fulfillment': i['details'],
            'input': {
                'cid': i['cid'],
                'txid': i['txid'],
            },
            'owners_before': [alicepriv],
        })
        inputs.append(f)
        balance += i['amount']

    length = len(utxo)
    if balance <= 0:
        return 'No need to merge, because of lack of balance'
    elif length <= 1:
        return 'No need to merge, because utxo len = 1'
    else:
        tx = Transaction.transfer(inputs, [([alicepub], balance)], metadata=metadata, asset=asset)
        tx = tx.sign([alicepriv])
        tx_id = tx.to_dict()['id']
        # write to backlog
        b.write_transaction(tx)
        # wait 2 sec
        print("========userA merge multi-asset========")
        print("========wait for block and vote...========")
        sleep(5)
        # get tx by id
        tx = b.get_transaction(tx_id)
        print("merge txid:" + tx.to_dict()['id'])

    utxo = b.get_outputs_filtered_not_include_freeze(alicepub, include_spent)
    for u in utxo:
        # print(u)
        u.pop('details')
    print('userA unspent asset:')
    print(json.dumps(utxo, indent=4))

if __name__ == '__main__':

    if not len(sys.argv)==3:
        print("Please provide the woner's keypairs! public_key private_key")
        sys.exit()

    public_key = sys.argv[1]
    private_key = sys.argv[2]
    include_spent = False

    # public_key= '6e2SwRRVQuGie5jC4uiS9HftrtjxR42k9K95NA1rHnSB'
    # private_key = '4dsXPQgmQ64vcZFd6N24kAakiMDaFjuMdiTAMyw9SpYi'

    merge_utxo(public_key,private_key,include_spent)

