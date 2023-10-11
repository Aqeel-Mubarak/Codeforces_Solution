import math
for _ in range(int(input())):
    count=0
    a,b,c =map(int, input().split())
    if a> b:
        a=a-b
        a=a/2
        count = math.ceil(a/ c)
    elif b>a:
        b=b-a
        b=b/2
        count = math.ceil(b/ c)  
    elif a==b:
         count= 0
    print(count)