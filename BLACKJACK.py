try:
    t=int(input())
    for i in range(0,t):
        x, y = [int(x) for x in input().split(" ")]

        if(21-(x+y)>10 or 21-(x+y)<1):
            print(-1)
        else:
            print(21-(x+y))
except:
    pass
