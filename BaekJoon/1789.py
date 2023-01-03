N=int(input())
sum=0
start=0
while N >= sum: #N이 sum이상이면
    start+=1 #start를 1씩 증가시킴
    sum+=start #sum에 start값을 합함
    if N <= sum: #N이 sum보다 작으면
        break #탈출

print(start-1) 