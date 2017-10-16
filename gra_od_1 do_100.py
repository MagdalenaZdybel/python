from random import randint

wylosowano = randint(1, 100)

Costam = True
while True:
    while Costam:
        wprowadzona = int(input('wpisz liczbe'))

        if wprowadzona == wylosowano:
            print('gol!!!')
            Costam = False
        elif wprowadzona < wylosowano:
            print('za mało')
        elif wprowadzona > wylosowano:
            print('za duzo')




