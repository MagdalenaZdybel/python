#drużyna piłkarska poszukuje  dziewczyn do zespołu. wiek od 10 do 12 lat. Pytanie o płeć ("d" dziewczynka, "c" chłopiec.
#komunikat informujmący o tym, że dany użytkownik kwalifikuje się do drużyny. Dodatkowo - chłopcóww nie pyta już o wiek.
plec = str(input('Podaj swoją płeć. Jeśli jesteś dziewczynką wpisz "d". Jeśli jesteś chłopcem wpisz: "c": '))
if plec == str("d"):
    wiek = int(input("Podaj swój wiek: "))
    if wiek >= 10 and wiek <= 12:
        print("Zapraszamy do drużyny!")
    elif plec == str("d") and wiek >= 13:
        print("Niestety ale to drużyna dla dziewcząt w wieku od 10 do 12 lat.")
    elif plec == str("d") and  wiek <= 9:
        print("Niestety ale to drużyna dla dziewcząt w wieku od 10 do 12 lat.")
else:
    print("To drużyna dla dziewcząt. Nie możesz się zapisać.")