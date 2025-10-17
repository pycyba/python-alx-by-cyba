import java.util.stream.LongStream;

// W tej wersji używam "parallel stream", aby zrównoleglić obliczenia (wykorzystać wiele procesorów)
public class mnozenie5p {
    private static long mnoz_zakres(int n) {
        return LongStream.range(0, n)
            .parallel()
            .flatMap(i -> LongStream.range(0, n)
                    // .parallel()
                    .map(j -> i * j))
            .sum();
    }


    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        
        long wynik = mnoz_zakres(n);
        System.out.printf("Wynik: %d\n", wynik);
    }
}
