try:
    a, b = map(int, input("Podaj liczby: ").split())
    operator = input('Operador operacja: ')
    if operator == '+' or operator == '-' or operator == '*' or operator == '/':
        match operator:
            case '+': print(a + b)
            case '-': print(a - b)
            case '*': print(a * b)
            case '/': print(a / b)
except Exception as e:
    print(e)
