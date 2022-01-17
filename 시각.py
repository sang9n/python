n = int(input())
m = 59
s = 59
cnt = 0
for i in range(n+1):
    for j in range(m+1):
        for k in range(s+1):
            if '3' in str(i)+str(j)+str(k):
                cnt+=1
print(cnt)

