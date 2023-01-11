score = int(input())

if score >= 90:
    print('A')
elif score < 90 and score >= 70:
    print('B')
elif score < 70 and score >= 40:
    print('C')
else:
    print('D')