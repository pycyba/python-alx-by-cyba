// Najbardziej oczywista implementacja w Javie
// Wersja z tworzeniem tablic.

public class mnozenie4 {
    private static long mnoz_zakres(int n) {
        int[] t1 = new int[n];
        int[] t2 = new int[n];
        
        for(int i=0; i < n; i++) {
            t1[i] = i;
            t2[i] = i;
        }
        
        long suma = 0;
        for(int x : t1) {
            for(int y : t2) {
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
