t = int(input())

score_list = list(map(int, input().split()))
max_score = max(score_list)

new_score = []
for score in score_list:
    new_score.append(score/max_score*100)

avg_score = sum(new_score)/t
print(avg_score)