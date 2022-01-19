
arr = [0]*10
cnt = 1
for i in range(10):
    n = int(input())
    arr[i] += n%42
'''
arr =[]
for i in range(10):
    n= int(input())
    arr.append(n%42)
''' 
arr = set(arr) # 중복 없애주는 자료구조
print(len(arr))