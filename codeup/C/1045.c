#include <stdio.h>

int main(){
    long int a, b, temp;
    scanf("%ld %ld",&a,&b);
    if(a < b){
        a = temp;
        a = b;
        b = temp;
    }
    printf("%ld\n", a+b);
    printf("%ld\n", a-b);
    printf("%ld\n", a*b);
    printf("%ld\n", a/b);
    printf("%ld\n", a%b);
    printf("%.2f\n", float(a)/float(b));
    
}
