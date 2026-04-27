#include <stdio.h>
int divf(int n){
int i;
while (n%2==0) {
        printf("%d", 2);
        n=n/2;
    }
    for (i=3;i<=n;i=i+2) {
        while (n%i==0) {
            printf("%d",i);
            n=n/i;
        }
    }
    if (n>2) {
        printf("%d",n);
    }
}

int main()
{
int n,i;
    printf("enter the number:\n");
    scanf("%d",&n);
    if (n<0){
        printf("not a positive number");
    }
    else{
        divf(n);
    }
    return 0;
}
