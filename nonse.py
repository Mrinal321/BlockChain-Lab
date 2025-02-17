import hashlib

def solve_puzzle(string, leading_zeros) :
    nonce = 0
    while True:
        nonce_str = str(nonce)
        data = string +nonce_str
        hash_value = hashlib.sha256(data.encode()).hexdigest()
        if hash_value.startswith("0" * leading_zeros) :
            return nonce_str, hash_value
        nonce += 1

input_string = input("Enter the string: ")
input_zeros = int(input("Enter the number of leading zeros: "))

nonce_value, hash_result = solve_puzzle(input_string, input_zeros)

print("Input String:", input_string)
print("Nonce value for which the puzzle in solved:", nonce_value)
print("Generated Hash:", hash_result)