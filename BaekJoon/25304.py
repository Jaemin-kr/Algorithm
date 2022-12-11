total_cost = int(input())
total_num = int(input())

for i in range(total_num):
    a, b = map(int, input().split())
    total_cost -= a*b
if total_cost == 0:
    print('Yes')
else:
    print('No')
