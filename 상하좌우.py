n = int(input())

plans = input().split()
# 동(0,1) 서(0,-1) 남(1,0) 북(-1,0)
dx = [0,0,1,-1]
dy = [1,-1,0,0]
x,y = 1,1
move = ['R','L','D','U']

for plan in plans:
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
        if nx < 1 or ny < 1 or nx >n or ny > n:
            continue
        x,y = nx,ny
    
print(x,y)

