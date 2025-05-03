import hashlib

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        
    def calculate_hash(self):
        hash_str = str(self.data) + str(self.previous_hash)
        return hashlib.sha256(hash_str.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]


    def create_genesis_block(self):
        return Block("Genesis block", "0")
    
    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
    
blockchain = Blockchain()
blockchain.add_block(Block("Block 1", ""))

for block in blockchain.chain:
    print("Value: ", block.data)