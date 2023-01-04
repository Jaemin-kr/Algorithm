import sys

stack = []
N = int(input())
for _ in range(N):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == "push":
        stack.append(cmd[1])
    elif cmd[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if len(stack) != 0:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'pop':
        if len(stack) != 0:
            num = stack.pop()
            print(num)
        else:
            print(-1)

# import sys
# input = sys.stdin.readline

# n = int(input())

# stack = []
# for i in range(n):
#     command = sys.stdin.readline().split()

#     if command[0] == 'push':
#         stack.append(command[1])
#     elif command[0] == 'pop':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack.pop())
#     elif command[0] == 'size':
#         print(len(stack))
#     elif command[0] == 'empty':
#         if len(stack) != 0:
#             print(0)
#         else:
#             print(1)
#     elif command[0] == 'top':
#         if len(stack) != 0:
#             print(stack[-1])
#         else:
#             print(-1)

    
