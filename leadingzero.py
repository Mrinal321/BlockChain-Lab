import hashlib

def solve_puzzle(string, leading_zeros):
    nonce = 0
    while True:
        data = string + str(nonce)
        hash_value = hashlib.sha256(data.encode()).hexdigest()
        if hash_value.startswith("0" * leading_zeros):
            return nonce, hash_value
        nonce += 1

nonce, hash_value = solve_puzzle("I am Mrinal!", 2)
print(nonce)