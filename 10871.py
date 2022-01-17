import sys

N, X = map(int,input().split())

arr = list(map(int,sys.stdin.readline().split())) # 입력 여러 개 일 때

for i in range(N):
    if arr[i]<X:
        print(arr[i],end=' ')