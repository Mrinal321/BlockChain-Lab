import hashlib

def build_merkle_tree(leaves):
    num_leaves = len(leaves)

    if num_leaves == 1:
        return leaves[0]
    if num_leaves %2 == 1:
        leaves.append(leaves[-1])
        num_leaves += 1

    pairs = [leaves[i] + leaves[i+1] for i in range(0, num_leaves, 2)]
    hashes = [hashlib.sha256(pair.encode()).hexdigest() for pair in pairs]

    return build_merkle_tree(hashes)

leaves = ["apple", "banana", "cherry", "date"]
merkle_root = build_merkle_tree(leaves)
print("Merkle root: ", merkle_root)

