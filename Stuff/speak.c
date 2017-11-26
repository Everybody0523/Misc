#include<stdio.h>
#include<string.h>
#include<stdlib.h>

/*
Usage: First argument should be what you want to be said, second argument
the number of times. For when you want to make your computer talk a lot,
but don't want to keep hitting "say".
*/
int main(int argc, char ** argv){
    if (argc == 1 || argc == 2){
        fprintf(stderr, "Too few arguments! \n");
    }
    else if (argc > 3){
        fprintf(stderr, "Too many arguments! \n");
    }
    else{
        int n = strlen(argv[1]);
        int reps = atoi(argv[2]);
        char * command = malloc(sizeof(char) * (4 + n + 2));
        strcpy(command, "say ");
        strcat(command, argv[1]);
        for (int i = 0; i < reps; i++){
            system(command);
        }
        free(command);
    }
    return 0;
}
