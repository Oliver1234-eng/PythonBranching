### Zadatak 6. Datum na koji pada uskrs u Gregorijanskom kalendaru za godine 1982–2048 se računa po formuli:
### a = year % 19;
### b = year % 4;
### c = year % 7;
### d = (19a + 24) % 30;
### e = (2b + 4c + 6d + 5) % 7
### Datum na koji pada uskrs je 22 + d + e mart (ako je vrednost veća od 31 onda je april). Napiši funkciju koja
### računa datum uskrsa. Funkcija kao parametar prima godinu i vraća poruku sa informacijom kada je uskrs
### ako je godina u zadatom opsegu, odnosno poruku da je došlo do greške ako godina nije u zadatom opsegu.
### Primer izvršavanja programa:
### >>> print(uskrs(1994))
### uskrs je 29. marta 1994. godine
### >>> print(uskrs(2011))
### uskrs je 19. aprila 2011. godine
### >>> print(uskrs(1962))
### godina nije u predviñenom opsegu

def uskrs(year):
  if year < 1982 or year > 2048:
    return 'Godina nije u predvidjenom opsegu.'
  else:
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    datum = 22 + d + e
    if datum > 31:
      return 'Uskrs je {} aprila {} godine.'.format(datum - 31, year)
    else:
      return 'Uskrs je {} marta {} godine.'.format(datum, year)

print(uskrs(1994))
print(uskrs(2011))
print(uskrs(1962))