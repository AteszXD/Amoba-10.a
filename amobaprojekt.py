# 10x10 táblázat
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

# Milyen jelet rakjon
jel = "x"
lepesszam = 0
for i in range(5):
    input("Hova rak? ")
    if lepesszam % 2 == 0:
        jel = "x"
    else:
        jel = "o"
    print(jel)
    lepesszam += 1
    