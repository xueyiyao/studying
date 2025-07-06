from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left: Node = None
        self.right: Node = None
        self.height = 1 # height is max distance from leaf

class AVL:
    def __init__(self):
        self.root: Node = None

    def get_height(self, node: Node) -> int:
        return 0 if not node else node.height
    
    def get_balance_factor(self, node: Node) -> int:
        return 0 if not node else (self.get_height(node.left) - self.get_height(node.right))
    
    def search(self, key) -> bool:
        return True if self.search_helper(key) else False
    
    def insert(self, key) -> None:
        self.root = self.insert_helper(self.root, key)
    
    def search_helper(self, key) -> Node:
        p = self.root
        while p and p.key != key:
            if key < p.key:
                p = p.left
            else:
                p = p.right
        return p

    def insert_helper(self, root: Node, key) -> Node:
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert_helper(root.left, key)
        else:
            root.right = self.insert_helper(root.right, key)
        
        # height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # rotate
        bf = self.get_balance_factor(root)
        if bf > 1 and key < root.left.key:
            return self.right_rotate(root)
        if bf < -1 and key > root.right.key:
            return self.left_rotate(root)
        if bf > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if bf < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    
    '''
       A            B
     X   B   ->   A   Z
        Y Z      X Y   
    '''
    def left_rotate(self, root: Node) -> Node:
        A,B = root, root.right
        X,Y,Z = A.left, B.left, B.right
        
        A.right = Y
        B.left = A

        A.height = 1 + max(self.get_height(X), self.get_height(Y))
        B.height = 1 + max(self.get_height(A), self.get_height(Z))

        return B

    '''
       A            B
     X   B   <-   A   Z
        Y Z      X Y   
    '''
    def right_rotate(self, root: Node) -> Node:
        B,A = root, root.left
        X,Y,Z = A.left, A.right, B.right

        B.left = Y
        A.right = B

        B.height = 1 + max(self.get_height(Y), self.get_height(Z))
        A.height = 1 + max(self.get_height(X), self.get_height(B))

        return A
    
    def print_tree(self):
        if not self.root:
            print('\nTree is empty!')
            return

        level_order = ''
        with_details = ''
        q = deque([self.root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(str(node.key))
                    with_details += f'{node.key}'.ljust(5) + f'h = {self.get_height(node)}, b = {self.get_balance_factor(node)}\n'
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append('n')
            level_order += ' '.join(level) + '\n'

        print('\nLevel Order Traversal:')
        print(level_order)
        print('Level Order Traversal with Height and Balance Factor:')
        print(with_details)
