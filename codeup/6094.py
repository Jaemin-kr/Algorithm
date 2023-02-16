n = int(input())
a = input().split() #문자로 인식하여 구분
for i in range(n) :  #0부터 n-1까지...
  a[i] = int(a[i])       #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장

a = sorted(a)
print(a[0])

