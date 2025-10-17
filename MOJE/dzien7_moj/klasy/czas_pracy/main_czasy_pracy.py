from klasa_czas_pracy import CzasPracy

def main():
    e = CzasPracy("Jan", "Nowak", 100.0)
    e.register_time(5)
    print("Wypłata:", e.pay_salary())  # 500.0
    print("Wypłata po raz drugi:", e.pay_salary())  # 0.0
    e.register_time(10)
    print("Wypłata po 10h:", e.pay_salary())  # 1200.0

if __name__ == '__main__':
    main()