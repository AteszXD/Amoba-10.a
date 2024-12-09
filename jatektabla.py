import shutil

def racsok(tablazat):
    terminal_width = shutil.get_terminal_size().columns
    sorindex = -1  # Mert ha 0-ról kezdi és utólag csökkentem, akkor valami sztrókot kap félúton a program

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


def ureshelyek(tablazat):
    for sor in tablazat:
        if ' ' in sor :
            return True
    return False