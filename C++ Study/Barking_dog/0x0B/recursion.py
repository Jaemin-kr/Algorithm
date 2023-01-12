a = int(input())

def func1(n):
    if(n==0): return
    sum += n
    func1(n-1)

print(func1(a))
