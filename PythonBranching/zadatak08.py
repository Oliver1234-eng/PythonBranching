### Zadatak 8. Godina je prestupna ako je deljiva sa 4, osim ako je poslednja godina u veku, a tada je
### prestupna ako je deljiva sa 400 (na primer 1800 i 1900 nisu prestupne dok 1600 i 2000 jesu). Napisati
### funkciju koji proverava da li je godina prestupna.
### Primer izvršavanja programa:
### >>> print(prestupnaGodina(1983))
### nije prestupna
### >>> print(prestupnaGodina(1984))
### prestupna
### >>> print(prestupnaGodina(1900))
### nije prestupna
### >>> print(prestupnaGodina(2000))
### prestupna
def prestupnaGodina(year):
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    return 'Prestupna'
  else:
    return 'Nije prestupna'

print(prestupnaGodina(1983))
print(prestupnaGodina(1984))
print(prestupnaGodina(1900))
print(prestupnaGodina(2000))