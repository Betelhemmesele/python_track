n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    M=input().split()
    if M[0]=="pop":
        s.pop()
    elif M[0]=="discard":
        s.discard(int(M[1]))
    elif M[0]=="remove":
        s.remove(int(M[1]))
print(sum(s))
