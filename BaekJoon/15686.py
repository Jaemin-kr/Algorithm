from itertools import combinations


N, M = list(map(int,input().split()))
city = []
for _ in range(N):
    city.append(list(map(int, input().split())))

result = 999999
house = []
chicken_store = []

#print(arr)

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken_store.append([i,j])



for chicken in combinations(chicken_store, M):
	temp = 0
	for home_list in house:
		chicken_length = 999
		for j in range(M):
			chicken_length = min(chicken_length, abs(home_list[0] - chicken[j][0]) + abs(home_list[1] - chicken[j][1]))
		temp += chicken_length
	result = min(result, temp)

print(result)