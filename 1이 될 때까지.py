n , k = map(int,input().split())

cnt = 0
while True:
    tmp = (n//k)*k # n과 가장 가까운 k의 배수
    cnt += (n - tmp) # 1씩 빼주는걸 한번에 세기
    n = tmp
    n //=k
    cnt+=1
    if n < k:
        break

cnt += (n-1)
print(cnt)