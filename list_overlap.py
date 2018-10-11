a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
wynik = []

for a_el in a:
    if a_el in b:
        if a_el not in wynik:
            wynik.append(a_el)
print(wynik)
