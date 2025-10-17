#include <iostream>

int pierwsza_parzysta(int a, int b) {
    if(a % 2 == 0) {
        return a;
    }
    if(b % 2 == 0) {
        return b;
    }
}


int main() {
    std::cout << "Początek programu\n";
    std::cout << "parzysta(4, 6) " << pierwsza_parzysta(4, 6) << '\n';
    std::cout << "parzysta(7, 6) " << pierwsza_parzysta(7, 6) << '\n';
    std::cout << "parzysta(5, 9) " << pierwsza_parzysta(5, 9) << '\n';
    std::cout << "Koniec programu\n";

    return 0;
}
