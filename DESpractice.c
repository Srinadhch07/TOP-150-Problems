#include <stdio.h>

int main() {
    int i, p8[8] = {6, 7, 8, 9, 4, 3, 2, 1};
    int p10[10] = {6,7,8,9,10,1,2,3,4,5};
    char input[11], temp[11],k1[9]; 

    printf("Enter 10 bit String:");
    scanf("%s", input);

    for (i = 0; i < 10; i++) {
    	char bit = input[p10[i] - 1];
        temp[i] = bit; 
        printf("%c",temp[i]);
	    }
	    
	    for(i=0;i<5;i++){
	    	temp[i]=(i==4)?temp[10]:temp[i+1];
		}
		printf("\nLS-1 = %s",temp);
		for(i=5;i<10;i++){
			temp[i] = (i==9)?temp[5]:temp[i+1];
		}
		
		printf("\nLS-2 =  %s",temp);
		for(i=0; i<8;i++){
			k1[i]=temp[p8[i]-1];
		}
		printf("\nKey-1 = %s",k1);

    return 0;
}