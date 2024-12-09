def jatektabla(tablazat):
    sorindex = -1 # Mert ha 0-ról kezdi és utólag csökkentem akkor valami sztrókot kap félúton a program
    for row in range(10):
        # A Nemes Tihamérről vett amőba '+-+-+-+\n| | | |' megoldás erősen átalakítva
        row = '+---' * 10 + '+' 
        print(row) 
        print('|', end='')
        sorindex += 1
        for oszlopindex in range(10):
            print(f" {tablazat[sorindex][oszlopindex]} ", end='|')
        print() # Új sor hogy ne egy emeletes E betű legyen az egész
    print('+---' * 10 + '+')