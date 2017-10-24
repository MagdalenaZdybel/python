from decimal import Decimal
StopnieF = 65
StopnieC = Decimal(float(5) / 9.0 * (StopnieF - 32))
print(StopnieF, 'stopni w skali Fahrenheita: ', 'to', round(StopnieC, 2), 'stopni Celsusza')