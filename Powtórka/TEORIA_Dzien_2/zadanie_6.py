# Kalkulator: +, -, *, /, //, %
# Walidacja wejścia i dzielenie przez zero

# 1) Pobranie liczb
while True:
    try:
        x, y = map(float, input("Podaj dwie liczby (oddzielone spacją): ").split())
        break
    except ValueError:
        print("Błąd: podaj dwie liczby, np. 3 4.5.")

# 2) Pobranie operatora
dozwolone = {"+", "-", "*", "/", "//", "%"}
while True:
    operator = input("Podaj operator (+, -, *, /, //, %): ").strip()
    if operator in dozwolone:
        break
    print("Błąd: nieznany operator.")

# 3) Obliczenia z obsługą dzielenia przez zero
try:
    match operator:
        case "+":
            wynik = x + y
        case "-":
            wynik = x - y
        case "*":
            wynik = x * y
        case "/":
            if y == 0:
                raise ZeroDivisionError("Dzielenie przez zero.")
            wynik = x / y
        case "//":
            if y == 0:
                raise ZeroDivisionError("Dzielenie przez zero.")
            wynik = x // y
        case "%":
            if y == 0:
                raise ZeroDivisionError("Dzielenie przez zero.")
            wynik = x % y
        case _:
            # Teoretycznie nieosiągalne dzięki walidacji
            print("Nieznany operator.")
            raise SystemExit(1)

    print(f"Wynik: {x} {operator} {y} = {wynik}")

except ZeroDivisionError as e:
    print(f"Błąd: {e}")