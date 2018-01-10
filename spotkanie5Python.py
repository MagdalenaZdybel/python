#Wyobraźmy sobie klasę "Człowiek" z metodą "mowa" i podklasę "Człowieka" - "Polityk" z metodami
# "przyjmij łapówkę" i "kłam". Domyślnie "Człowiek" po wykonaniu metody "mów" (speak) wypisze "Mowie prawdę",
#  każda instancja "Polityka" powie "Kłamie, bo mogę", chyba że wcześniej została wykonana metoda "przyjmij łapówkę"
#  (recive_bribe), wtedy powie prawdę.

class Czlowiek:
   # alive = True
    def __init__(self, imie, wzrost, waga):
        self.imie = imie
        self.wzrost = wzrost
        self.waga = waga

    def speak(self):
        print("Mówię prawdę")

    def count_bmi(self):
        pass

    def diff_to_norm(self):
        pass

    def save_data(self):
        pass

    def to_burn(self):
        pass

    def to_eat(self):
        pass

    def what_to_do(self):
        pass

class Polityk(Czlowiek):
    bribed = False
    def speak(self):
        if self.bribed:
            super().speak()
        else:
            print("Kłamię, bo mogę")

    def recive_bribe(self):
        self.bribed - True

antoni = Polityk('Antoni', 20, 120)
kajetan = Polityk('Kajetan', 25, 150)
zuzik = Czlowiek('Zuzik', 15, 160)
antoni.speak()
antoni.recive_bribe()
antoni.speak()
kajetan.speak()
zuzik.speak()