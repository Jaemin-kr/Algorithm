import sys

input = sys.stdin.readline
result = 0

for _ in range(5):
    start, finish = input().split()

    h1, m1 = map(int, start.split(':'))
    h2, m2 = map(int, finish.split(':'))

    result += (h2*60+m2) - (h1*60+m1)

print(result)