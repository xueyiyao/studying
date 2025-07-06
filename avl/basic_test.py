from avl import *

def main():
    tree = AVL()
    for i in range(10):
        tree.root = tree.insert(tree.root, i)
        tree.print_tree()

    print(tree.search(11))
    print(tree.search(0))
    print(tree.search(4))
    print(tree.search(-1))

if __name__ == "__main__":
    main()