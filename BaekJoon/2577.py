a = int(input())
b = int(input())
c = int(input())

num_list = list(str(a*b*c))

for i in range(10):
    print(num_list.count(str(i)))