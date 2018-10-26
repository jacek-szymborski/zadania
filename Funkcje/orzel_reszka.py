import random

def losuj():
    rzut = int(random.randint(0, 1))
    return rzut

def zliczaj():
    orzel = 0
    reszka = 0
    i = 0
    while i < 100:
        i = i + 1
        if losuj() == 0:
            orzel += 1
        else:
            reszka += 1
    return orzel, reszka

def wyniki():
    a = zliczaj()
    print(f"{a[0]} razy orzeł, {a[1]} razy reszka")

wyniki()