#include <stdio.h>
#include <stdlib.h>

long mnoz_zakres(int n) {
    int *t1 = (int*) malloc (n * sizeof(int));
    int *t2 = (int*) malloc (n * sizeof(int));
    
    for(int i=0; i < n; i++) {
        t1[i] = i;
        t2[i] = i;
    }
    
    long long suma = 0;
    for(int i=0; i < n; i++) {
        for(int j=0; j < n; j++) {
            suma += t1[i] * t2[j];
        }
    }
    
    free(t1);
    free(t2);
    
    return suma;
}


int main(int argc, char **argv) {
    int n = atoi(argv[1]);
    
    long wynik = mnoz_zakres(n);
    printf("Wynik: %ld\n", wynik);

    return 0;
}
