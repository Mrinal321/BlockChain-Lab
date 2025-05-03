import hashlib

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        hash_string = str(self.data) + str(self.previous_hash)
        return hashlib.sha256(hash_string.encode()).hexdigest()
    
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block("Genesis Block", "0")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

blockchain = Blockchain()
print("Mining block 1......")
blockchain.add_block(Block("Block 1", ""))
print("Mining block 2......")
blockchain.add_block(Block("Block 2", ""))

for block in blockchain.chain:
    print("Block Data: ", block.data)
    print("Block Hash: ", block.hash)