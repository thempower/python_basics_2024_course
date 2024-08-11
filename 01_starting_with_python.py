imie = input("Jak masz na Imię? ")
wiek = input("Ile masz lat? ")


print("Cześć " + imie + " zapraszamy do skorzystania z naszej oferty")
print(imie + " masz " + wiek +  " lat " )

if int(wiek) >= 18:
    print("Jesteś pełnoletni(-a)")
else:
    print("Nie jesteś pełnoletni(-a)")

