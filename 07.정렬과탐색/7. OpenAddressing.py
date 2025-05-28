M = 13  # 버킷의 수


class HashTable:
    def __init__(self):
        self.table = [0] * M

    def hashFn(self, key):  # 해시함수
        return key % M

    def hashFn2(self, key):  # 이중 해시법
        return 11 - (key % 11)  # M보다 작은 수 중에 제일 큰 소수

    def insert(self, key):
        hashVal = self.hashFn(key)

        for i in range(M):
            # 선형 조사
            # bucket = (hashVal + i) % M  # 해시테이블에서의 인덱스 번호

            # 이차 조사법
            # bucket = (hashVal + i ** 2) % M  # 군집화 완화법

            # 이중 해싱법
            bucket = (hashVal + i * self.hashFn2(key)) % M

            if self.table[bucket] == 0:  # 비어있으면
                self.table[bucket] = key
                break

    def search(self, key):
        hashVal = self.hashFn(key)

        for i in range(M):
            # 선형 조사
            # bucket = (hashVal + i) % M  # 해시테이블에서의 인덱스 번호

            # 이차 조사법
            # bucket = (hashVal + i ** 2) % M  # 군집화 완화법

            # 이중 해싱법
            bucket = (hashVal + i * self.hashFn2(key)) % M

            if self.table[bucket] == 0:  # 비어있으면
                return -1
            elif self.table[bucket] == key:
                return bucket

    def delete(self, key):
        hashVal = self.hashFn(key)

        for i in range(M):
            # 선형 조사
            # bucket = (hashVal + i) % M  # 해시테이블에서의 인덱스 번호

            # 이차 조사법
            # bucket = (hashVal + i ** 2) % M  # 군집화 완화법

            # 이중 해싱법
            bucket = (hashVal + i * self.hashFn2(key)) % M

            if self.table[bucket] == 0:  # 비어있으면
                print("No key to delete")
                return
            elif self.table[bucket] == key:
                print("Deleted [%d] at bucket[%d]." % (key, bucket))
                self.table[bucket] = -1
                return

    def display(self):
        print("\nBucket  key")
        print("===========")

        for i in range(M):
            print("HT[%2d] : %2d" % (i, self.table[i]))


if __name__ == "__main__":
    HT = HashTable()

    data = [45, 27, 88, 9, 71, 60, 46, 38, 24]

    for d in data:
        print("h(%2d) = %2d" % (d, HT.hashFn(d)), end=" ")
        HT.insert(d)
        print(HT.table)

    HT.display()
    print()

    print("Search(46) ---> ", HT.search(46))
    HT.delete(9)
    HT.display()
    print()
    print("Search(46) ---> ", HT.search(46))
