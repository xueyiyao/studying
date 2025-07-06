import time, random
from avl import *

class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        def _insert(node, val):
            if not node:
                return BSTNode(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node
        self.root = _insert(self.root, val)

    def search(self, val):
        node = self.root
        while node:
            if node.val == val:
                return True
            node = node.left if val < node.val else node.right
        return False

def benchmark_insert(tree_class, data):
    tree = tree_class()
    start = time.perf_counter()
    for value in data:
        tree.insert(value)
    end = time.perf_counter()
    return end - start, tree

def benchmark_search(tree, data):
    start = time.perf_counter()
    for value in data:
        tree.search(value)
    end = time.perf_counter()
    return end - start

def main():
    N = 500
    KEY_LOWER_BOUND = -100000
    KEY_UPPER_BOUND = 100000
    random_data = random.sample(range(KEY_LOWER_BOUND, KEY_UPPER_BOUND), N)
    sorted_data = list(range(KEY_LOWER_BOUND, KEY_LOWER_BOUND + N + 1))

    M = 1000000
    search_data = random.sample(range(-M, M), M)
    
    print(f"=== Random Data (N = {N}, M = {M}) ===")
    res, bst = benchmark_insert(BST, random_data)
    print("BST Insert:", res)
    res, avl = benchmark_insert(AVL, random_data)
    print("AVL Insert:", res)
    print("BST Search:", benchmark_search(bst, search_data))
    print("AVL Search:", benchmark_search(avl, search_data))

    print(f"\n=== Sorted Data (N = {N}, M = {M}) ===")
    res, bst = benchmark_insert(BST, sorted_data)
    print("BST Insert:", res)
    res, avl = benchmark_insert(AVL, sorted_data)
    print("AVL Insert:", res)
    print("BST Search:", benchmark_search(bst, search_data))
    print("AVL Search:", benchmark_search(avl, search_data))

if __name__ == "__main__":
    main()