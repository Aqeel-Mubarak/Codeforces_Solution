first_sum=second_sum=0
length=int(input())
ticket=list(map(int,input()))
first=(len (ticket))//2
for i in range(first):
    first_sum+=ticket[i]
for i in range(first, len(ticket)):
    second_sum+=ticket[i]
def check(arg):
    for char in ticket:
        if char!=4 and char!=7:
            return False
    return True
if check(ticket)==True and first_sum==second_sum:
    print('YES')
else:
    print('NO')