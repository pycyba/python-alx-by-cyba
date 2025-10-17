from klasa_czas_pracy import CzasPracy

def test_scenariusz_zadania():
    e = CzasPracy("Jan", "Nowak", 100.0)
    e.register_time(5)
    assert e.pay_salary() == 500.0
    assert e.pay_salary() == 0.0
    e.register_time(10)
    assert e.pay_salary() == 1200.0

def test_kumulacja_rejestracji():
    e = CzasPracy("A", "B", 50.0)
    e.register_time(3)
    e.register_time(2.5)
    assert e.pay_salary() == 275.0

def test_nadgodziny_per_rejestracja():
    e = CzasPracy("A", "B", 80.0)
    e.register_time(9)
    e.register_time(7)
    assert e.pay_salary() == 1360.0

def test_wyzerowanie_po_wyplacie():
    e = CzasPracy("A", "B", 100.0)
    e.register_time(8)
    _ = e.pay_salary()
    assert e.pay_salary() == 0.0

def test_walidacja_godzin():
    e = CzasPracy("A", "B", 100.0)
    try:
        e.register_time(0)
        assert False, "Powinien być ValueError dla 0 godzin"
    except ValueError:
        pass
    try:
        e.register_time(-3)
        assert False, "Powinien być ValueError dla ujemnych godzin"
    except ValueError:
        pass

