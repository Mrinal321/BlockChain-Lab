import hashlib
import json
from time import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previpus_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) : 
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, time(), "Genesis Block", "0")
    
    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(previous_block.index + 1, time(), data, previous_block.hash)
        self.chain.append(new_block)
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.hash != previous_block.hash:
                return True

blockchain = Blockchain()

blockchain.add_block("Transaction 1")
blockchain.add_block("Transection 2")
blockchain.add_block("Transection 3")

print("Blockchain is valid: ", blockchain.is_chain_valid())

# attempt to tamper with the second block 
blockchain.chain[1].data = "Tampered Transaction"
print("Blockchain is valid: ", blockchain.is_chain_valid())