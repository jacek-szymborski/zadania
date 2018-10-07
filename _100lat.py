#Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them
# the year that they will turn 100 years old.
import datetime

imie = input("Podaj swoje imie: ")
wiek = int(input("podaj swój wiek:"))
aktualny_rok = (datetime.datetime.now()).year
sto_lat = (aktualny_rok - wiek) + 100
rep = int(input('Podaj ilosc powtorzen: '))
r = 1
while r <= rep:
    print()
    print(f'Yo! {imie}!, będziesz mieć 100 lat w roku {sto_lat}!')
    r = r + 1
