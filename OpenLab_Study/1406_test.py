#시간 초과 ㅠㅠ
import sys
input = sys.stdin.readline
str_t = input()
cusor_position = len(str_t)
for i in range(int(input())):
    command = input()
    if command == "L" and cusor_position > 0:
        cusor_position -= 1
    elif command == "D" and cusor_position < len(str_t)+1:
        cusor_position += 1
    elif command == "B" and cusor_position > 0:
        str_t = str_t[:cusor_position-1]+str_t[cusor_position:]
        cusor_position-=1
    elif command[0] == "P":
        str_t = str_t[:cusor_position]+command[2]+str_t[cusor_position:]
        cusor_position+=1

print(str_t)