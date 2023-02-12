
def GCD(num1,num2):
    while(num2):
        num1,num2 = num2, num1%num2
    return num1

def LCM(num1,num2):
    ans = (num1*num2)//GCD(num1,num2)
    return int(ans)

a,b = map(int,input().split())
print(GCD(a,b))
print(LCM(a,b))