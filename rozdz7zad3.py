#podróż samochodem. Zjazd do stacji benzynowej. Do następnej stacji jest 200 km. Napisz program który będzie Ci
#sugerował  czy masz zatankować na nastepnej stacji czy na jeszcze kolejnej. Program powinien zapytać o rzeczy:
#jak duży jest bak, jaki jest obecnie poziom paliwa w baku (w procentach) i ile jedzie na 1 litrze kilometrów.
#Dodatkowo zostaw w programie 5-litrowy zapas na margines błędu.

wielkoscBaku = float(input("Wpisz pojemność baku samochodu: "))
pozostaloscPaliwa = float(input("Wpisz ile procent paliwa pozostała w baku: "))
kmNaLitr = float(input("Wpisz ile średnio robisz km na 1 litrze paliwa: "))
zapasBezpieczenstwa = float(5)
odlegloscOdStacji = float(200)

tankowanie = wielkoscBaku - pozostaloscPaliwa * 0.1
print("Paliwa wystarczy Ci na: " , (tankowanie * kmNaLitr))
KolejneTankowanie = (tankowanie * kmNaLitr) / 200
print("Sugerujemy tankowanie na stacji paliw nr: ", KolejneTankowanie)


