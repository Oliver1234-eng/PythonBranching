### Zadatak 4. Kazna za brzu vožnju računa se kao 5000 din + 500 din za svaki kilometar preko ograničenja + 10000 din 
### za vožnju preko 120km/h. Napisati funkciju koja prima izmerenu brzinu vozila i ograničenje
### brzine. Ako je brzina veća od dozvoljene funkcija vraća poruku sa cenom kazne, a ako je manja vraća
### poruku da je sve u redu.
### Primer izvršavanja programa:
### >>> print(kazna(80,60))
### vasa kazna iznosi 15000din
### >>> print(kazna(50,60))
### niste prekoracili brzinu
### >>> print(kazna(130,60))
### vasa kazna iznosi 50000din
def kazna(brzina, ogranicenje):
    if brzina <= ogranicenje:
        return "Niste prekoracili brzinu"
    else:
        kazna = 5000 + (brzina - ogranicenje) * 500
        if brzina > 120:
            kazna += 10000
        return "Vasa kazna iznosi " + str(kazna) + "din"

print(kazna(80,60))
print(kazna(50,60))
print(kazna(130,60))