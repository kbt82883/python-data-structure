import queue


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def preOrder(self, root):  # 전위 순회
        if root != None:
            print("[%c] " % root.data, end="")
            self.preOrder(root.left)
            self.preOrder(root.right)

    def inOrder(self, root):  # 중위 순회
        if root != None:
            self.inOrder(root.left)
            print("[%c] " % root.data, end="")
            self.inOrder(root.right)

    def postOrder(self, root):  # 후위 순회
        if root != None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print("[%c] " % root.data, end="")

    def levelOrder(self, root):  # 레벨 순회
        Q = queue.Queue()
        Q.put(root)

        while not Q.empty():
            root = Q.get()
            print("[%c] " % root.data, end="")

            if root.left != None:
                Q.put(root.left)

            if root.right != None:
                Q.put(root.right)
        print()

    def nodeCount(self, root):  # 전체 노드 개수
        if root == None:
            return 0
        else:
            return 1 + self.nodeCount(root.left) + self.nodeCount(root.right)

    def isExternal(self, root):  # 단말 노드인지
        return root.left == None and root.right == None

    def leafCount(self, root):  # 단말 노드 개수
        if root == None:
            return 0
        else:
            if self.isExternal(root):
                return 1
            else:
                return self.leafCount(root.left) + self.leafCount(root.right)

    def getHeight(self, root):  # 노드의 높이
        if root == None:
            return 0
        else:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def treeReverse(self, root):
        if root != None:
            root.left, root.right = root.right, root.left

            self.treeReverse(root.left)
            self.treeReverse(root.right)


if __name__ == "__main__":
    T = BinaryTree()
    N6 = Node("F")
    N5 = Node("E")
    N4 = Node("D")
    N3 = Node("C", N6, None)
    N2 = Node("B", N4, N5)
    N1 = Node("A", N2, N3)

    print("Pre  : ", end="")
    T.preOrder(N1)
    print()
    print("In   : ", end="")
    T.inOrder(N1)
    print()
    print("Post : ", end="")
    T.postOrder(N1)
    print()
    print("Level : ", end="")
    T.levelOrder(N1)
    print()

    print("Node Count : %d" % T.nodeCount(N1))
    print("Leaf Count : %d" % T.leafCount(N1))
    print("Tree Height: %d" % T.getHeight(N1))

    T.treeReverse(N1)

    print("Pre  : ", end="")
    T.preOrder(N1)
    print()
    print("In   : ", end="")
    T.inOrder(N1)
    print()
    print("Post : ", end="")
    T.postOrder(N1)
    print()
    print("Level : ", end="")
    T.levelOrder(N1)
    print()

    print("Node Count : %d" % T.nodeCount(N1))
    print("Leaf Count : %d" % T.leafCount(N1))
    print("Tree Height: %d" % T.getHeight(N1))
