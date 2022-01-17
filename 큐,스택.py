# 스택   선입후출 // DFS,재귀함수
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()
print(stack[::-1])
print(stack)
# 큐 (시간 복작도를 줄이기 위해 모듈 임포트)  선입선출

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
