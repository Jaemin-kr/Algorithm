num = input()
arr = [0] * 9 #0~9배열
# num_list = list(str(num))

#print(num)
for i in num: #0 ~ 
    number = int(i) #자리수 분리
    if number == 9: #number가 9면 6으로
        number = 6
    arr[number] += 1 #0~8까지는 추가시 +1
arr[6] = (arr[6]+1) // 2 #6+9의 개수를 통해 6,9가 많을 경우 세트수 구하기
print(max(arr))