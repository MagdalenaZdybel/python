from decimal import Decimal
piecdziesiecioGroszowki = float(input("podaj ilość 50-groszówek: "))
dwudziestoGroszowki = float(input("podaj ilość 20-groszówek: "))
dziesiecioGroszowki = float(input("podaj ilość 10-groszówek: "))
piecioGroszowki = float(input("podaj ilość 5-groszówek: "))

lacznaWartoscBilonu = Decimal(float((piecdziesiecioGroszowki * 0.50) + (dwudziestoGroszowki * 0.20) + (dziesiecioGroszowki * 0.10) + (piecioGroszowki * 0.05)))
print("łączna warość bilonu wynosi: ", round(lacznaWartoscBilonu, 2), "zł")
