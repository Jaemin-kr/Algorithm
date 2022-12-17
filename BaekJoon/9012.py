import sys
T = int(input()) #반복 횟수

for _ in range(T):
    cnt = 0  #괄호를 저장할 변수
    arr = sys.stdin.readline()  #괄호 입력을 받아옴
    print(arr)
    for i in arr: #입력받은 괄호의 길이동안
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
        #(입력시 괄호 +, )입력시 괄호 -
        if cnt < 0: #전체괄호의 짝이 맞지 않으면 break
            break
    if cnt == 0: #전체 괄호의 짝이 맞으면 YES
        print("YES")
    else:
        print("NO") #아니면 NO
