import hashlib 

class Block: 
    def __init__(self, data, previous_hash): 
        self.data = data 
        self.previous_hash = previous_hash 
        self.nonce = 0 
        self.hash = self.calculate_hash()  
        
    def calculate_hash(self): 
        hash_string = str(self.data)+str(self.previous_hash)+str(self.nonce) 
        return hashlib.sha256(hash_string.encode()).hexdigest() 
     
    def mine_block(self, difficulty): 
        while self.hash[0:difficulty] != '0' * difficulty: 
            self.nonce += 1 
            self.hash = self.calculate_hash() 
 
class Blockchain: 
    def __init__(self): 
        self.chain = [self.create_genesis_block()] 
        self.difficulty = 2 

    def create_genesis_block(self): 
        return Block("Genesis Block", "0") 

    def get_last_block(self): 
        return self.chain[-1] 
    
    def add_block(self, new_block): 
        new_block.previous_hash = self.get_last_block().hash 
        new_block.mine_block(self.difficulty) 
        self.chain.append(new_block) 

blockchain = Blockchain() 
blockchain.add_block(Block("Block 1", "")) 
blockchain.add_block(Block("Block 2", "")) 
blockchain.add_block(Block("Block 3", "")) 

for block in blockchain.chain: 
    print("Block data: ", block.data) 
    print("Block hash: ", block.hash)
