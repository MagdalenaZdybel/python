import random,easygui
tajemnica = random.randint(1, 150)
strzal = 0
proba = 0
easygui.msgbox("""Wpisz swoją propozycję liczby i sprawdź czy trafisz!
               Liczba musi mieścić się w zakresie 1 do 150 . Maksymalna ilość próbnych trafień to 6 razy""")
while strzal != tajemnica and proba <6:
    strzal = easygui.integerbox("Jaka to liczba?")
    if strzal < tajemnica:
        easygui.msgbox(str(strzal) + " jest za mała, próbuj jeszcze raz"