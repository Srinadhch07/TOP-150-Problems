#include<stdio.h>
 int main(){
    int i, p8[8]={6,7,8,9,1,2,3,4};
    int p10[10] = {6,7,8,9,10,1,2,3,4,5};
    char input[11], temp[11],k1[9],sri[10];

    printf("Enter 10 bits inputs: ");
    scanf("%s",input);
    for(i=0;i<10;i++){
        temp[i]=input[p10[i]-1];
        printf("%i",p10[i]-1);
    }
    printf("\nTemp value :%s\n",temp);
    printf("Input value :%s\n",input);
    temp[10] = '\0';
    printf("Bits after p10:%s\n",temp);
    //printf("sri[10] value:%d\n",sri[9]);
    for(i=0;i<5;i++)
        temp[i]=(i==4)?temp[10]:temp[i+1];
    for(i=5;i<10;i++)
        temp[i] = (i==9) ? temp[5]: temp[i+1];
    printf("Output after LS-1: %s\n",temp);

    for(i=0;i<8;i++)
        k1[i]=temp[p8[i]-1];
    k1[8] ='\0';
    printf("key k1:%s\n",k1);

    return 0;
 }