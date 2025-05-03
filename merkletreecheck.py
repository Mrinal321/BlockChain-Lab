import hashlib

# Hashing function
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Build Merkle Tree and return levels and root
def build_merkle_tree(leaves):
    current_level = [sha256(leaf) for leaf in leaves]
    tree = [current_level]
    
    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i + 1] if i + 1 < len(current_level) else left
            combined = sha256(left + right)
            next_level.append(combined)
        current_level = next_level
        tree.insert(0, current_level)
    
    root = tree[0][0]
    return tree, root

# Generate Merkle proof for an element
def generate_merkle_proof(element, leaves, tree):
    if element not in leaves:
        return None  # element not found
    
    index = leaves.index(element)
    element_hash = sha256(element)
    proof = []
    
    for level in reversed(tree[1:]):  # Exclude root level
        sibling_index = index ^ 1  # Toggle last bit to find sibling
        if sibling_index < len(level):
            sibling_hash = level[sibling_index]
            direction = 'right' if index % 2 == 0 else 'left'
            proof.append((sibling_hash, direction))
        index = index // 2
    
    return proof

# Verify the Merkle proof
def verify_proof(element, proof, root):
    current_hash = sha256(element)
    for sibling_hash, direction in proof:
        if direction == 'right':
            current_hash = sha256(current_hash + sibling_hash)
        else:
            current_hash = sha256(sibling_hash + current_hash)
    return current_hash == root

# ----------------------------
# Example Usage
data = ['tx1', 'tx2', 'tx3', 'tx4']
tree, merkle_root = build_merkle_tree(data)
print("Merkle Root:", merkle_root)

# Test a member
member = 'tx2'
proof = generate_merkle_proof(member, data, tree)
if proof and verify_proof(member, proof, merkle_root):
    print(f"'{member}' is a member of the Merkle Tree.")
else:
    print(f"'{member}' is NOT a member of the Merkle Tree.")

# Test a non-member
non_member = 'tx5'
proof = generate_merkle_proof(non_member, data, tree)
if proof and verify_proof(non_member, proof, merkle_root):
    print(f"'{non_member}' is a member of the Merkle Tree.")
else:
    print(f"'{non_member}' is NOT a member of the Merkle Tree.")
