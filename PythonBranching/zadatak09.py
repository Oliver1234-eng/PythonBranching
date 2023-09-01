### Zadatak 9. Napiši funkciju koji datum prima u obliku dd/mm/gggg i proverava da li je datum validan. Na
### primer 24/5/1962 je validan datu, ali 31/9/2000 nije jer septembar nema 31 dan. Takođe voditi računa i o 
### tome da li je godina prestupna.
def prestupnaGodina(godina):
  if godina % 4 == 0 and (godina % 100 != 0 or godina % 400 == 0):
    return 'Prestupna'
  else:
    return 'Nije prestupna'
    
def validanDatum(dan, mesec, godina):
  prestupna = prestupnaGodina(godina)
  meseci = [1, 3, 5, 7, 8, 10, 12]
  
  if mesec == 2:
    if prestupna == 'Prestupna':
      if dan > 0 and dan <= 29:
        return 'Validan datum'
    else:
      if dan > 0 and dan <= 28:
        return 'Validan datum'
  else:
    if mesec in meseci and dan > 0 and dan <= 31:
      return 'Validan datum'
    elif mesec not in meseci and dan > 0 and dan <= 30:
      return 'Validan datum'
  return 'Nevalidan datum'

print(validanDatum(24, 5, 1962))
print(validanDatum(31, 9, 2000))