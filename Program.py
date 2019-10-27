# Created by Kamil Kołodziejczyk
# v0.1
from random import randint


def licz(grupa_badanych):
    print(grupa_badanych, end="")
    policz1 = [poz for poz, wartosc in enumerate(grupa_badanych) if wartosc == 1]
    policz0 = [poz for poz, wartosc in enumerate(grupa_badanych) if wartosc == 0]
    print("\nLiczba osob ZA wynosi: " + str(len(policz1)) + " Liczba osob PRZECIW wynosi: " + str(len(policz0)) + "\n")


print(
    "Witaj w programie badającym zachowanie okreslonej populacji na zadane pytanie przy wykorzystaniu Modelu Sznajda.")
print("Program losuje okresloną liczbę (populację) o losowych \"zdaniach na dany temat\".")
print("Nastepnie nalezy określić ile powtórzeń ma on wykonać.")
print("Na zakończenie program okresli zdanie jakie populacja zajęła w danym temacie.")
print("Ps. 1 w liście symbolizują osoby wyrażające swoje zdanie ZA, zaś 0 oznacza PRZECIW.")

try:
    populacja = int(input("Określ badną populację: "))
    powtorzenia = int(input("Określ liczbę powtórzeń: "))
except Exception:
    print("W programie zadeklarowane zostały niepoprawne wartości!!!")
    print("W celu zaprezentowania działania programu domyślnie wykona sie on dla wartości: \nPopulacja: 100 osób \n"
          "Powtorzeń: 1000")
    populacja = 100
    powtorzenia = 1000

grupa_badanych = [randint(0, 1) for i in range(populacja)]
print("Wylosowana grupa badanych:")
licz(grupa_badanych)
p = 0
while p < powtorzenia:
    Si = randint(1, populacja - 3)
    if grupa_badanych[Si] == grupa_badanych[(Si + 1)]:
        grupa_badanych[(Si - 1)] = grupa_badanych[Si]

    elif grupa_badanych[Si] != grupa_badanych[(Si + 1)]:
        grupa_badanych[(Si - 1)] = grupa_badanych[(Si + 1)]
    grupa_badanych[(Si + 2)] = grupa_badanych[Si]
    p += 1
    print("Powtorzenie numer: " + str(p) + " " + "Wylosowana para: " + str(Si) + " i " + str(Si + 1))
licz(grupa_badanych)

input("Naciśnij dowolny klawisz aby zakończyć pracę programu")
