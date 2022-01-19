A = int(input())
B = int(input())
C = int(input())
arr = [0]*10

tmp = str(A*B*C)
for i in tmp:
    
    for j in range(10):
        if i ==str(j):
            arr[j]+=1

for i in range(10):
    print(arr[i])




