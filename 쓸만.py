#if i%2: continue  # 홀수 이면 참이되므로 continue실행됨 (나머지 부분을 건너뛰고 조건식으로 넘어감) 
# continue문은 연산 비용이 많이 든다 --> 사용 지양

# numbers = [1,2,3,4,5]
# twise = [num*2 for num in numbers if num%2 ==1] # 실행(3) for(1) 조건(2)
# print(twise)
#파이썬에는 함수가 시작하고 종료함에 따라 객체가 생성되거나 소멸하지 않는다
# [::-1] 맨 끝에서부터 전부 출력 ( 거꾸로 출력 )

# num = 3
# x = [None]*num
# for i in range(num):
#     x[i]=int(input())

# print(x)

# x1= []
# for _ in range(num):
#     x1.append(int(input()))
# print(x1)

# list1 = [1,2,3]
# list2 = [1,2,3]
# print (list1 is list2) # 고정된 값이 아니기 때문에 같지 않다 False (튜플도 마찬가지)
# import copy
# li1 =[1,2,3]
# li2 = li1
# li1[0] = 5
# print(li2) # li1과 li2는 같은 리스트를 참조하고 li2도 함께 바뀐다.
# li2 = copy.deepcopy(li1) # li1의 원소가 바뀌어도 li2가 바뀌지 않는다
# print(li2)
# li1[0]=10
# print(li1)

# print(li2)
# a = list(range(1,10))
# n = len(a)
# for i in range(n//2):
#     a[i],a[n-i-1] = a[n-i-1],a[i]

# print(a)
# def reverse(a,b):
#     a,b = b,a
#     return a ,b

# q=2
# w=3
# q,w=reverse(q,w)
# print(q,w)

# def reverse_arr(arr):
#     le = len(arr)
#     for i in range(le//2):
#         arr[i],arr[le-1-i] = arr[le-1-i],arr[i]


# arr1 = [1,2,3,4,5]
# reverse_arr(arr1)
# print(arr1)

# def sum_all(n): # 1부터 n까지의 합 구하기           # 중요!! 파이썬에서 지역 변수는 함수 내에서 선언된 변수 -> 함수 내에서 선언된 지역변수는 함수 내에서만 사용 가능
#     tot = 0
#     while n!=0:
#         tot +=n
#         n-=1
#     return tot

# a= 10
# total = sum_all(a)
# print(total)

# def change(arr,idx , val):
#     arr[idx]=val

# arr1 = [1,2,3,4,5,6,7,8,9,10]
# index = int(input("바꾸고 싶은 인덱스 = "))
# value = int(input("바꾸고 싶은 값 = "))
# change(arr1,index,value)
# print(arr1 , sep='*')

# def bin(arr1,key):
#     arr1.sort() # 이진 검색 하기 위해 오름차순 정렬    # 이진 검색이 선형 검색보다 더 빠름
#     first = 0 # 검색 범위 맨 앞 인덱스
#     last = len(arr1)-1 # 검색 범위 맨 끝 인덱스
#     while True:
#         mid = (first + last)//2
#         if arr1[mid]==key:
#             return mid
#         elif arr1[mid]<key:
#             first = mid+1
#         else:
#             last = mid-1

#         if first>last:
#             break
#     return -1

# if __name__ == '__main__':
#     num = int(input('원소 수'))
#     arr = [None]*num
#     # arr.append((int,input().split()))
#     for i in range(len(arr)):
#         arr[i] = int(input())
#     print(arr)
# import hashlib
# class Node:

#     def __init__(self,key:any,value:any,next:Node):

# import hashlib

class HashTable:
    def __init__(self):
        self.hash_table=list([0 for _ in range(8)]) # 해쉬
    def hash_function(self,key):
        return key%8
    def insert(self,key,value):
        hash_value = self.hash_function(hash(key))
        self.hash_table[hash_value] = value
    def read(self,key):
        hash_value = self.hash_function(hash(key))
        return self.hash_table[hash_value]

    def print(self):
        print(self.hash_table)



# a = [0 for i in range(10)]
# print(a)
# a = [[0]*2]*3 # 이렇게 2차원 행렬을 만들면 각 행이 똑같은 값을 참조 #121참고
# b = [[0 for _ in range(3)] for _ in range(3)]
# print(b)
# a[0][0]=1 #
# b[0][0]=1



    