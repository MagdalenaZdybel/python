from decimal import Decimal
print("Program przeliczający temperaturę ze stopni Fahrenheita na stopnie Celsjusza")
print("Wprowadz temperaturę w stopniach Fahrenheita: ")
StopnieF = float(input())
StopnieC = Decimal(float(5) / 9.0 * (StopnieF - 32))
print(StopnieF, 'stopni w skali Fahrenheita: ', 'to', round(StopnieC, 2), 'stopni Celsusza')

podajTemp = input()
fahrenheita = (float(podajTemp))
fahrenheita = (float(input("Poda")))