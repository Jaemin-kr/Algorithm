#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int sum = 0;

    for(int i = 0; i < 11; i++){
        sum += i;
    }

    cout << "합은 : " << sum << '\n';

    sum = 0;
    int i = 0;
    while(i <11){
        sum += i;
        i++;
    }

    cout << "while의 sum : " << sum << "\n";

    int luckey_num = 7;
    int user_in = 0; 
    while(user_in != luckey_num){
        cout << "luckey num 입력" << '\n';
        cin >> user_in;
        if(luckey_num == user_in){
            cout << "맞았습니다~" << '\n';
        } 
        else{
            cout << "다시 생각해보세요~" << '\n';
        }
    }

}