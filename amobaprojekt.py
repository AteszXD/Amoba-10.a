# 10x10 táblázat

# Megoldás 1, ez kirajzolja, bár indexezni nem tudom hogy fogjuk
"""
def Jatekter():
    print("┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐")
    for _ in range(9):
        print("│   |   |   |   |   |   |   |   |   |   |")
        print("├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print("│   |   |   |   |   |   |   |   |   |   |")
    print("└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘")
    
Jatekter()
"""

# Megoldás 2, indexelt, de nem rácsos, Amíg nincs rács addig tesztnek az E betű lesz (E = Empty)

tablazat = [
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']
]

# Milyen jelet rakjon
jel = "X"
lepesszam = 0

# Hova tegye a jelet
while True: # Itt majd lesz konkrét ellenőrzés
    sor = int(input("Hányadik sorba szeretne tenni? (1-10) ")) 
    oszlop = int(input("Hányadik oszloba szeretne tenni? (1-10) "))
    while not(sor > 0 and sor < 11) or not(oszlop > 0 and oszlop < 11):
        print("Valamelyik pozíció a táblázaton kívül esik!")
        sor = int(input("Hányadik sorba szeretne tenni? (1-10) ")) 
        oszlop = int(input("Hányadik oszloba szeretne tenni? (1-10) "))
    while (tablazat[sor-1][oszlop-1]) != 'E':
        print("Ez a hely már foglalt!")
        sor = int(input("Hányadik sorba szeretne tenni? (1-10) ")) 
        oszlop = int(input("Hányadik oszloba szeretne tenni? (1-10) ")) 
    (tablazat[sor-1][oszlop-1]) = jel
    for sor in tablazat:
        print(' '.join(sor))
    if lepesszam % 2 == 1:
        jel = "X"
    else:
        jel = "O"
    lepesszam += 1