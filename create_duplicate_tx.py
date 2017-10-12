from time import sleep
from crypto import generate_keypair
from bigchaindb.common.transaction import Transaction, Asset, Fulfillment
from bigchaindb.common.util import serialize
from bigchaindb import Bigchain

delay = 5


def create_duplicate_tx():
    ##################################################### 1.CREATE
    # Cryptographic Identities Generation
    alice, bob = generate_keypair(), generate_keypair()

    # Digital Asset Definition (e.g. bicycle)
    asset = Asset(data={"bicycle": {"manufacturer": "bkfab", "serial_number": "abcd1234"}})

    # Metadata Definition
    metadata = {'planet': 'earth1'}

    # create trnsaction  TODO : owners_before might be node_pubkey in v0.8.0
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

    # wait 2 sec
    sleep(delay)

    # get tx by id
    tx = b.get_transaction(tx_id)
    print("1.tx_create query       : ", tx)
    print(" ")

    #####################################################
    print("2.write dulpicate tx: ", b.write_transaction(tx))


if __name__ == '__main__':
    create_duplicate_tx()

