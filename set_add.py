if __name__ == '__main__':
    N=int(input())
    set1=set()
    count=0
    for i in range(N):
        set1.add(input())
    for i in set1:
        count=count+1
    print(count)
