def policz_samogloski(zdanie):
    liczba_elementow = 1
    for letter in zdanie:
        if letter == [A, a, e, i, o, u]:
            liczba_elementow = liczba_elementow + 1
    assert isinstance(letter, object)
    return letter

print(policz_samogloski("Ala ma kota"))
print(policz_samogloski("Pies psu niedzwiedziem, bo tak"))