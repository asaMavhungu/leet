#include <stdio.h>

void func(int *v){
  (*v)++;
}

int
main () {
    int a = 5;
    func(&a);
    printf("a: %d\n", a); // output-> a: 6
    
    return 0;
}