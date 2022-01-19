# import sys
# sys.stdin = open("input.txt","rt")

N = int(input())

arr = list(map(int,input().split()))
# max = 0
# for i,val in enumerate(arr):
#     if val > max:
#         max = val
#         idx = i
max = max(arr)

tot = 0
for i in range(N):
    # if i == idx:
    #     continue
    
    tot += arr[i]/max*100

avg = tot/N
print(avg)
