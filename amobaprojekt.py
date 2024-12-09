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

# Milyen jelet rakjon (Később lesz meghívva)
jel = "X" # Feltételezzük, hogy X kezd
lepesszam = 0

# Hova tegye a jelet
while jatektabla.ureshelyek(tablazat) == True: # Ha esetleg mind a 100 hely foglalt akkor a játék érjen véget
    
    # Első bekérés
    sor = int(input("Hányadik sorba szeretne tenni? (1-10) ")) 
    oszlop = int(input("Hányadik oszlopba szeretne tenni? (1-10) "))

    # Táblázaton belüli koordinátát írt-e a user
    while not(sor >= 1 and sor <= 10) or not(oszlop >= 1 and oszlop <= 10):
        print("Valamelyik pozíció a táblázaton kívül esik!")
        sor = int(input("Hányadik sorba szeretne tenni? (1-10) ")) 
        oszlop = int(input("Hányadik oszlopba szeretne tenni? (1-10) "))
    
    # Üres-e a mező ahova rak a user
    while (tablazat[sor-1][oszlop-1]) != ' ':
        print("Ez a hely már foglalt!")
        sor = int(input("Hányadik sorba szeretne tenni? (1-10) ")) 
        oszlop = int(input("Hányadik oszlopba szeretne tenni? (1-10) "))

    # A jel berakása
    (tablazat[sor-1][oszlop-1]) = jel

    # Kiírjuk a játéktáblát
    jatektabla.racsok(tablazat)

    # Megnézzük, nyert-e már valaki
    if nyertesellenor.nyertesellenor(tablazat):
        print(f"Gratulálunk! {jel} játékos nyert!")
        break # Itt kilépünk a ciklusból, a játéknak vége

    # Beállítjuk, hogy milyen jelet tesz a user a következő körben
    lepesszam += 1
    if lepesszam % 2 == 0:
        jel = "X"
    else:
        jel = "O"