M = 13


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class HashTable:
    def __init__(self):
        self.table = [None] * M

    def hashFn(self, key):  # 해시함수
        return key % M

    def insert(self, key):
        bucket = self.hashFn(key)

        node = Node(key)  # 노드 만들고
        node.next = self.table[
            bucket
        ]  # 노드의 next가 버킷 헤드가 가르키고 있던 노드를 가르킴
        self.table[bucket] = node  # 버킷 헤드가 노드를 가르킴

    def display(self):
        for i in range(M):
            print("HT[%2d] : " % (i), end="")
            n = self.table[i]

            while n is not None:
                print(n.data, end=" ")
                n = n.next
            print()


if __name__ == "__main__":
    import random

    HT = HashTable()

    for i in range(20):
        HT.insert(random.randint(10, 99))

    HT.display()
