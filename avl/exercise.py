class Node:
    def __init__(self, key: tuple):
        self.key: tuple = key
        self.left: Node = None
        self.right: Node = None
        self.height = 1

class TupleAVL:
    def __init__(self):
        self.root: Node = None

    def has_conflict(self, existing: tuple, candidate: tuple):
        if candidate[0] <= existing[0] < candidate[1]:
            return True
        if existing[0] <= candidate[0] < existing[1]:
            return True
        return False
    
    def get_height(self, root: Node) -> int:
        return 0 if not root else root.height
    
    def get_balance_factor(self, root: Node) -> int:
        return 0 if not root else (self.get_height(root.left) - self.get_height(root.right))
    
    def insert(self, key: tuple) -> bool:
        self.root, inserted = self.insert_helper(self.root, key)
        return inserted

    def insert_helper(self, root: Node, key: tuple) -> tuple[Node, bool]:
        inserted = False
        if not root:
            return Node(key), True
        elif self.has_conflict(root.key, key):
            return root, False
        elif key < root.key:
            root.left, inserted = self.insert_helper(root.left, key)
        else:
            root.right, inserted = self.insert_helper(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        bf = self.get_balance_factor(root)
        if bf > 1 and key < root.left.key:
            return self.right_rotate(root), inserted
        if bf < -1 and key > root.right.key:
            return self.left_rotate(root), inserted
        if bf > 1 and key > root.right.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root), inserted
        if bf < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root), inserted

        return root, inserted
    
    def left_rotate(self, root: Node) -> Node:
        A = root
        B = A.right
        X = A.left
        Y = B.left
        Z = B.right

        B.left = A
        A.right = Y

        A.height = 1 + max(self.get_height(X), self.get_height(Y))
        B.height = 1 + max(self.get_height(A), self.get_height(Z))

        return B
    
    def right_rotate(self, root: Node) -> Node:
        B = root
        A = B.left
        X = A.left
        Y = A.right
        Z = B.right

        A.right = B
        B.left = Y

        B.height = 1 + max(self.get_height(Y), self.get_height(Z))
        A.height = 1 + max(self.get_height(X), self.get_height(B))

        return A


class MeetingScheduler():
    def __init__(self, rooms: list[str]):
        self.rooms: dict[str, TupleAVL] = {}
        for roomId in rooms:
            self.rooms[roomId] = TupleAVL()

    def schedule(self, startTime: int, endTime: int) -> str:
        key = (startTime, endTime)
        for roomId, tree in self.rooms.items():
            inserted = tree.insert(key)
            if inserted:
                return roomId
        return "Could not find room!"
    
def main():
    scheduler = MeetingScheduler(["nyc", "london", "tokyo"])
    print(scheduler.schedule(10,20)) #nyc
    print(scheduler.schedule(10,20)) #london
    print(scheduler.schedule(10,20)) #tokyo
    print(scheduler.schedule(10,15)) #err
    print(scheduler.schedule(15,30)) #err
    print(scheduler.schedule(35,40)) #nyc
    print(scheduler.schedule(20,30)) #nyc
    print(scheduler.schedule(25,35)) #london
    
if __name__ == "__main__":
    main()
        