sample = list(map(int, input().split()))
ascend = sorted(sample)
descend = sorted(sample, reverse=True)



if sample == ascend:
    print("ascending")
elif sample == descend:
    print("descending")
else:
    print("mixed")