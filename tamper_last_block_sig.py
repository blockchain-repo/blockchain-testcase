from uuid import uuid3
from time import sleep
from crypto import generate_keypair, hash_data
from bigchaindb.common.transaction import Transaction, Asset
from bigchaindb.common.util import serialize, gen_timestamp
from bigchaindb.common.crypto import hash_data
from bigchaindb import Bigchain
from bigchaindb.models import Block

delay = 5


def tamper_block():
    # Cryptographic Identities Generation
    alice, bob = generate_keypair(), generate_keypair()
    print(" ")
    # Digital Asset Definition (e.g. bicycle)
    asset = Asset(data={"bicycle": {"manufacturer": "bkfab", "serial_number": "abcd1234"}})

    # Metadata Definition
    metadata = {'planet': 'earth'}

    # create trnsaction  TODO : owners_before might be node_pubkey in v0.8.0
    tx = Transaction.create([alice.public_key], [([alice.public_key], 1)], metadata=metadata, asset=asset)

    # sign with private key
    tx = tx.sign([alice.private_key])
    tx_id = tx.to_dict()['id']
    print("tx_id                       : ", tx_id)

    # create block
    b = Bigchain()
    block = b.create_block([tx])
    block_id = block.to_dict()['id']
    block_voters = block.to_dict()['block']['voters']
    print("last_block_id    sig        : ", block_id, block.signature)
    print(block.to_dict())
    # tamper block sig
    block.sign(alice.private_key)
    block_dict = block.to_dict()
    print("tamper_block_id  sig        : ", block_dict['id'], block_dict['signature'])
    print(block_dict)
    print("db response                 : ", b.backend.write_block(serialize(block_dict)))
    sleep(delay)
    print("tamper_block status         : ", b.block_election_status(block_dict['id'], block_voters))
    print("blocks_status_containing_tx : ", b.get_blocks_status_containing_tx(tx_id))
    print(" ")


if __name__ == '__main__':
    tamper_block()
