#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;
int board[100][100] = {0, };

void check_board(int a, int b){
    for(int i = a; i < a+10; i++){
        for(int j = b; j< b+10; j++){
            board[i][j] = 1;
        }
    }
}

int main(){
    //iostream과 stdio버퍼 동기화
    ios::sync_with_stdio(0);
    cin.tie(0); 

    int n, cnt = 0;
    cin >> n;
    for(int i=0; i<n; i++){
        int x, y;
        cin >> x >> y;
        check_board(x, y);
    }

    for(int i=0; i<100; i++){
        for(int j = 0; j<100; j++){
            if(board[i][j] == 1){
                cnt += 1;
            }
        }
    }

    cout << cnt;

    


}
