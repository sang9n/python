

min = 100

for i in range(1,10):
    tmp = int(input())
    dif = abs(tmp-100)
    if dif < min:
        min = dif
        ans1 = tmp 
        ans2 = i

    
print(ans1)
print(ans2)
