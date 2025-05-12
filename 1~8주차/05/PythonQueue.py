import queue

Q = queue.Queue(maxsize=15)  # 큐 객체
S = queue.LifoQueue(maxsize=15)  # 스택 객체

for e in range(1,10):
    Q.put(e)
    S.put(e)

print("Queue : ", end='')
for _ in range(1,10):
    print(Q.get(), end=' ')
print()

print("Stack : ", end='')
for _ in range(1,10):
    print(S.get(), end=' ')
print()