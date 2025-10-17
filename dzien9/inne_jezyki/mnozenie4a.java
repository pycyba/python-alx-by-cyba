// Najbardziej oczywista implementacja w Javie
// Wersja bez tworzenia tablic.

public class mnozenie4a {
    private static long mnoz_zakres(int n) {
        long suma = 0;
        for(int x=0; x < n; x++) {
            for(int y=0; y < n; y++) {
                suma += x * y;
            }
        }
        return suma;
    }


    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        
        long wynik = mnoz_zakres(n);
        System.out.printf("Wynik: %d\n", wynik);
    }
}
