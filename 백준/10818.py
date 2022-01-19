N = int(input())
arr = list(map(int,input().split()))
max = arr[0] # max = arr[0] 
min = arr[0] # min = arr[0]
for i in range(N):
    if arr[i] > max:
        max = arr[i]
    elif arr[i] < min:
        min = arr[i]
    else:
        pass
print(min, max)