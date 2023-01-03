import sys

word = list(sys.stdin.readline().rstrip())
word1 = []

for _ in range(int(sys.stdin.readline())):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'L':
        if word:
            word1.append(word.pop())
    
    elif cmd[0] == 'D':
        if word1:
            word.append(word1.pop())
    
    elif cmd[0] == 'B':
        if word:
            word.pop()
    
    else:
        word.append(cmd[1])

word.extend(reversed(word1))
print(''.join(word))