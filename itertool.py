from itertools import combinations, permutations

nums = [1,2,3,4]
permu = list(permutations(nums, 2))
#nums 중 2개 선택
combi = list(combinations(nums, 2))
#nums 중 순서에 관계없이 2개
print(permu)
print(combi)