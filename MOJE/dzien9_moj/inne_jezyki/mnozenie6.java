import java.math.BigInteger;

// W tej wersji do reprezentowania liczb używam klasy BigInteger, czyli liczb bez ograniczenia na wielkość; czegoś, co działa analogicznie do Pythonowego int.

public class mnozenie6 {
    private static BigInteger mnoz_zakres(int n) {
        BigInteger[] t1 = new BigInteger[n];
        BigInteger[] t2 = new BigInteger[n];
        
        for(int i=0; i < n; i++) {
            t1[i] = BigInteger.valueOf(i);
            t2[i] = BigInteger.valueOf(i);
        }
        
        BigInteger suma = BigInteger.ZERO;
        for(BigInteger x : t1) {
            for(BigInteger y : t2) {
                suma = suma.add(x.multiply(y));
            }
        }
        
        return suma;
    }


    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        
        BigInteger wynik = mnoz_zakres(n);
        System.out.printf("Wynik: %d\n", wynik);
    }
}
