# a = int(input())
# n = 0
# ans = 0

# while True:
#     n += 1
#     #print(n)
#     ans = (n*(n+1))/2
#     if ans >= a:
#         print(int(ans))
#         break
#     else:
#         continue
s = 0
c = 0
n = int(input())

while True :
  s += c
  c += 1
  if s>=n :
    break

print(s)