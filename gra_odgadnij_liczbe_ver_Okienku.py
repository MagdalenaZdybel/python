import random, easygui

tajemnica = random.randint(1, 99)
strzal = 0
proba = 0
easygui.msgbox("Wpisz swoją propozycję liczby i sprawdź czy trafisz!")
easygui.msgbox("Liczba musi mieścić się w zakresie 1 do 99 . Maksymalna ilość próbnych trafień to 6 razy")
while strzal != tajemnica and proba < 6:
    strzal = easygui.integerbox("Jaka to liczba?")
    if strzal < tajemnica:
        easygui.msgbox(str(strzal) + " jest za mała, próbuj jeszcze raz!")
    elif strzal > tajemnica:
        easygui.msgbox(str(strzal) + "jest za duża, próbuj jeszcze raz!")

    proba = proba + 1

if strzal == tajemnica:
    easygui.msgbox("Skuces, trafiłeś w sam środek i odgadłeś tajemną liczbę! Gratulacje! Zagraj ponownie!")
else:
    easygui.msgbox("Wykorzystałeś wysztkie strzały i kołczan wieje pustką! Zagraj jeszcze raz! Tajemna liczba to "
                   + str(tajemnica))
