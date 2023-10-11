n=int(input())
for i in range(1,n+1):
    if i!=1:
        print("that",end=' ')
    if i%2==0:
        print("I love",end= ' ')
    elif i%2!=0:
        print("I hate",end=' ')
print("it")