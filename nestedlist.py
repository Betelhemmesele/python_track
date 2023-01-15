if __name__ == '__main__':
    list1=[]
    list2=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
        list2.append(score)
    list2=sorted(set(list2))
    name1=[]
    nm=list2[1]
    for i in list1:
        if nm==i[1]:
            name1.append(i[0])
    name1.sort()
    for i in name1:
        print(i)
