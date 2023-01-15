if __name__ == '__main__':
    N = int(input())
    list1=[]
    for i in range(0,N):
        cm=input().split()
        if cm[0]=="insert":
            list1.insert(int(cm[1]),int(cm[2]))
        elif cm[0]=="remove":
            list1.remove(int(cm[1]))
        elif cm[0]=="append":
            list1.append(int(cm[1]))
        elif cm[0]=="print":
            print(list1)
        elif cm[0]=="sort":
            list1.sort()
        elif cm[0]=="pop":
            list1.pop()
        else:
            list1.reverse()
