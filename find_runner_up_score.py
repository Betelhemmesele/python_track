if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list1=[]
    for i in arr:
        if i not in list1:
            list1.append(i)
        else:
            continue
    list1.sort()
    print(list1[-2])
