if __name__ == '__main__':
    # take input from stdin 
    N = int(input())
    set1=set(map(int,input().split()))
    M = int(input())
    set2=set(map(int,input().split()))

    
    set3=(set1.difference(set2)).union(set2.difference(set1))
    for i in sorted(list(set3)):
            print(i) 
   
