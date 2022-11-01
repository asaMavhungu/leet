#include <stdio.h>

int main(void){
	int i = 3;
	int j = i;
	
	i = 2;

	printf("i = %d %d \n", i, j);  // value of i
}