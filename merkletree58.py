import hashlib

class MerkleTree:
    def __init__(self, data_list):
        """
        Initialize the Merkle Tree with a list of data.
        """
        self.leaves = [self.hash_data(data) for data in data_list]
        self.tree = self.build_tree(self.leaves)

    @staticmethod
    def hash_data(data):
        """
        Hash a piece of data using SHA-256.
        """
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def build_tree(self, leaves):
        """
        Build the Merkle Tree and return the root hash.
        """
        tree = [leaves]
        while len(tree[-1]) > 1:
            current_level = tree[-1]
            next_level = []
            for i in range(0, len(current_level), 2):
                # Pair adjacent nodes and hash them together
                left = current_level[i]
                right = current_level[i + 1] if i + 1 < len(current_level) else left
                combined_hash = self.hash_data(left + right)
                next_level.append(combined_hash)
            tree.append(next_level)
        for tr in tree:
            for t in tr:
                print(f"{t}  ", end="")
            print("", end="\n")
        
        return tree

    def get_root(self):
        """
        Get the Merkle root (top of the tree).
        """
        return self.tree[-1][0] if self.tree else None

    def get_proof(self, index):
        """
        Get the proof for a given leaf index.
        """
        proof = []
        for level in self.tree[:-1]:
            sibling_index = index ^ 1  # XOR to find sibling
            print(f"XOR: {index} ^ 1 = {sibling_index}")
            if sibling_index < len(level):
                proof.append(level[sibling_index])
            index //= 2  # Move to the next level
        return proof

    @staticmethod
    def verify_proof(index, leaf, proof, root):
        """
        Verify a Merkle proof against the root hash.
        """
        current_hash = hashlib.sha256(leaf.encode('utf-8')).hexdigest()
        for sibling in proof:
            if index % 2 == 1:
                current_hash = hashlib.sha256((current_hash + sibling).encode('utf-8')).hexdigest()
            else:
                current_hash = hashlib.sha256((sibling + current_hash).encode('utf-8')).hexdigest()

            index = index // 2 + (index % 2)
        return current_hash == root


# Example Usage
if __name__ == "__main__":
    data = ["Transaction1", "Transaction2", "Transaction3", "Transaction4", "Transaction5"]
    merkle_tree = MerkleTree(data)

    # Get Merkle root
    root = merkle_tree.get_root()
    print("Merkle Root:", root)

    # Get proof for a specific leaf
    leaf_index = 2  # Index of "Transaction3"
    proof = merkle_tree.get_proof(leaf_index)
    print("Proof for Transaction3:", proof)

    # Verify proof
    leaf = data[leaf_index] + "3"
    is_valid = MerkleTree.verify_proof(leaf_index + 1, leaf, proof, root)
    print(f"Verification result for {leaf}: {is_valid}")