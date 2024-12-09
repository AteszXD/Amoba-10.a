import jatektabla
import nyertesellenor

# 10x10 táblázat
tablazat = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

# Milyen jelet rakjon
jel = "X"
lepesszam = 0

# Hova tegye a jelet
while True: # Itt majd lesz konkrét check
    sor = int(input("Hányadik sorba szeretne tenni? (1-10) ")) 
    oszlop = int(input("Hányadik oszlopba szeretne tenni? (1-10) "))
    while not(sor > 0 and sor < 11) or not(oszlop > 0 and oszlop < 11):
        print("Valamelyik pozíció a táblázaton kívül esik!")
        sor = int(input("Hányadik sorba szeretne tenni? (1-10) ")) 
        oszlop = int(input("Hányadik oszlopba szeretne tenni? (1-10) "))
    while (tablazat[sor-1][oszlop-1]) != ' ':
        print("Ez a hely már foglalt!")
        sor = int(input("Hányadik sorba szeretne tenni? (1-10) ")) 
        oszlop = int(input("Hányadik oszlopba szeretne tenni? (1-10) ")) 
    (tablazat[sor-1][oszlop-1]) = jel
    jatektabla.jatektabla(tablazat)
    if lepesszam % 2 == 1:
        jel = "X"
    else:
        jel = "O"
    lepesszam += 1