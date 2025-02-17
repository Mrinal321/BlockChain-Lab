def string_to_ascii_binary(input_string):
    binary_representation = [format(ord(char), '08b') for char in input_string]
    return ''.join(binary_representation) 

text = "Bangladesh"
binary_pattern = string_to_ascii_binary(text)

binary_pattern += '1'
i = 1
j = 512 - 64 - len(binary_pattern)
while i < j:
    binary_pattern += '0'
    i += 1

last_64 = bin(len(text))[2:]
last_64 = last_64[::-1]
while len(last_64) < 64:
    last_64 += '0'
last_64 = last_64[::-1]
binary_pattern += last_64
block_size = 32
array_size = 512
blocks = []

# Divide into 16 blocks
for i in range(0, array_size, block_size):
    blocks.append(binary_pattern[i:i + block_size])

# Print each block
for idx, block in enumerate(blocks):
    print(f"Block {idx + 1}: {block}")