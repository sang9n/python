n = int(input())

score = list(map(int,input().split()))


avg = round(sum(score)/n)

min = 2140000000

for idx , x in enumerate (score):
    tmp = abs(x-avg)
    if tmp<min:
        min = tmp
        a = x
        num = idx + 1
    elif tmp == min:
        if a < x:
            num = idx + 1

print(avg,num) # 파이썬은 지역변수 유효범위를 함수안에 선언했냐 안했냐로 구분
    
        