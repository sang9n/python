import sys
# sys.stdin = open("input.txt","rt")

C = int(input())
for _ in range(C):

    arr = list(map(int,sys.stdin.readline().rstrip().split()))
    N = arr[0]
    arr = arr[1:]
    avg = sum(arr)/len(arr)
    over_avg = 0
    for i in arr:
        if i > avg:
            over_avg +=1
    rate = over_avg/len(arr)*100
    print("{:.3f}%".format(rate))
    # rate = round(over_avg/len(arr)*100,3)
    # print(f"{rate}%")
    # print(N)
    # print(arr)

