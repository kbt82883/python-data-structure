# O(log n)


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def getHeight(root):
    if root == None:
        return 0

    return 1 + max(getHeight(root.left), getHeight(root.right))


def getBalance(root):
    if root == None:
        return 0

    return getHeight(root.left) - getHeight(root.right)


def rotateLeft(p):
    c = p.right
    p.right = c.left
    c.left = p

    return c


def rotateRight(p):
    c = p.left
    p.left = c.right
    c.right = p

    return c


def insert(root, key):
    if root == None:
        return TreeNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        pass

    balance = getBalance(root)

    if balance > 1 and key < root.left.key:
        print("--- LL Type ---")
        return rotateRight(root)  # LL로 깨지면 오른쪽으로 돌리기

    if balance > 1 and key > root.left.key:
        print("--- LR Type ---")
        root.left = rotateLeft(root.left)
        return rotateRight(root)

    if balance < -1 and key > root.right.key:
        print("--- RR Type ---")
        return rotateLeft(root)  # RR로 깨지면 왼쪽으로 돌리기

    if balance < -1 and key < root.right.key:
        print("--- RL Type ---")
        root.right = rotateRight(root.right)
        return rotateLeft(root)

    return root


def preOrder(root):
    if root != None:
        print("%2d" % root.key, end="")
        preOrder(root.left)
        preOrder(root.right)


def display(root, msg):
    print(msg, end="")
    preOrder(root)
    print()


if __name__ == "__main__":
    root = None
    data = [7, 8, 9, 2, 1, 5, 3, 6, 4]

    for i in range(9):
        root = insert(root, data[i])
        display(root, "[Insert %2d] : " % data[i])
    print()
