from time import sleep

import sys

from crypto import generate_keypair
from bigchaindb.common.transaction import Transaction, Asset, Fulfillment
from bigchaindb.common.util import serialize
from bigchaindb import Bigchain
import json


def create_transfer(public_key,private_key,include_spent):
    asset = Asset(data={"bicycle": {"manufacturer": "bkfab", "serial_number": "abcd1234"}},data_id="334cd061-846b-4213-bd25-588e951def5f")

    ##################################################### 1.getfreeze
    b = Bigchain()

    utxo_freeze = b.get_freeze_outputs_only(public_key)

    # for u in utxo_freeze:
    #     # print(u)
    #     u.pop('details')
    print('userA frozen asset:')
    print(json.dumps(utxo_freeze,indent=4))
    # print(json.load(utxo))


    #
    # ##################################################### 2.Unfreeze
    inputs = []
    balance = 0
    for i in utxo_freeze:
        f = Fulfillment.from_dict({
            'fulfillment':i['details'] ,
            'input': {
                'cid': i['cid'],
                'txid': i['txid'],
             },
             'owners_before': [public_key],
        })
        inputs.append(f)
        balance += i['amount']

    # create trnsaction
    tx = Transaction.freeze_asset(inputs, [([public_key],balance,False)],asset)
    # #  inputs and asset


    # sign with alice's private key
    tx = tx.sign([private_key])
    tx_id = tx.to_dict()['id']

    # write to backlog
    b = Bigchain()
    b.write_transaction(tx)
    print("unfreeze asset for userA")
    print("========wait for block and vote...========")
    # wait 2 sec
    sleep(5)

    # get tx by id
    tx = b.get_transaction(tx_id)

    print("unfreeze asset tx1_id:" + tx.to_dict()['id'])

    ##################################################### 3.UTXO
    #  inputs and asset
    utxo = b.get_outputs_filtered_not_include_freeze(public_key, include_spent)
    for u in utxo:
        # print(u)
        u.pop('details')
    print('userA unspent asset:')
    print(json.dumps(utxo,indent=4))
    # print(json.load(utxo))


if __name__ == '__main__':

    if not len(sys.argv)==3:
        print("Please provide the woner's keypairs! public_key private_key")
        sys.exit()

    public_key = sys.argv[1]
    private_key = sys.argv[2]
    include_spent = False

    # public_key= '6e2SwRRVQuGie5jC4uiS9HftrtjxR42k9K95NA1rHnSB'
    # private_key = '4dsXPQgmQ64vcZFd6N24kAakiMDaFjuMdiTAMyw9SpYi'

    create_transfer(public_key,private_key,include_spent)

