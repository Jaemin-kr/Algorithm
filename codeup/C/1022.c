
#include <stdio.h>

int main(){
    char data[2000];
    fgets(data, 2000, stdin);
    printf("%s",data);
    
}