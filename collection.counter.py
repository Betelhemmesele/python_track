from collections import Counter
n=int(input())
list1=list(map(int,input().split()))
m=int(input())
list1=Counter(list1)
earning=0
for i in range(m):
    size,price=map(int,input().split())
    if list1[size]:
        list1[size]-=1
        earning=earning+price
print(earning)
