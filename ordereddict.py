from collections import OrderedDict
n=int(input())
orddict = OrderedDict()
for _ in range(n):
    line = input().rstrip().split()
    item_name, net_price = ' '.join(line[:-1]), int(line[-1])
    if item_name in orddict:
        orddict[item_name]+=net_price
    else:
        orddict[item_name]=net_price
for item in orddict:
    print(item,orddict[item])
