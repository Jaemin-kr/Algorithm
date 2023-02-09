while True:
    exam = list(map(int, input()))
    #print(sum(exam))
    cnt = 0
    if sum(exam) == 0:
        break
    #print("print - ",exam[-1])
    for i in range(len(exam)):
        #print("len", len(exam))
        #print(exam[-i])
        #print(exam[i])
        if exam[i] != exam[-i-1]:
            cnt += 1
        else:
            continue
    if cnt == 0:
        print("yes")
        #exam = []
    elif cnt != 0:
        print("no")
        #exam = []


