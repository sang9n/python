# import sys
# sys.stdin = open("input.txt","rt")

T = int(input())

for _ in range(T):
    arr = list((input()))
    cnt=0
    tot=0

    for i in range(len(arr)):
        if arr[i]=='O':
            cnt+=1
        else:
            cnt=0
        tot+=cnt
        
    print(tot)