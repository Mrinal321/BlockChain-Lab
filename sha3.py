import hashlib 

message = b"Hello,!" 
 
# Create a SHA-3 hash object with a 256-bit output size 
sha3_256 = hashlib.sha3_256() 

# Update the hash object with the message 
sha3_256.update(message) 
digest = sha3_256.digest() 
hexdigest = digest.hex() 
print(hexdigest)