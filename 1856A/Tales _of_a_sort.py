t=int(input())
for _ in range(t):
    curr=0
    n=int(input())
    ls=list(map(int,input().split()))
    for i in range(n-1):
        if ls[i]>ls[i+1]:
            curr=max(curr,ls[i])
    print(curr)