#include <stdio.h>
#include <stdlib.h>

long mnoz_zakres(int n) {
    
    long long suma = 0;
    for(int i=0; i < n; i++) {
        for(int j=0; j < n; j++) {
            suma += i * j;
        }
    }
    
    return suma;
}


int main(int argc, char **argv) {
    int n = atoi(argv[1]);
    
    long wynik = mnoz_zakres(n);
    printf("Wynik: %ld\n", wynik);

    return 0;
}
