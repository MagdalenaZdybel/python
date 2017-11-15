print("wprowadz liczbę dla któej chcesz wyświetlić tabliczkę możenia: ")
podanaLiczba = int(input())
dlugoscLiczby = int(input("jak dluga ma byc tabliczka? "))
print("Oto tabliczka: ")
i = 1
while i <= dlugoscLiczby:
    print(podanaLiczba," x ", i, "=", podanaLiczba * i)
    i = i + 1



