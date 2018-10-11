liczba = int(input("Podaj liczbę: " ))

if liczba % 2 == 0 and liczba % 4 == 0:
    print("To jest liczba parzysta i podzielna przez 4")
elif liczba % 2 == 0:
    print("To jest liczba parzysta")
elif liczba % 2 != 0:
    print("To jest liczba nieparzysta")
