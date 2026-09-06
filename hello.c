#include <stdio.h>
#include <stdio.h>

int main(){
    int n;
    int a,max,min;

    scanf("%d", &n);
    scanf("%d", &a);
    max = min = a;

    for(int i=1;i<n;i++){
        scanf("%d", &a);
        if (a>max){
            max = a;}  
        if(a<min){
            min = a;
        }
    }
    printf("%d", max - min);
}