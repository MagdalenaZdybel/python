haslo = "wielkarzecz"
podajHaslo = input(" Podaj hasło: ")
if podajHaslo == haslo:
     print("Brawo!")
     zakupy = float(input("Podaj kwotę za zakupy: "))
     rabat10 = zakupy * 0.10
     rabat20 = zakupy * 0.20

     if zakupy <= 50:
                print("Rabat wynosi " , "10%" , ", kwota rabatu: " , rabat10, "do zapłaty: ", (zakupy - rabat10))
     else:
            print("Rabat wynosi: " , "20%", ", kwota rabatu: ", rabat20 , "do zapłaty: ", (zakupy - rabat20))
else:
    print("Se ne udało")