# 이진 탐색의 단점(삽입/삭제 연산의 비효율성)을 극복
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root == None:  # 현재 위치가 비어있으면
        return TreeNode(key)

    if key < root.key:  # 현위치 노드의 key보다 작으면
        root.left = insert(root.left, key)  # root.left 위치에 삽입할 수 있도록 재귀호출
    elif key > root.key:  # 위와 정반대
        root.right = insert(root.right, key)
    else:
        print("중복된 키는 입력되지않음.")

    return (
        root  # 재귀가 끝나고 돌아올 때, root.left & root.right에 연결될 수 있도록 반환
    )


def getMinNode(root):  # 계속 왼쪽 자식 노드로 갈 수 있으면 감
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
    else:  # 현위치 노드가 입력한 key와 같으면
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            succ = getMinNode(root.right)  # 오른쪽 서브트리의 최솟값
            root.key = succ.key  # 현재 노드 값을 그 노드 값으로 바꾸고
            root.right = delete(
                root.right, succ.key
            )  # 그 최소값을 가진 노드를 오른쪽 서브트리에서 삭제함

    return root  # 삭제가 끝나면, 상위 노드에게 현재의 노드를 반환해서 그대로 연결됨


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
