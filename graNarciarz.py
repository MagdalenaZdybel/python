import pygame
import sys
import random


narciarz_rysunki = ["skier_down.png","skier_right1.png",
           "skier_right2.png","skier_left2.png",
           "skier_left1.png"]

class KlasaNarciarz(pygame.sprite.Sprite):           #narciarz
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("skier_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.nachylenie  = 0

    def obroc(self, kierunek):                          #obracamy narciarza
        self.nachylenie = self.nachylenie + kierunek
        if self.nachylenie < -2: self.nachylenie = -2
        if self.nachylenie > 2: self.nachylenie = 2
        srodek = self.rect.center
        self.image = pygame.image.load(narciarz_rysunki[self.nachylenie])
        self.rect = self.image.get_rect()
        self.rect.center = srodek
        predkosc = [self.nachylenie, 6 - abs(self.nachylenie) *2]
        return predkosc

    def przesun(self, predkosc):                                 #przesuwanie narciarza lewo - prawo
        self.rect.centerx = self.rect.centerx + predkosc[0]
        if self.rect.centerx < 20: self.rect.centerx = 20
        if self.rect.centerx > 620: self.rect.centerx = 620



class KlasaPrzeszkoda(pygame.sprite.Sprite):                    #drzewka i flagi
    def __init__(self, plik_graficzny, pole, rodzaj):
        pygame.sprite.Sprite.__init__(self)
        self.plik_graficzny = plik_graficzny
        self.image = pygame.image.load(plik_graficzny)
        self.rect = self.image.get_rect()
        self.rect.center = pole
        self.rodzaj = rodzaj
        self.zaliczona = False
    def update(self):           #przesuniecie tła do góry
        global predkosc
        self.rect.centery -= predkosc[1]
        if self.rect.centery < -32:     #usuniecie przeszkody, ktora jest poza gorną krawędź ekranu
            self.kill()

def utworz_mape():              #tworzymy ekran wypelniony drzewkami i flagami rozmieszonymi LOSOWO
    global przeszkody
    zajete_pola = []
    for i in range(10):
        wiersz = random.randint(0, 9)
        kolumna = random.randint(0, 9)
        pole = [kolumna * 64 +20, wiersz * 64 + 20 +640]
        if not (pole in zajete_pola):
            zajete_pola.append(pole)
            rodzaj = random.choice(["drzewko", "flaga"])
            if rodzaj == "drzewko": rysunek = "skier_tree.png"
            elif rodzaj == "flaga": rysunek = "skier_flag.png"
            przeszkoda = KlasaPrzeszkoda(rysunek, pole, rodzaj)
            przeszkody.add(przeszkoda)


def animuj():                                         #odmalowanie ekranu
    ekran.fill([255, 255, 255])
    przeszkody.draw(ekran)
    ekran.blit(narciarz.image, narciarz.rect)
    ekran.blit(wynik_tekst, [10, 10])
    pygame.display.flip()

pygame.init()                                   #przygotowanie gry
ekran = pygame.display.set_mode([640, 640])
zegar = pygame.time.Clock()
narciarz = KlasaNarciarz()
predkosc = [0, 6]
przeszkody = pygame.sprite.Group()
pozycja_mapy = 0
punkty = 0
utworz_mape()
czcionka = pygame.font.Font(None, 50)

uruchomiona = True              #początek głównej pętl
while uruchomiona:
    zegar.tick(30) #akutalizujemy grafikę 30 razy na sekundę
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT: uruchomiona = False
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_LEFT:
                predkosc = narciarz.obroc(-1)
            elif  zdarzenie.key == pygame.K_RIGHT:
                predkosc = narciarz.obroc(1)
    narciarz.przesun(predkosc)

    pozycja_mapy += predkosc[1]  #przesuwamy tło

    if pozycja_mapy >=640:   #tworzymy nowy ekran pełen przeszkod
        utworz_mape()
        pozycja_mapy = 0

    kolizja = pygame.sprite.spritecollide(narciarz, przeszkody, False)  #sprawdzamy czy narciarz uderzył w drzewo lub zabrał
    if kolizja:                                                             #flagę
        if kolizja[0].rodzaj == "drzewko" and not kolizja[0].zaliczona:
            punkty - punkty - 100
            narciarz.image = pygame.image.load("skier_crash.png")
            animuj()
            pygame.time.delay(1000)
            narciarz.image = pygame.image.load("skier_down.png")
            narciarz.nachylenie = 0
            predkosc = [0, 6]
            kolizja[0].zaliczona = True
        elif kolizja[0].rodzaj == "flaga" and not kolizja[0].zaliczona:
            punkty += 10
            kolizja[0].kill()

    przeszkody.update()
    wynik_tekst = czcionka.render("Wynik: " + str(punkty), 1, (0, 0, 0))    #wyświetlenie wyniku
    animuj()
pygame.quit()





