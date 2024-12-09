import shutil
# Ez nem maga a tábla hanem inkább kezelő

def racsok(tablazat): # Ez a rácsokat fogja megrajzolni (legalábbis kéne)
    terminal_width = shutil.get_terminal_size().columns
    sorindex = -1  # Mert ha 0-ról kezdi és utólag csökkentem akkor valami sztrókot kap félúton a program

    for row in range(10):
        # Rácsok
        racssor = '+---' * 10 + '+'
        print(racssor.center(terminal_width)) 
        
        # A játéktábla kiírás
        racsoszlop = '|'
        sorindex += 1
        for oszlopindex in range(10):
            racsoszlop += f" {tablazat[sorindex][oszlopindex]} |"
        print(racsoszlop.center(terminal_width))
    
    # Utolsó rácssor
    racssor = '+---' * 10 + '+'
    print(racssor.center(terminal_width))


def ureshelyek(tablazat): # Ez megnézi van-e még üres hely a táblázatban
    for sor in tablazat:
        if ' ' in sor :
            return True
    return False

# Ez lett volna ami megnézi hogy integert írt-e a felhasználó de nem működött
"""
def bekeres(tablazat):
    while True: # Menjen örökké majd ha sikerül végig menni akkor kilép
            try: # Ha nincs baj:
                sor = int(input("Hányadik sorba szeretne tenni? (1-10) "))
                oszlop = int(input("Hányadik oszlopba szeretne tenni? (1-10) "))
                return sor, oszlop # Mert ha több sor akkor kilép az első return után
            except ValueError: # Ha van baj
                print("Ide számot kell írni!")
"""