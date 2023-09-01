### Zadatak 10. Napiši program koji prima datum u obliku dd/mm/gggg i računa redni broj dana u godini.
### Redni broj dana u godini se računa na sledeći način:
### 1. danUGodini = 31(mm - 1) + dd
### 2. ako je mm posle februara danUGodini umanji za (4mm+23)/10
### 3. ako je prestupna godina i mm posle februara danUGodini uvećaj za 1
def prestupnaGodina(godina):
  if godina % 4 == 0 and (godina % 100 != 0 or godina % 400 == 0):
    return 'Prestupna'
  else:
    return 'Nije prestupna'

def redniBrojDana(dan, mesec, godina, prestupna):
  danUGodini = 31 * (mesec - 1) + dan
  if mesec > 2:
    danUGodini -= (4 * mesec + 23) // 10
  
  if prestupna == True and mesec > 2:
    danUGodini += 1
    
  return danUGodini

print(redniBrojDana(24, 5, 1962, prestupnaGodina(1962)))
print(redniBrojDana(31, 9, 2000, prestupnaGodina(2000)))