print("Aby wyliczyć ilość potrzebnej wykładziny wprowadz następujące dane w centymetrach")
szerokosc_pokoju = float(input("Podaj szerokość pokoju: "))
dlugosc_pokoju = float(input("Podaj długość pokoju: "))
cenaWykladziy = float(input("Podaj cenę jednego metra2 wybranej wykładziny: "))
ile_potrzeba = szerokosc_pokoju * dlugosc_pokoju
kosztWykladziny = float(ile_potrzeba * 0.01) * cenaWykladziy
zmianaNaMetry = float(ile_potrzeba * 0.01)
print("Potrzebujesz: ", ile_potrzeba, "cm2 wykładziny, czyli ",zmianaNaMetry, "m2." )
print("Całkowity koszt wykładziny wyniesie: ", int(kosztWykladziny), "zł.")
