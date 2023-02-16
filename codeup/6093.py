n = int(input())
a = input().split() #문자로 인식하여 구분
for i in range(n) :  #0부터 n-1까지...
  a[i] = int(a[i])       #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장

for i in range(-1, -n-1, -1) :  #카운트한 값을 공백을 두고 출력
  print(a[i], end=' ')

