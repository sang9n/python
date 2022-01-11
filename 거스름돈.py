n = 1260

_list = [500 , 100 ,50 ,10]
cnt = 0
for i in _list:
    cnt += n//i
    n = n%i

print(cnt)

# 큰 단위가 항상 작은 단위의 배수이므로 가장 큰 화폐 단위부터 거슬러 주는 것이 최적의 해