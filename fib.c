#include <stdlib.h>
#include <stdio.h>

void fib(int **f_pointer, int n){
  int *outputSorta = malloc(sizeof(int) * n);
  outputSorta[0] = 0;
  outputSorta[1] = 1;
  int i;
  for(i = 2; i <= n; i++){
    outputSorta[i] = outputSorta[i-2] + outputSorta[i-1];
  }
  *f_pointer = outputSorta;
}

int main(int argc, char **argv){
  int count = strtol(argv[1], NULL, 10);
  int *fib_sequence;
  fib(&fib_sequence, count);
  printf("%d\n", fib_sequence[count - 1]);
}
