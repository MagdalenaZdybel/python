class Czas:
    def _init_(self, godzina = 0, minuta = 0, sekunda = 0):
        self.godzina = godzina
        self.minuta = minuta
        self.seunda = sekunda


class Zegar (Czas):
    def _init_(self, format_czasu, *args, **kwargs):
        super ().__init__ (*args, **kwargs)
        self.format_czasu = format_czasu


class DokladnyZegar (Zegar):
    def _init_(self, *args, milisek=0, **kwargs):
        super ().__init__ (*args, **kwargs)
        self.milisek = milisek


dokZeg = DokladnyZegar (11, sekunda=10, milisek=30, minuta=2)
zeg = Zegar (11, sekunda=10, minuta=2)
n_czas = Czas (godzina=1, sekunda=10, minuta=2)
print (n_czas.godzina)
print (n_czas.minuta)
print (n_czas.sekunda)
print (zeg)
print (dokZeg)
