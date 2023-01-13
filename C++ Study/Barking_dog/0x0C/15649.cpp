#include <bits/stdc++.h>
using namespace std;

int n,m;
int arr[10];
bool isused[10];

void func(int k){ //현재 k개까지의 수를 택함
    if(k==m){ //m개를 모두 선택했으면
        for(int i = 0; i < m; i++)
            cout << arr[i] << ' '; //arr에 기록한 수열을 출력
        cout << '\n';
        return;
    }

    for(int i = 1; i <= n; i++){//1~n까지
        if(!isused[i]){ //i가 사용되지 않았으면
            arr[k] = i; //k번째 수를 i로 정함
            isused[i] = 1; //i를 사용했다고 표시
            func(k+1); //다음수를 정하러 k+1로 들어감
            isused[i] = 0; //k번째수를 i로 설정한 경우에 대해 모두 확인했으므로 i를 사용되지 않았다고 명시
        }
    }
}

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
    func(0);
}
