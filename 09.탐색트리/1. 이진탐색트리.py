# 이진 탐색의 단점(삽입/삭제 연산의 비효율성)을 극복
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root == None:
        return TreeNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        print("중복된 키는 입력되지않음.")

    return root


def getMinNode(root):
    while root != None and root.left != None:
        root = root.left

    return root


def delete(root, key):
    # case 1: 단말노드의 삭제 or 자식이 하나(오른쪽)인 노드의 삭제
    # case 2: 자식이 하나(왼쪽)인 노드의 삭제
    # case 3: 자식이 두 개
    # 왼쪽 서브트리의 최댓값 or 오른쪽 서브트리의 최솟값을 delete한 자리로로
    if root == None:
        return None

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left == None:  # case1
            return root.right
        elif root.right == None:  # case2 ??
            return root.left
        else:  # case3 ?
            # 오른쪽 서브트리의 최솟값
            succ = getMinNode(root.right)
            root.key = succ.key
            root.right = delete(root.right, succ.key)

    return root


def preOrder(root):
    if root != None:
        print("%2d " % root.key, end="")
        preOrder(root.left)
        preOrder(root.right)


def display(root, msg):
    print(msg, end="")
    preOrder(root)
    print()


if __name__ == "__main__":
    root = None
    data = [35, 18, 7, 26, 3, 22, 30, 12, 26, 68, 99]

    for key in data:
        root = insert(root, key)
        display(root, "[Insert %2d] : " % key)
    print()

    # root = delete(root, 30)
    # display(root, '[Delete 30] : ')
    # root = delete(root, 26)
    # display(root, '[Delete 26] : ')

    root = delete(root, 35)  # 18로도 해보기?
    display(root, "[Delete 35] : ")
