n,m,k = map(int,input().split())

_list = list(map(int,input().split()))
_list.sort()
max1 = _list[-1]
max2 = _list[-2]

res = 0
cnt = 0

cnt += int(m/(k+1))*k + m%(k+1)  # 최댓값 갯수 # 공식을 만들어서 간단하게 작성 가능

res += max1*cnt
res += max2*(k-cnt)
print(res)