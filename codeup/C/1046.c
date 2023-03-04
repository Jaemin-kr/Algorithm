#include <stdio.h>

int main(){
    long int a, b, c;
    //float ans;
    scanf("%ld %ld %ld",&a,&b,&c);

    printf("%ld\n", a+b+c);
    printf("%.1f\n", (float)(a+b+c)/3);
    
}
