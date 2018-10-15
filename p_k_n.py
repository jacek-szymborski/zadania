p1_name = input("Podaj Imie Gracza 1: ")
p2_name = input("Podaj Imie Gracza 2: ")
p1_gra = None
p2_gra = None

while True:

    p1_gra = input(f"{p1_name}: P,K,M?:")
    p2_gra = input(f"{p2_name}: P,K,M?:")
    if p1_gra == "P" and p2_gra == "P":
        print(f"{p1_name}:{p1_gra} {p2_name}:{p2_gra} REMIS")
    elif p1_gra == "N" and p2_gra == "N":
        print(f"{p1_name}:{p1_gra} {p2_name}:{p2_gra} REMIS")
    elif p1_gra == "K" and p2_gra == "K":
        print(f"{p1_name}:{p1_gra} {p2_name}:{p2_gra} REMIS")
    elif p1_gra == "P" and p2_gra == "N":
        print(f"{p1_name}:{p1_gra} {p2_name}:{p2_gra} - Wygrywa {p2_name}")
    elif p1_gra == "P" and p2_gra == "K":
        print(f"{p1_name}:{p1_gra} {p2_name}:{p2_gra} - Wygrywa {p1_name}")
    elif p1_gra == "N" and p2_gra == "P":
        print(f"{p1_name}:{p1_gra} {p2_name}:{p2_gra} - Wygrywa {p1_name}")
    elif p1_gra == "N" and p2_gra == "K":
        print(f"{p1_name}:{p1_gra} {p2_name}:{p2_gra} - Wygrywa {p2_name}")
    elif p1_gra == "K" and p2_gra == "P":
        print(f"{p1_name}:{p1_gra} {p2_name}:{p2_gra} - Wygrywa {p2_name}")
    elif p1_gra == "K" and p2_gra == "N":
        print(f"{p1_name}:{p1_gra} {p2_name}:{p2_gra} - Wygrywa {p1_name}")
    else:
        break
