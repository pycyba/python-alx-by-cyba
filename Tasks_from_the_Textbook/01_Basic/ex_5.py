cityaA = str(input("City A: "))
cityaB = str(input("City B: "))
dyst = float(input(f"Dystans {cityaA} - {cityaB}: "))
cenapaliwa = float(input(f"Cena paliwa: "))
srednie = float(input(f"Srednie spalanie: "))

koszt = dyst * (srednie/100) * cenapaliwa
print(f"Koszt przejazdu {cityaA} - {cityaB} wynosi {koszt: .0f}")




