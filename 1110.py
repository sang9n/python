N = int(input())
cnt = 0
while True:
    
    a = N//10
    b = N%10
    c = a+b
    d = 10*b+c
    cnt+=1
    e = d//10
    f = d%10