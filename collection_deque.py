from collections import deque
n=int(input())
d=deque()
for _ in range(n):
    inp=list(input().split())
    if inp[0]=="append":
        d.append(int(inp[1]))
    elif inp[0]=="appendleft":
        d.appendleft(int(inp[1]))
    elif inp[0]=="pop":
        d.pop()
    elif inp[0]=="popleft":
        d.popleft()
for i in d:
    print(i ,end=" " )
