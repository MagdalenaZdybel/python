import random

tajemnica = random.randint(1, 150)
strzal = 0
proba = 0
print("Wpisz swoją propozycję liczby i sprawdź czy trafisz! ")
print("Liczba musi mieścić się w zakresie 1 do 150 . Maksymalna ilość próbnych trafień to 6 razy")
while strzal != tajemnica and proba < 6:
    strzal = int(input("Podaj swoją liczbę: "))
    if strzal < tajemnica:
        print("Za mało! Strzelaj jeszcze raz")
    elif strzal > tajemnica:
        print("Za dużo! Strzelaj ponownie!")

    proba = proba + 1

if strzal == tajemnica:
    print("Hurraaaaa! Trafiony!")
else:
    print("Nie udało się. Kołczan świeci pustką bo wszystkie strzały wykorzystałeś!")
    print("Tajemną liczbą to", tajemnica)
