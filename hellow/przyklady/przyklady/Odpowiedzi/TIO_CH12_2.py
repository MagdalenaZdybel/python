# TIO_CH12_2.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Odpowied� do zadania praktycznego 2, z rozdzia�u 12.

listaImion = []
print "Wprowad� pi�� imion (po ka�dym z nich naci�nij Enter):"
for i in range(5):
    imie = raw_input()
    listaImion.append(imie)

print "Oto imiona:", listaImion
print "Oto posortowane imiona:", sorted(listaImion)
