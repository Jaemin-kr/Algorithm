#include <stdio.h>
#include <algorithm>
using namespace std;
int main()
{
    printf("입력\n");
    int N;
    scanf("%d", &N);//수의 개수
    int num[500000] = {};
    int i = 0;
    while (i < N)//num에 수 담기
    {
        scanf("%d", &num[i]);
        i++;
    }
    sort(num, num + N);//오름차순 정리
    i = 0;
    long long int mean = 0;//산술평균
    printf("결과\n");
    while (i < N)
    {
        mean = mean + num[i];
        i++;
    }
    double Mean = static_cast<double>(mean);
    Mean = Mean / N;
    if(Mean<1&&Mean>-0.5)//-0방지
    {
        Mean=-Mean;
    }
    printf("%0.lf\n", Mean);
    long long int median = num[N / 2];//중앙값
    printf("%d\n", median);
    i = 0;
    long long int a=0, b=0, n=1, freq=0;//최빈값
    while (i < N)
    {
        if (num[i] == num[i + 1])  //현숫자와 다음숫자가 같을 때
        {
            a++;
        }
        else  //현숫자와 다음숫자가 다를 때
        {
            if (a > b)  //현횟수가 저장횟수보다 클 때
            {
                b = a;//b에 횟수 저장
                n=1;
                freq = num[i];
            }
            else if(a==b) //현횟수와 저장횟수가 같을 때(최빈값이 여러개일 때 두번째로 작은값 맞추기)
            {
                n++;
                if(n==2)
                {
                    freq=num[i];
                }
            }
            a = 0;
        }
        i++;
    }
    if (b == 0)  //같은수가 안나왔을 때
    {
        freq = num[1];
    }
    if(N==1) //수가 한개
    {
        freq=num[0];
    }
    printf("%d\n",freq);
    long long int range=num[N-1]-num[0];//범위
    printf("%d",range);
    return 0;
}