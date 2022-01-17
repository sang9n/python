import sys
sys.stdin = open("input.txt","rt")

n = int(input())
_list = list(map(int,input().split()))
_list.sort()
cnt=0
while len(_list)!=0:
    for _ in range(_list[-1]):
        if _list[-1]>len(_list):
            cnt+=1
            break
        _list.pop()
    
        
    cnt+=1

print(cnt)
