#include <stdio.h>
#include <string.h>

char * itoa(int num){
    char *str = "00";
    sprintf(str, "%d", num);
    return str;
}

int main(){
    int *nums;
    *nums = 1;
*nums++ = 2;
printf("%lu", sizeof(nums));
    return 0;
}
