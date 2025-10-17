import java.util.stream.LongStream;

// W tej wersji używam "lamb i stream-ów", czyli elementów programowania funkcyjnego, dostępnych od Javy 8
public class mnozenie5 {
    private static long mnoz_zakres(int n) {
        return LongStream.range(0, n)
            .flatMap(i -> LongStream.range(0, n).map(j -> i * j))
            .sum();
    }


    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        
        long wynik = mnoz_zakres(n);
        System.out.printf("Wynik: %d\n", wynik);
    }
}
