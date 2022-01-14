import sys
sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())
result = 0
min_v = 412000

for _ in range(n):
    _list = list(map(int,input().split()))
    min_v = min(_list) # 리스트 안에서 작은 것
    # print(min_v)
    result = max(result,min_v) # 작은 것 중에 가장 큰 것
print(result)
    