for _ in range(int(input())):
    n, m, k, h = map(int, input().split())
    x = list(map(int, input().split()))
    ran = [i*k for i in range(1, m)]
    count = 0
    for i in x:
        if abs(h-i) in ran:
            count += 1
    print(count)