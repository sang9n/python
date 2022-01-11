n,m,k = map(int,input().split())

_list = list(map(int,input().split()))

_list.sort()
max1 = _list[-1]
max2 = _list[-2]
cnt =0
sum =0

while True:
    for _ in range(k):
        if cnt == m:
            break
        sum +=max1
        cnt+=1
        
    sum += max2
    cnt+=1
    if cnt == m:
        break
    