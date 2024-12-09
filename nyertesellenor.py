def nyertesellenor(tablazat):
    # Sorok ellenőrzése
    for rowindex in range(10):
        for i in range(6):  # 5 egymás melletti mezőt keresése
            if tablazat[rowindex][i] != ' ' and tablazat[rowindex][i] == tablazat[rowindex][i+1] == tablazat[rowindex][i+2] == tablazat[rowindex][i+3] == tablazat[rowindex][i+4]:
                return True

    # Oszlopok ellenőrzése
    for colindex in range(10):
        for i in range(6):  # 5 egymás alatti mezőt keresése
            if tablazat[i][colindex] != ' ' and tablazat[i][colindex] == tablazat[i+1][colindex] == tablazat[i+2][colindex] == tablazat[i+3][colindex] == tablazat[i+4][colindex]:
                return True

    # 1. átló ellenőrzése (bal felsőtől jobb alsóig)
    for i in range(6):  # 5 egymás alatti mezőt keresünk az átlón
        if tablazat[i][i] != ' ' and tablazat[i][i] == tablazat[i+1][i+1] == tablazat[i+2][i+2] == tablazat[i+3][i+3] == tablazat[i+4][i+4]:
            return True

    # 2. átló ellenőrzése (jobb felsőtől bal alsóig)
    for i in range(4, 10):  # 5 egymás alatti mezőt keresünk az átlón
        if tablazat[i][9-i] != ' ' and tablazat[i][9-i] == tablazat[i-1][9-i+1] == tablazat[i-2][9-i+2] == tablazat[i-3][9-i+3] == tablazat[i-4][9-i+4]:
            return True

    return False