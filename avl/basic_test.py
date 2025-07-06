from avl import *

def main():
    tree = AVL()
    for i in range(10):
        tree.root = tree.insert_helper(tree.root, i)
        tree.print_tree()

    print(tree.search_helper(11))
    print(tree.search_helper(0))
    print(tree.search_helper(4))
    print(tree.search_helper(-1))

if __name__ == "__main__":
    main()