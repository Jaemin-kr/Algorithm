T = int(input())
stack = []
operand = []
cnt = 1
temp = True

for i in range(T):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        operand.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        operand.append('-')
    else:
        temp = False

if temp == False:
    print("NO")
else:
    for i in operand:
        print(i)