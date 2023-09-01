### Zadatak 2. Napiši funkciju koja prima broj bodova na testu, a vraća ocenu sa testa. Student na testu
### može da osvoji od 0 do 100 bodova. Ocenjivanje je dato u tabeli:
###    bodovi    ocena
### od 0 do 55     5
### od 56 do 65    6
### od 66 do 75    7
### od 76 do 85    8
### od 86 do 95    9
### od 96 do 100  10
### Primer izvršavanja programa:
### >>> ocenjivanje(77)
### 8
### >>> ocenjivanje(95)
### 9
### >>> ocenjivanje(96)
### 10
def ocenjivanje(bodovi):
    if bodovi <= 55:
        print("Ocena: 5")
    elif bodovi <= 65:
        print("Ocena: 6")
    elif bodovi <= 75:
        print("Ocena: 7")
    elif bodovi <= 85:
        print("Ocena: 8")
    elif bodovi <= 95:
        print("Ocena: 9")
    else:
        print("Ocena: 10")

ocenjivanje(77)
ocenjivanje(95)
ocenjivanje(96)