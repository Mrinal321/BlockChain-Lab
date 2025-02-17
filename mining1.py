import hashlib
import time

version = 1
previous_block_hash = "00000000000000000007d28e1a9ac3b37760e3b3fbbd3df2b8f7670a434f18a6" 
merkle_root = "9d7d1c2fa42e7f520d33de8e7bb28132586d30ef7c6d9b9e446e6c12d1f7cf25"

timestamp = int(time.time())
difficulty = 4
nonce = 0

header = str(version) + previous_block_hash + merkle_root + str(timestamp) + str(difficulty) + str(nonce)

while True:
    header_with_nonce = header + str(nonce)
    hash = hashlib.sha256(header_with_nonce.encode()).hexdigest()

    if hash[:difficulty] == "0" * difficulty:
        print("Block mined successfully!")
        print("Nonce:", nonce)
        print("Hash:", hash)
        break
    
    nonce += 1