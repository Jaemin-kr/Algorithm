//arr에 두 수의 합이 100이되면 1 아니면 0 return 하는 함수

int func2(int arr[], int N){
    int occur[101] = {};
    for(int i=0; i<N; i++){
        if(occur[100-arr[i]] == 1)
            return 1;
        occur[arr[i]] = 1;
    
    }
    return 0;
}