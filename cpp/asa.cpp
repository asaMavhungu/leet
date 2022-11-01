#include <stdio.h>

int main()
{
	int j;
	int i;
	int *p; // declare pointer

	i = 7;
	p = &i; // The pointer now holds the address of i
	j = *p; // j = *(&i)

	printf("i = %d \n", i);  // value of i
	printf("j = %d \n", j);  // value of j
	printf("*p = %d \n", p); // the address held by the pointer

	*p = 32; // asigns value to i via the pointer

	printf("i = %d \n", i);   // value of i
	printf("j = %d \n", j);   // value of j
	printf("*p = %d \n", p);  // the address held by the pointer
	printf("&i = %d \n", &i); // address of i
  
  	return 0;
}